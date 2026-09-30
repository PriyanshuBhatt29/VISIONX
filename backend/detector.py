from functools import lru_cache
import cv2
import numpy as np
from ultralytics import YOLO


@lru_cache(maxsize=1)
def get_model(model_name: str = "yolo11n.pt") -> YOLO:
    return YOLO(model_name)


def detect(frame: np.ndarray, model_name: str = "yolo11n.pt"):
    model = get_model(model_name)
    result = model.predict(frame, verbose=False)[0]

    detections = []
    if result.boxes is None:
        return detections

    names = result.names
    for box, confidence, class_id in zip(
        result.boxes.xyxy.cpu().numpy(),
        result.boxes.conf.cpu().numpy(),
        result.boxes.cls.cpu().numpy(),
    ):
        x1, y1, x2, y2 = map(int, box)
        cid = int(class_id)
        detections.append({
            "class_id": cid,
            "label": str(names[cid]),
            "confidence": float(confidence),
            "box": (x1, y1, x2, y2),
        })
    return detections


def annotate(frame: np.ndarray, detections: list[dict]) -> np.ndarray:
    canvas = frame.copy()
    for d in detections:
        x1, y1, x2, y2 = d["box"]
        cv2.rectangle(canvas, (x1, y1), (x2, y2), (30, 30, 255), 2)
        label = f'{d["label"]} {d["confidence"]:.0%}'
        cv2.putText(canvas, label, (x1, max(20, y1 - 8)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (30, 30, 255), 2)
    return canvas
