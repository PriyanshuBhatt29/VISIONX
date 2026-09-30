from backend.tracker import CentroidTracker


def test_tracker_assigns_stable_ids():
    tracker = CentroidTracker(max_distance=100)
    first = tracker.update([(0, 0, 20, 20)])
    second = tracker.update([(3, 2, 23, 22)])
    assert first == second
