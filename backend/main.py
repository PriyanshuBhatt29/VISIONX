import time
from contextlib import asynccontextmanager

import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .analytics import AnalyticsEngine
from .detector import annotate, detect
from .tracker import CentroidTracker


tracker = CentroidTracker()
analytics = AnalyticsEngine()
MODEL_NAME = "yolo11n.pt"


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="VISIONX",
    version="1.0.0",
    description="Real-time computer vision intelligence platform",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/")
async def root():
    return FileResponse("frontend/index.html")


@app.get("/api/health")
async def health():
    return {"status": "online", "system": "VISIONX", "model": MODEL_NAME}


@app.get("/api/stats")
async def stats():
    return {
        "active_objects": len(tracker.tracks),
        "unique_objects": len(analytics.unique_ids),
        "people": 0,
        "line_crossings": analytics.total_crossings,
    }


@app.post("/api/detect")
async def detect_image(file: UploadFile = File(...)):
    payload = await file.read()
    array = np.frombuffer(payload, dtype=np.uint8)
    frame = cv2.imdecode(array, cv2.IMREAD_COLOR)
    if frame is None:
        return {"error": "Invalid image"}

    start = time.perf_counter()
    detections = detect(frame, MODEL_NAME)
    boxes = [d["box"] for d in detections]
    ids = tracker.update(boxes)
    for d, tid in zip(detections, ids):
        d["track_id"] = tid

    labels = [d["label"] for d in detections]
    snapshot = analytics.update(ids, labels)
    snapshot["latency_ms"] = round((time.perf_counter() - start) * 1000, 2)
    snapshot["fps"] = round(1000 / max(snapshot["latency_ms"], 1), 2)

    annotated = annotate(frame, detections)
    ok, encoded = cv2.imencode(".jpg", annotated)
    return {
        "analytics": snapshot,
        "detections": detections,
        "image_base64": encoded.tobytes().hex() if ok else None,
    }


@app.websocket("/ws/live")
async def websocket_live(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({
        "type": "ready",
        "message": "VISIONX live channel ready. Send base64 JPEG frames."
    })
    try:
        while True:
            message = await websocket.receive_json()
            raw = message.get("frame")
            if not raw:
                continue
            import base64
            data = base64.b64decode(raw)
            frame = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
            if frame is None:
                await websocket.send_json({"type": "error", "message": "Invalid frame"})
                continue
            start = time.perf_counter()
            detections = detect(frame, MODEL_NAME)
            ids = tracker.update([d["box"] for d in detections])
            for d, tid in zip(detections, ids):
                d["track_id"] = tid
            labels = [d["label"] for d in detections]
            snapshot = analytics.update(ids, labels)
            snapshot["latency_ms"] = round((time.perf_counter() - start) * 1000, 2)
            snapshot["fps"] = round(1000 / max(snapshot["latency_ms"], 1), 2)
            await websocket.send_json({"type": "result", "analytics": snapshot, "detections": detections})
    except Exception:
        await websocket.close()
