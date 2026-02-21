import asyncio

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello!"}


def test_ws():
    with client.websocket_connect("/ws") as ws:
        ws.send_text("hello")
        response == ws.receive_text()
        assert response == "Echo: hello"
