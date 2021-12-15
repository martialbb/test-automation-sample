import json
import requests

import assertion_utils


def test_create_payment_happy_path():
    url = "https://connect.squareupsandbox.com/v2/payments"

    payload = {
        'source_id': 'cnon:card-nonce-ok',
        'idempotency_key': 'f9fd57e6-bb8e-4b1a-b9fc-3d28db129bff',
        'amount_money': {
            'amount': 150,
            'currency': 'USD'
        }
    }
    #TODO: For this demo the ACCESS TOKEN will be in the code. In the real world this is usually retrieve
    # via an environment variable or a secret manager (vault, AWS Secret Manager etc..)
    headers = {
        "square-version": "2021-11-17",
        "authorization": "Bearer EAAAEG9GSiqZgHjnisKdLr_n2hfaADvhWUR5ybYTdFxIcDpUO97w4uF4QGwtMxRk",
        "content-type": "application/json",
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    # More assertions will be needed here to validate the create payment response
    #  Typically there should be an assertion function for data validation
    #  containing several low level assertions when creating the test framework
    assertion_utils.assert_payment_reponse(response)
    assertion_utils.assert_payment_body(response,payload)

