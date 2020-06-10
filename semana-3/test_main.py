from main import get_temperature
import requests


class MockResponse:

    @staticmethod
    def json():
        return {"currently": {"temperature": 62}}


def test_get_temperature_by_lat_lng(monkeypatch):

    expected_result = 16

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    result = get_temperature(-14.235004, -51.92528)
    assert result == expected_result


def test_get_temperature_no_lat_lng(monkeypatch):

    def mock_json(*args, **kwargs):
        return {"currently": {"temperature": None}}

    monkeypatch.setattr(requests.Response, "json", mock_json)

    result = get_temperature(None, None)
    assert result is None
