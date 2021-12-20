from fastapi.testclient import TestClient
from facebook_scraper import *

import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from starlette.status import HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY


from service.app import app
import requests


client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"FACEBOOK": "SCRAPER"}

def test_invalid_get():
    response = client.get("/display_one_result?post_id=1")
    assert response.status_code == 404

def test_invalid_delete():
    response = client.get("/delete_one/?post_id=1")
    assert response.status_code == 405
    
def test_smoketest():
    list(get_posts(group=117507531664134, pages=2))


