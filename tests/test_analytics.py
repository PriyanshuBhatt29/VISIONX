from backend.analytics import AnalyticsEngine


def test_people_count_and_unique_objects():
    engine = AnalyticsEngine()
    result = engine.update([1, 2], ["person", "car"])
    assert result["people"] == 1
    assert result["unique_objects"] == 2
