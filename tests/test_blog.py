from fileinput import filename
from fastapi import status, HTTPException  
import platform
import pdb
from pathlib import Path
from ocr.main import app
from fastapi.testclient import TestClient
import pytest


@pytest.fixture()
def os_type():
    return platform.system() 

def test_ocr_response_code(os_type):
    client = TestClient(app)
    testfile = Path(__file__).parent.parent.joinpath('testdata').joinpath('image_with_txt.png')
    files = {"image" : testfile.open("rb")}
    response =  client.post("/ocr", files=files)
    assert response.status_code == status.HTTP_200_OK