import pytest
import requests

ID_FILE = {}
URL = "http://localhost:8080/"




def _respons(method, url, headers=None, payload=None):
    return requests.request(method, url, headers=headers, data=payload)


def upload():
    url = URL + "upload"
    headers = {
        'Content-Type': 'application/text'
    }
    payload = b"{'test': 'ok'}"
    res = _respons("POST", url, headers, payload)
    ID_FILE = res.text
    print(res.status_code)
    return res.status_code


def test_upload():
    res = upload()
    print(ID_FILE)
    assert res == 200

def download():
    url = URL + "download/342342342341234124"
    res = _respons("GET", url).status_code
    return res



def check():
    url = URL + "check/342342342341234124"
    res = _respons("GET", url).status_code
    return res


def test_download():
    assert download() == 404

def test_check():
    assert check() == 404