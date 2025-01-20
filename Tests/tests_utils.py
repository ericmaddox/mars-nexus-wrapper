import pytest
from unittest.mock import Mock
from Mars_Wrapper.utils import handle_api_response

def test_handle_api_response():
    # Mock a successful HTTP response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'status': 'ok', 'data': 'mars_data'}
    
    # Test success case
    result = handle_api_response(mock_response)
    assert result == {'status': 'ok', 'data': 'mars_data'}

    # Mock a failed HTTP response (404 error)
    mock_response.status_code = 404
    mock_response.json.return_value = {'error': 'Not found'}
    
    # Test failure case: Ensure the exception is raised correctly
    with pytest.raises(Exception, match="API request failed with status code 404"):
        handle_api_response(mock_response)
