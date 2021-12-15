# The following are assertion methods for the payment API
import json


def assert_payment_reponse(response):
    # Fail the test if the response object is null
    assert response is not None
    assert response.status_code == 200
    assert response.reason == 'OK'


def assert_payment_body(response, payload):
    # Fail the test if the response object is null
    assert response is not None
    response_body = json.loads(response.text)
    assert response_body['payment']['status'] == 'COMPLETED'
    assert response_body['payment']['approved_money']['amount'] == payload['amount_money']['amount']
    assert response_body['payment']['total_money']['amount'] == payload['amount_money']['amount']


def assert_payment_body_notnull(response):
    # Fail the test if the response object is null
    assert response is not None
    response_body = json.loads(response.text)
    assert response_body['payment'] is not None


def assert_payments(response):
    # Fail the test if the response object is null
    assert response is not None
    # TODO: Validate payments list
