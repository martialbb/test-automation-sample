import json
import requests

def test_complete_payment():
    url = 'https://connect.squareupsandbox.com/v2/payments/5cESkkxpc3xBZMYATwqY75JXiJTZY/complete'
    # TODO: For this demo the ACCESS TOKEN will be in the code. In the real world this is usually retrieve
    # via an environment variable or a secret manager (vault, AWS Secret Manager etc..)
    headers = {
        "square-version": "2021-11-17",
        "authorization": "Bearer EAAAEG9GSiqZgHjnisKdLr_n2hfaADvhWUR5ybYTdFxIcDpUO97w4uF4QGwtMxRk",
        "content-type": "application/json",
    }
    response = requests.request("POST", url, headers=headers)
    response_body = json.loads(response.text)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert response_body['payment']['status'] == 'COMPLETED'

def test_complete_invalid_payment():
    pass