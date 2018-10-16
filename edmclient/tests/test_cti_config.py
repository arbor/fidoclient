import json
import logging
import unittest
from unittest.mock import patch
from edmclient.edm import EdgeDefenseManager as Fido

LOG = logging.getLogger('TestCti')

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
    response = {'message': '',
                'data': {
                    'cti_token': 'secret-cti-token',
                    'passivetotal_token': 'secret-passivetotal-token',
                    'passivetotal_user': 'you@my-company.com',
                    'shodan_token': 'secret-shodan-token'
                    }
                }
    return MockResponse(json.dumps(response), 200, HEADERS)


def mocked_requests_post(*args, **kwargs):
    """
    Use mock POST response
    """
    response = {'message': 'Success!',
                'data': {}}
    return MockResponse(json.dumps(response), 200, HEADERS)


class TestConfiguration(unittest.TestCase):

    def setUp(self):
        self.fido = Fido(FIDO, FIDO_TOKEN, api_version='v1')

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_get_config(self, mock_get):
        """
        Get CTI configuration
        """
        response = self.fido.configuration.cti.show()
        self.assertEqual(response['status_code'], 200)
        for _key in ['cti_token', 'passivetotal_token',
                     'passivetotal_user', 'shodan_token']:
            self.assertIn(_key, response['body']['data'])

    @patch('requests.post', side_effect=mocked_requests_post)
    def test_update_cti_config(self, mock_post):
        """
        Update CTI configuration
        """
        response = self.fido.devices.add(
                                cti_token='secret-cti-token',
                                passivetotal_token='secret-passivetotal-token',
                                passivetotal_user='you@my-company.com',
                                shodan_token='secret-shodan-token')
        self.assertEqual(response['status_code'], 200)
        self.assertEqual(response['body']['message'], 'Success!')


if __name__ == '__main__':
    unittest.main()
