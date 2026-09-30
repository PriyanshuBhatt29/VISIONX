from dataclasses import dataclass


@dataclass
class AnalyticsEngine:
    total_crossings: int = 0
    unique_ids: set[int] | None = None

    def __post_init__(self):
        if self.unique_ids is None:
            self.unique_ids = set()

    def update(self, track_ids: list[int], labels: list[str], line_y: int | None = None,
               previous_centers: dict[int, tuple[int, int]] | None = None,
               current_centers: dict[int, tuple[int, int]] | None = None) -> dict:
        self.unique_ids.update(track_ids)
        crossings = 0

        if line_y is not None and previous_centers and current_centers:
            for tid in track_ids:
                before = previous_centers.get(tid)
                after = current_centers.get(tid)
                if before and after and (before[1] < line_y <= after[1]):
                    crossings += 1

        self.total_crossings += crossings
        return {
            "active_objects": len(track_ids),
            "unique_objects": len(self.unique_ids),
            "people": sum(label.lower() == "person" for label in labels),
            "line_crossings": self.total_crossings,
        }
