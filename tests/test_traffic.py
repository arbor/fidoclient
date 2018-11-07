import json
import logging
import unittest
from unittest.mock import patch
from edmclient.edm import EdgeDefenseManager as Fido

LOG = logging.getLogger('TestTraffic')

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


def mocked_requests_get(*args, **kwargs):
    """
    Use mock GET response
    """
    response = {'data': 'Sample data'}
    return MockResponse(json.dumps(response), 200, HEADERS)


class TestTraffic(unittest.TestCase):

    def setUp(self):
        self.fido = Fido(FIDO, FIDO_TOKEN, api_version='v1')

    @patch('requests.Session.send', side_effect=mocked_requests_get)
    def test_get_traffic(self, mock_get):
        """
        Get edge traffic
        """
        response = self.fido.traffic.edge.show()
        self.assertEqual(response['status_code'], 200)


if __name__ == '__main__':
    unittest.main()
