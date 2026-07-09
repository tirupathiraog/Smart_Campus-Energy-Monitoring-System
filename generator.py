import requests
import random
import time
from datetime import datetime

API_URL = "http://127.0.0.1:8000/upload"

BUILDINGS = {
"Degree Block": ["Lab1", "Lab2", "Lab3"],
"Engineering Block": ["Lab1", "Lab2"],
"Library": ["Reading Hall", "Digital Section"],
"Admin Block": ["Office", "Accounts"],
"Computer Science Block": ["Lab1", "Lab2", "Project Lab"],
"Mechanical Block": ["Workshop", "CAD Lab"],
"Civil Block": ["Survey Lab", "Material Lab"],
"Electronics Block": ["Embedded Lab", "VLSI Lab"],
"Hostel Block": ["Floor1", "Floor2", "Common Area"],
"Cafeteria": ["Kitchen", "Dining Hall"]
}

def generate():

    building = random.choice(list(BUILDINGS.keys()))
    room = random.choice(BUILDINGS[building])

    hour = datetime.now().hour

    if 8 <= hour <= 18:
        power = random.uniform(8, 15)
    else:
        power = random.uniform(1, 3)

    # spike
    if random.random() < 0.2:
        power += random.uniform(20, 80)

    return {
        "building": building,
        "room": room,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "power_kwh": round(power, 2)
    }


def send():

    while True:
        data = generate()

        try:
            requests.post(API_URL, json=data)
            print("Sent:", data)
        except Exception as e:
            print("Error:", e)

        time.sleep(10)


if __name__ == "__main__":
    print("Generator Running...")
    send()