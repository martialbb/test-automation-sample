import json
import requests

def test_list_payments():
    url = "https://connect.squareupsandbox.com/v2/payments"

#TODO: For this demo the ACCESS TOKEN will be in the code. In the real world this is usually retrieve
    # via an environment variable or a secret manager (vault, AWS Secret Manager etc..)
    headers = {
        "square-version": "2021-11-17",
        "authorization": "Bearer EAAAEG9GSiqZgHjnisKdLr_n2hfaADvhWUR5ybYTdFxIcDpUO97w4uF4QGwtMxRk",
        "content-type": "application/json",
    }
    response = requests.request("GET", url, headers=headers)
    response_body = json.loads(response.text)
    # More assertions will be needed here to validate the list payment response
    #  Typically there should be an assertion function for data validation
    #  containing several low level assertions when creating the test framework
    # TODO: Create an assertion function for reuse
    #  for test_create_payment() when refactoring.
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert response_body['payments'][0]['status'] == 'COMPLETED'
    assert response_body['payments'][0]['approved_money']['amount'] == 100
    assert response_body['payments'][0]['total_money']['amount'] == 100
