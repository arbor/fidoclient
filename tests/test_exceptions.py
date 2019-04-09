import json
import logging
import unittest
from unittest.mock import patch
from edmclient.edm import EdgeDefenseManager as Fido
from edmclient.exceptions import EdmApiClientError, EdmApiServerError

LOG = logging.getLogger('TestExceptions')

FIDO = 'test.fido.arbor.net'
FIDO_TOKEN = 'xLxD89YS0ZJc9f7JAOTZf_wchzjLqIMMCFV8tFue'
HEADERS = {'Server': 'nginx/1.14.0',
           'Date': 'Fri, 05 Oct 2018 18:31:39 GMT',
           'Content-Type': 'application/json',
           'Connection': 'keep-alive'}


class MockResponse:
    def __init__(self, content, status_code, headers):
        self.content = content
        self.status_code = status_code
        self.headers = headers


def mocked_requests_server_error(*args, **kwargs):
    """
    Use mock GET response
    """
    response = {'errors': {'ProgrammingError': """relation "device" does not exist
LINE 9:           FROM device
                       ^
('
          SELECT
              id,
              name,
              host,
              apitoken,
              down,
              last_alert_sync
          FROM device
        WHERE id= %s ', ['1'])"""}
                }
    return MockResponse(json.dumps(response), 500, HEADERS)


def mocked_requests_client_error(*args, **kwargs):
    """
    Use mock GET response
    """
    response = {'errors': 'The method is not allowed for the requested URL'}
    return MockResponse(json.dumps(response), 405, HEADERS)


class TestExceptions(unittest.TestCase):

    def setUp(self):
        self.fido = Fido(FIDO, FIDO_TOKEN, api_version='v1',
                         raise_on_error=True)

    @patch('requests.Session.send', side_effect=mocked_requests_server_error)
    def test_server_error(self, mock_delete):
        """
        Server Error
        """
        self.assertRaises(EdmApiServerError, self.fido.configuration.cti.show)

    @patch('requests.Session.send', side_effect=mocked_requests_client_error)
    def test_client_error(self, mock_delete):
        """
        Client Error
        """
        self.assertRaises(EdmApiClientError, self.fido.configuration.cti.show)


if __name__ == '__main__':
    unittest.main()
