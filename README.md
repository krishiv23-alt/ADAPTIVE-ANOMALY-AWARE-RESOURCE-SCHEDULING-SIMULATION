# 🚀 Adaptive Anomaly-Aware Resource Scheduler Simulation

A web-based simulation of a Kubernetes-like cluster that integrates **real-time resource monitoring, anomaly detection, adaptive scheduling, and self-healing mechanisms**. This project visualizes how distributed systems manage workloads dynamically under varying conditions.

---

## 📌 Overview

This project models a container orchestration environment where **pods (workloads)** are scheduled across **nodes (compute resources)**. It demonstrates how systems detect anomalies, rebalance loads, and recover from failures in real time.

The simulation includes an interactive dashboard to monitor cluster behavior, making it ideal for **operating systems and distributed systems projects**.

---

## ✨ Features

* ⚙️ **Adaptive Scheduling** – Dynamically allocates pods to nodes
* 📊 **Real-Time Monitoring** – Tracks CPU & memory usage
* ⚠️ **Anomaly Detection** – Identifies abnormal workloads
* 🔄 **Pod Migration** – Moves pods to balance load
* 🛠 **Self-Healing** – Restarts crashed pods automatically
* 📈 **Live Graphs** – Visualizes CPU load and system health
* 📜 **Activity Logs** – Displays real-time scheduler events

---

## 🏗️ System Architecture

```
Frontend (HTML/CSS/JS Dashboard)
        ↑
Flask API (Backend Server)
        ↑
Simulation Engine (Scheduler + Cluster Model)
```

---

## 🧰 Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript
* **Visualization:** Chart.js
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
scheduler-simulation
│
├── app.py
├── simulation.py
│
├── templates
│   └── index.html
│
└── static
    └── style.css
```

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/krishiv23-alt/ADAPTIVE-ANOMALY-AWARE-RESOURCE-SCHEDULING-SIMULATION
```

2. Navigate to the project:

```
cd adaptive-scheduler-simulation
```

3. Install dependencies:

```
pip install flask
```

4. Run the application:

```
python app.py
```

5. Open in browser:

```
http://127.0.0.1:5000
```

---

## 📊 Dashboard Preview

The dashboard includes:

* 🖥️ **Cluster View:** Nodes and pods
* 📈 **CPU Usage Graph:** Real-time load monitoring
* 🥧 **Status Chart:** Running / Anomaly / Crash distribution
* 📜 **Activity Panel:** Live scheduler events

---

## 🧠 Key Concepts Demonstrated

* Container Scheduling
* Load Balancing
* Distributed System Monitoring
* Fault Tolerance & Self-Healing
* Real-Time Simulation

---

## 📌 Use Cases

* Academic projects (OS / Distributed Systems)
* Research simulations
* Learning Kubernetes concepts visually
* Demonstrating scheduling algorithms

---

## 🚀 Future Enhancements

* Advanced scheduling algorithms (Round Robin, Priority, EDF)
* Machine learning-based anomaly detection
* Node load heatmaps
* Larger cluster simulation (100+ pods)
* Real Kubernetes API integration

---

## 👨‍💻 Author

* **Krishiv Chopra**
* **Anishka Shah**
* **Anshika Kumar**

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star!
