import json
import requests


# This test verifies that a payment is retrieved when passing the payment id
import assertion_utils


def test_search_payment():
    url = 'https://connect.squareupsandbox.com/v2/payments/HlZKt3U2s6QhI9YuXLOSyUDDrKBZY'
    # TODO: For this demo the ACCESS TOKEN will be in the code. In the real world this is usually retrieve
    # via an environment variable or a secret manager (vault, AWS Secret Manager etc..)
    headers = {
        "square-version": "2021-11-17",
        "authorization": "Bearer EAAAEG9GSiqZgHjnisKdLr_n2hfaADvhWUR5ybYTdFxIcDpUO97w4uF4QGwtMxRk",
        "content-type": "application/json",
    }
    response = requests.request("GET", url, headers=headers)
    assertion_utils.assert_payment_reponse(response)
    assertion_utils.assert_payment_body_notnull(response)


def test_search_invalid_payment():
    pass
