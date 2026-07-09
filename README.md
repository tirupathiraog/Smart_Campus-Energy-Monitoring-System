# ⚡ Smart Campus Energy Monitoring System

<p align="center">
  <img src="screenshots/Dashboard.png" alt="Dashboard" width="100%">
</p>

## 📖 Project Overview

The **Smart Campus Energy Monitoring System** is a web-based application designed to monitor and analyze electricity consumption across campus buildings in real time. The system collects energy data, detects abnormal power usage, generates alerts, and presents the information through an interactive dashboard.

This project was developed as part of the **Master of Computer Applications (MCA)** program to demonstrate real-time monitoring, data visualization, and anomaly detection using modern web technologies.

---

## ✨ Features

- ⚡ Real-time energy monitoring
- 📊 Interactive dashboard with live statistics
- 📈 Energy consumption trend visualization
- 🚨 Automatic anomaly detection and alert generation
- 🏢 Building-wise energy monitoring
- 📋 Recent alerts display
- 🔄 Auto-refresh dashboard
- 📉 Energy usage analytics

---

## 🛠️ Technologies Used

### Backend
- Python
- FastAPI

### Database
- PostgreSQL

### Frontend
- HTML5
- CSS3
- JavaScript
- Chart.js

### Development Tools
- Visual Studio Code
- Git
- GitHub

---

## 📂 Project Structure

```text
Smart-Campus-Energy-Monitoring-System/
│
├── templates/
│   └── index.html
│
├── screenshots/
│   ├── Dashboard.png
│   ├── Energy building.png
│   ├── Energy chart.png
│   └── Recent alerts.png
│
├── database.py
├── detection.py
├── generator.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/tirupathiraog/Smart_Campus-Energy-Monitoring-System.git
```

### 2. Navigate to the Project

```bash
cd Smart_Campus-Energy-Monitoring-System
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
uvicorn main:app --reload
```

The application will be available at:

```
http://127.0.0.1:8000
```

---

## 📸 Screenshots

### 🖥️ Dashboard

![Dashboard](screenshots/Dashboard.png)

The dashboard provides a complete overview of the Smart Campus Energy Monitoring System, displaying live status, key metrics, and real-time energy information.

---

### 📈 Energy Trend Chart

![Energy Trend](screenshots/Energy%20chart.png)

The energy trend chart visualizes power consumption over time, helping identify energy usage patterns and sudden spikes.

---

### 🏢 Building Energy Monitoring

![Building Monitoring](screenshots/Energy%20building.png)

This section shows building-wise energy consumption, allowing administrators to compare energy usage across different campus buildings.

---

### 🚨 Recent Alerts

![Recent Alerts](screenshots/Recent%20alerts.png)

Recent alerts display abnormal energy consumption detected by the system, enabling quick identification of potential issues.

---

## ⚙️ System Workflow

1. Generate energy consumption data.
2. Store readings in PostgreSQL.
3. Detect abnormal energy usage.
4. Generate alerts automatically.
5. Display live information on the dashboard.
6. Monitor building-wise energy consumption.
7. Visualize trends using interactive charts.

---

## 🎯 Project Objectives

- Monitor campus energy consumption in real time.
- Detect unusual energy usage automatically.
- Provide interactive dashboards for analysis.
- Improve awareness of energy utilization.
- Support efficient campus energy management.

---

## 🔮 Future Enhancements

- AI-based energy consumption prediction
- Email and SMS notifications
- Mobile application
- Cloud deployment (AWS/Azure)
- User authentication and role management
- Monthly energy reports
- Energy forecasting using Machine Learning

---

## 👨‍💻 Author

**Tirupathi Rao G**

Master of Computer Applications (MCA)

---

## 🤝 Contributions

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project was developed for educational purposes as part of an MCA academic project.
