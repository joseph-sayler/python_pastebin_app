import pytest
import json
import uuid
from fastapi.testclient import TestClient
from secrets import token_urlsafe
from app import app, __version__


client = TestClient(app)


def test_version():
    assert __version__ == '0.1.0'


def test_get_paste_success():
    response = client.get("/id/NAEMN-E")
    assert response.status_code == 200
    assert response.text == '{"identifier":"NAEMN-E","title":"test paste","text":"TEST TEST","date":"Dec 28, 2021 @ 11:31 PM"}'


def test_get_paste_fail():
    response = client.get("/id/ABCDE")
    assert response.status_code == 404


def test_receive_past_success():
    data = {
        "title": token_urlsafe(7),
        "text": str(uuid.uuid4())
    }
    response = client.post("/paste/", json.dumps(data))
    assert response.status_code == 200


def test_bad_path():
    response = client.get("/bad_path/")
    assert response.status_code == 404
