import uuid
from secrets import token_urlsafe

import pytest  # noqa: F401
from fastapi.testclient import TestClient

from app import __version__, app

client = TestClient(app)


def test_version():
    assert __version__ == "0.1.0"


def test_get_paste_success():
    response = client.get("/id/NAEMN-E")
    assert response.status_code == 200
    assert (
        response.text
        == '{"identifier":"NAEMN-E","title":"test paste","text":"TEST TEST","date":"Dec 28, 2021 @ 11:31 PM"}'  # noqa: E501
    )


def test_get_paste_fail():
    response = client.get("/id/ABCDE")
    assert response.status_code == 404


def test_receive_paste_success():
    data = {"title": token_urlsafe(7), "text": str(uuid.uuid4())}
    response = client.post("/paste/", json=data)
    assert response.status_code == 200


def test_bad_path():
    response = client.get("/bad_path/")
    assert response.status_code == 404
