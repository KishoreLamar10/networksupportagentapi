import pytest
from fastapi.testclient import TestClient
from app.api.server import app


client = TestClient(app)


def test_health_check():
    """Test the health check endpoint returns 200 and status ok."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "model" in data


def test_home_page():
    """Test the home page returns HTML."""
    response = client.get("/")
    assert response.status_code == 200
    assert "NetSupport AI API" in response.text


def test_support_missing_query():
    """Test /support rejects a request with no query field."""
    response = client.post("/support", json={})
    assert response.status_code == 422  # Validation error


def test_support_empty_query():
    """Test /support with an empty query string."""
    response = client.post("/support", json={"query": ""})
    # Should still return 200 — the agent handles empty queries gracefully
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "sources" in data


def test_support_with_history():
    """Test /support accepts conversation history."""
    response = client.post("/support", json={
        "query": "what about error E202?",
        "history": [
            {"role": "user", "content": "What are common router errors?"},
            {"role": "assistant", "content": "Common errors include E101 (DNS failure) and E202 (DHCP timeout)."},
        ]
    })
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data


def test_stream_endpoint():
    """Test the streaming endpoint returns SSE events."""
    response = client.post(
        "/support/stream",
        json={"query": "how to reset my router"},
    )
    assert response.status_code == 200
    assert "text/event-stream" in response.headers.get("content-type", "")
    # Check that we got at least one data event
    body = response.text
    assert "data:" in body
