from dataclasses import dataclass
from math import hypot


@dataclass
class Track:
    track_id: int
    centroid: tuple[int, int]
    missed: int = 0


class CentroidTracker:
    """Small dependency-free tracker for portfolio/demo workloads."""

    def __init__(self, max_distance: float = 80.0, max_missed: int = 12):
        self.max_distance = max_distance
        self.max_missed = max_missed
        self.next_id = 1
        self.tracks: dict[int, Track] = {}

    @staticmethod
    def centroid(box: tuple[int, int, int, int]) -> tuple[int, int]:
        x1, y1, x2, y2 = box
        return ((x1 + x2) // 2, (y1 + y2) // 2)

    def update(self, boxes: list[tuple[int, int, int, int]]) -> list[int]:
        if not boxes:
            for track in self.tracks.values():
                track.missed += 1
            self._prune()
            return []

        centers = [self.centroid(box) for box in boxes]
        assigned: dict[int, int] = {}
        used_tracks: set[int] = set()

        pairs = []
        for i, center in enumerate(centers):
            for tid, track in self.tracks.items():
                pairs.append((hypot(center[0] - track.centroid[0],
                                    center[1] - track.centroid[1]), i, tid))
        pairs.sort()

        for distance, i, tid in pairs:
            if i in assigned or tid in used_tracks or distance > self.max_distance:
                continue
            assigned[i] = tid
            used_tracks.add(tid)

        result = []
        for i, center in enumerate(centers):
            if i in assigned:
                tid = assigned[i]
                self.tracks[tid].centroid = center
                self.tracks[tid].missed = 0
            else:
                tid = self.next_id
                self.next_id += 1
                self.tracks[tid] = Track(tid, center)
            result.append(tid)

        for tid, track in self.tracks.items():
            if tid not in used_tracks and tid not in result:
                track.missed += 1

        self._prune()
        return result

    def _prune(self):
        dead = [tid for tid, t in self.tracks.items() if t.missed > self.max_missed]
        for tid in dead:
            del self.tracks[tid]
