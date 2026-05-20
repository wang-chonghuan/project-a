from project_a import build_status


def test_build_status_is_ok():
    assert build_status()["status"] == "ok"
