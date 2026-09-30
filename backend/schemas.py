from pydantic import BaseModel, Field


class Detection(BaseModel):
    track_id: int | None = None
    class_id: int
    label: str
    confidence: float = Field(ge=0.0, le=1.0)
    x1: int
    y1: int
    x2: int
    y2: int


class AnalyticsSnapshot(BaseModel):
    fps: float
    latency_ms: float
    active_objects: int
    unique_objects: int
    people: int
    line_crossings: int
