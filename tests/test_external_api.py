from unittest.mock import Mock, patch

from src.external_api import convert


@patch("src.external_api.requests.get")
def test_convert(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"result": 7000.0}
    mock_get.return_value = mock_response
    operation = {"operationAmount": {"amount": "25780.71", "currency": {"name": "руб.", "code": "RUB"}}}

    operation_1 = {"operationAmount": {"amount": "25780.71", "currency": {"name": "USD", "code": "USD"}}}
    assert convert(operation) == 25780.71
    assert convert(operation_1) == 7000.0
