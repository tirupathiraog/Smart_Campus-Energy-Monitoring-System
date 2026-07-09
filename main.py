import threading
import time
import pandas as pd
from datetime import datetime

from fastapi import Query
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy import text

from database import engine

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# ---------------- MODEL ----------------
class Energy(BaseModel):
    building: str
    room: str
    timestamp: datetime
    power_kwh: float


# ---------------- UPLOAD ----------------
@app.post("/upload")
def upload_data(data: Energy):
    with engine.begin() as conn:
        conn.execute(text("""
            INSERT INTO energy_readings (building, room, timestamp, power_kwh)
            VALUES (:building, :room, :timestamp, :power_kwh)
        """), data.dict())
    return {"message": "stored"}


# ---------------- BACKGROUND ----------------
def background_detection():
    while True:
        try:
            df = pd.read_sql(
                "SELECT * FROM energy_readings ORDER BY timestamp DESC LIMIT 20",
                engine
            )

            if not df.empty:

                df['timestamp'] = pd.to_datetime(df['timestamp'])
                df['avg'] = df['power_kwh'].rolling(window=5).mean()

                latest = df.iloc[0]
                avg_value = df['avg'].iloc[-1]

                # -------- LOGIC --------
                if latest['power_kwh'] < 5:
                    risk_score = 10
                    alert_type = "Low Usage"

                elif latest['power_kwh'] < 50:
                    if pd.notna(avg_value) and latest['power_kwh'] > avg_value + 5:
                        risk_score = 40
                        alert_type = "Moderate Spike"
                    else:
                        risk_score = 20
                        alert_type = "Stable"

                else:
                    risk_score = 80
                    alert_type = "High Usage"

                # ✅ ONLY STORE REAL ALERTS
                if risk_score < 40:
                    continue

                # -------- DUPLICATE CHECK --------
                with engine.begin() as conn:
                    exists = conn.execute(text("""
                        SELECT COUNT(*) FROM energy_alerts
                        WHERE building = :building
                        AND room = :room
                        AND alert_type = :alert_type
                        AND DATE(timestamp) = CURRENT_DATE
                    """), {
                        "building": latest['building'],
                        "room": latest['room'],
                        "alert_type": alert_type
                    }).scalar()

                    if exists == 0:
                        conn.execute(text("""
                            INSERT INTO energy_alerts
                            (timestamp, building, room, risk_score, alert_type)
                            VALUES (:timestamp, :building, :room, :risk_score, :alert_type)
                        """), {
                            "timestamp": datetime.now(),
                            "building": latest['building'],
                            "room": latest['room'],
                            "risk_score": risk_score,
                            "alert_type": alert_type
                        })

        except Exception as e:
            print("Error:", e)

        time.sleep(10)


@app.on_event("startup")
def start_bg():
    t = threading.Thread(target=background_detection)
    t.daemon = True
    t.start()


# ---------------- APIs ----------------

@app.get("/energy/history")
def energy(building: str = Query("All")):

    if building == "All":

        query = """
        SELECT *
        FROM energy_readings
        ORDER BY timestamp DESC
        LIMIT 50
        """

        df = pd.read_sql(query, engine)

    else:

        query = """
        SELECT *
        FROM energy_readings
        WHERE building = %(building)s
        ORDER BY timestamp DESC
        LIMIT 50
        """

        df = pd.read_sql(
            query,
            engine,
            params={"building": building}
        )

    return df.to_dict(orient="records")


@app.get("/alerts")
def alerts():

    query = """
    SELECT
        a.id,
        a.timestamp,
        a.building,
        a.room,
        a.risk_score,
        a.alert_type,
        r.power_kwh
    FROM energy_alerts a

    LEFT JOIN LATERAL (
        SELECT power_kwh
        FROM energy_readings
        WHERE building = a.building
        ORDER BY timestamp DESC
        LIMIT 1
    ) r ON TRUE

    ORDER BY a.timestamp DESC
    LIMIT 20
    """

    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")


# ✅ FIXED SUMMARY (NO undefined)
@app.get("/summary")
def summary():

    energy_df = pd.read_sql("SELECT * FROM energy_readings", engine)
    alerts_df = pd.read_sql("SELECT * FROM energy_alerts ORDER BY timestamp DESC", engine)

    total_readings = len(energy_df)
    total_alerts = len(alerts_df)

    # ✅ default LOW (fix undefined)
    current_risk = "LOW"

    if not alerts_df.empty:
        latest = alerts_df.iloc[0]["risk_score"]

        if latest >= 70:
            current_risk = "HIGH"
        elif latest >= 30:
            current_risk = "MEDIUM"

    return {
        "total_readings": total_readings,
        "total_alerts": total_alerts,
        "current_risk": current_risk
    }


# ✅ FIXED BLOCK DATA (NO undefined)
@app.get("/block/summary")
def block_summary():

    query = """
    SELECT DISTINCT ON (building)
        building,
        room,
        power_kwh
    FROM energy_readings
    ORDER BY building, timestamp DESC
    """

    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")

# ---------------- DASHBOARD ----------------
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})