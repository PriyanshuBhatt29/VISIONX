# 🔴 VISIONX
## BLACK / RED PERFORMANCE COMPUTER VISION SYSTEM

<div align="center">

**SEE. TRACK. ANALYZE. RESPOND.**

A high-performance computer vision system built around precision, speed and visual intelligence.

![Python](https://img.shields.io/badge/Python-0A0A0A?style=for-the-badge&logo=python&logoColor=FF1744)
![YOLO](https://img.shields.io/badge/YOLO-0A0A0A?style=for-the-badge&logo=yolo&logoColor=FF1744)
![OpenCV](https://img.shields.io/badge/OpenCV-0A0A0A?style=for-the-badge&logo=opencv&logoColor=FF1744)
![FastAPI](https://img.shields.io/badge/FastAPI-0A0A0A?style=for-the-badge&logo=fastapi&logoColor=FF1744)
![WebSocket](https://img.shields.io/badge/WebSocket-0A0A0A?style=for-the-badge&logo=socketdotio&logoColor=FF1744)
![Docker](https://img.shields.io/badge/Docker-0A0A0A?style=for-the-badge&logo=docker&logoColor=FF1744)

</div>

---

## ⚡ What is VISIONX?

VISIONX is a modular real-time CV platform designed around one principle:

> **Raw pixels → detections → tracked entities → measurable intelligence.**

It combines YOLO object detection, OpenCV video processing, lightweight tracking, event analytics, FastAPI and WebSockets into a single system.

### Core capabilities

- 🎯 Real-time object detection
- 👥 Multi-object tracking
- 🚶 Person counting
- 🚧 Virtual line-crossing events
- 📈 Live FPS / latency telemetry
- 🎥 Webcam and video-file pipelines
- 🔌 REST + WebSocket APIs
- 🖥️ Black/red performance dashboard
- 🐳 Docker-ready deployment
- 🧪 Automated tests

---

## 🧠 System Architecture

```text
┌──────────────┐
│ CAMERA/VIDEO │
└──────┬───────┘
       ↓
┌─────────────────┐
│ OpenCV Pipeline │
└──────┬──────────┘
       ↓
┌─────────────────┐
│ YOLO Detector   │
└──────┬──────────┘
       ↓
┌─────────────────┐
│ Object Tracker  │
└──────┬──────────┘
       ↓
┌────────────────────┐
│ Analytics Engine   │
│ count • events     │
│ line crossing      │
│ FPS • latency      │
└──────┬─────────────┘
       ↓
┌────────────────────┐
│ FastAPI + WebSocket│
└──────┬─────────────┘
       ↓
┌────────────────────┐
│ VISIONX Dashboard  │
└────────────────────┘
```

---

## 🔥 Engineering Highlights

### Detection
YOLO inference produces bounding boxes, class labels and confidence scores.

### Tracking
VISIONX assigns lightweight persistent IDs to detected objects using centroid association, allowing objects to be followed across frames.

### Event Intelligence
The analytics layer can calculate:

- Current objects
- Unique tracked objects
- People count
- Line-crossing events
- Average confidence
- Processing FPS
- Frame latency

### API
The backend exposes:

| Endpoint | Purpose |
|---|---|
| `GET /api/health` | System health |
| `GET /api/stats` | Current analytics |
| `POST /api/detect` | Detect objects in an image |
| `WS /ws/live` | Live inference stream |

---

## 🚀 Quick Start

### 1. Clone

```bash
git clone https://github.com/PriyanshuBhatt29/VISIONX.git
cd VISIONX
```

### 2. Install

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Start

```bash
uvicorn backend.main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

The first YOLO inference downloads the configured model automatically.

---

## 🐳 Docker

```bash
docker compose up --build
```

---

## 📁 Project Structure

```text
VISIONX/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── detector.py
│   ├── tracker.py
│   ├── analytics.py
│   └── schemas.py
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── styles.css
├── tests/
│   ├── test_tracker.py
│   └── test_analytics.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧪 Testing

```bash
pytest -q
```

The tests cover tracker identity behavior and analytics calculations independently from the model.

---

## 🎯 Why this project matters

VISIONX demonstrates more than calling a pretrained model.

It shows the complete engineering path:

**Computer Vision → State → Events → API → Real-Time UI → Deployment**

That makes it suitable as a portfolio project for AI/ML, computer vision and AI engineering roles.

---

## 🛣️ Roadmap

- [x] Detection pipeline
- [x] Centroid tracking
- [x] Analytics engine
- [x] REST API
- [x] WebSocket architecture
- [x] Futuristic dashboard
- [x] Docker support
- [x] Tests
- [ ] GPU deployment profile
- [ ] ByteTrack integration
- [ ] PostgreSQL event storage
- [ ] Multi-camera support
- [ ] Alert rules
- [ ] Production observability

---

<div align="center">

### ◢ VISIONX // NEURAL VISION SYSTEM ◣

**BUILT TO SEE WHAT SOFTWARE CAN'T.**

</div>
