import json
import logging
import unittest
from unittest.mock import patch
from aemclient.aem import ArborEnterpriseManager

LOG = logging.getLogger('TestCti')

AEM = 'test.aem.arbor.net'
AEM_TOKEN = 'xLxD89YS0ZJc9f7JAOTZf_wchzjLqIMMCFV8tFue'
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
    ip = kwargs['params']['indicatorValue']
    response = {'data': ip}
    return MockResponse(json.dumps(response), 200, HEADERS)


class TestCti(unittest.TestCase):

    def setUp(self):
        self.aem = ArborEnterpriseManager(AEM, AEM_TOKEN, api_version='v1')

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_get_cti(self, mock_get):
        """
        Get CTI data
        """
        ip = '1.2.3.4'
        response = self.aem.cti.insights.show(indicatorValue=ip)
        self.assertEqual(response['status_code'], 200)
        self.assertEqual(response['body']['data'], ip)


if __name__ == '__main__':
    unittest.main()
