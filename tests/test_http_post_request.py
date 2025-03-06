import pytest
import requests
from src.http_post_request import send_http_post_request

class MockResponse:
    def __init__(self, status_code=200, json_data=None, headers=None):
        self.status_code = status_code
        self._json_data = json_data or {}
        self._headers = headers or {}
        self.text = str(json_data) if json_data else ''

    def json(self):
        return self._json_data

    @property
    def headers(self):
        return self._headers

    def raise_for_status(self):
        if 400 <= self.status_code < 600:
            raise requests.HTTPError(f"HTTP Error {self.status_code}")

# Monkeypatch requests.post for controlled testing
def test_send_http_post_request_success(monkeypatch):
    def mock_post(*args, **kwargs):
        return MockResponse(status_code=200, json_data={'message': 'success'})

    monkeypatch.setattr(requests, 'post', mock_post)

    result = send_http_post_request('https://example.com', data={'key': 'value'})
    
    assert result['status_code'] == 200
    assert result['data'] == {'message': 'success'}

def test_send_http_post_request_empty_url():
    with pytest.raises(ValueError, match="URL cannot be empty"):
        send_http_post_request('')

def test_send_http_post_request_network_error(monkeypatch):
    def mock_post(*args, **kwargs):
        raise requests.ConnectionError("Network error")

    monkeypatch.setattr(requests, 'post', mock_post)

    with pytest.raises(RuntimeError, match="HTTP POST request failed"):
        send_http_post_request('https://example.com')

def test_send_http_post_request_http_error(monkeypatch):
    def mock_post(*args, **kwargs):
        return MockResponse(status_code=404, json_data={'error': 'Not Found'})

    monkeypatch.setattr(requests, 'post', mock_post)

    with pytest.raises(requests.HTTPError):
        send_http_post_request('https://example.com')

def test_send_http_post_request_custom_headers(monkeypatch):
    captured_headers = {}
    def mock_post(*args, **kwargs):
        nonlocal captured_headers
        captured_headers = kwargs.get('headers', {})
        return MockResponse(status_code=200)

    monkeypatch.setattr(requests, 'post', mock_post)

    send_http_post_request(
        'https://example.com', 
        headers={'Authorization': 'Bearer token'}
    )

    assert captured_headers['Content-Type'] == 'application/json'
    assert captured_headers['Authorization'] == 'Bearer token'