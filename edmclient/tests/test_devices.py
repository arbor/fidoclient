import json
import logging
import unittest
from unittest.mock import patch
from edmclient.edm import EdgeDefenseManager as Fido

LOG = logging.getLogger('TestDevices')

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


def mocked_requests_post(*args, **kwargs):
    """
    Use mock POST response
    """
    response = {'apiToken': '********',
                'down': False,
                'host': 'bushing.tb.arbor.net',
                'id': 1,
                'name': 'BUSHING',
                'warnings': ['Failed to configure the device to send syslog \
                             messages to Arbor Enterprise Manager. Add Arbor \
                             Enterprise Manager as a syslog notification \
                             destination in the device UI.']}
    return MockResponse(json.dumps(response), 201, HEADERS)


def mocked_requests_get(*args, **kwargs):
    """
    Use mock GET response
    """
    response = {'data': [
                   {'apiToken': '********',
                    'down': False,
                    'host': 'bushing.tb.arbor.net',
                    'id': 1,
                    'name': 'BUSHING'}],
                'totalCount': 1}
    return MockResponse(json.dumps(response), 200, HEADERS)


def mocked_requests_delete(*args, **kwargs):
    """
    Use mock DELETE response
    """
    url = args[0]
    id = url.split('/')[-1]
    if id == '1':
        response = {}
        status_code = 204
    elif id == '2000':
        response = {'errors': {'Specified APS [2000] does not exist.':
                               'Specified APS [2000] does not exist.'}}
        status_code = 405
    else:
        response = {'message': 'The method is not allowed '
                               'for the requested URL.'}
        status_code = 405
    return MockResponse(json.dumps(response), status_code, HEADERS)


def mocked_requests_put(*args, **kwargs):
    """
    Use mock PATCH response
    """
    response = {'data': [
                   {'apiToken': '********',
                    'down': False,
                    'host': 'new_aed.arbor.net',
                    'id': 1,
                    'name': 'NEW AED'}],
                'totalCount': 1}
    return MockResponse(json.dumps(response), 200, HEADERS)


def mocked_requests_patch(*args, **kwargs):
    """
    Use mock PATCH response
    """
    response = {'data': [
                   {'apiToken': '********',
                    'down': False,
                    'host': 'new_aed.arbor.net',
                    'id': 1,
                    'name': 'NEW PATCHED AED'}],
                'totalCount': 1}
    return MockResponse(json.dumps(response), 200, HEADERS)


class TestDevices(unittest.TestCase):

    def setUp(self):
        self.fido = Fido(FIDO, FIDO_TOKEN, api_version='v1')

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_get_all_devices(self, mock_get):
        """
        Get all AEDs
        """
        response = self.fido.devices.show()
        self.assertEqual(response['status_code'], 200)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_get_one_devices(self, mock_get):
        """
        Get single AEDs
        """
        response = self.fido.devices.show(id=1)
        self.assertEqual(response['status_code'], 200)

    @patch('requests.post', side_effect=mocked_requests_post)
    def test_add_devices(self, mock_post):
        """
        Add AED
        """
        response = self.fido.devices.add(host='test.aed.arbor.net',
                                         apiToken='sample',
                                         name='TEST AED')
        self.assertEqual(response['status_code'], 201)

    @patch('requests.delete', side_effect=mocked_requests_delete)
    def test_delete_devices(self, mock_delete):
        """
        Delete AED
        """
        # No device specified
        response = self.fido.devices.remove()
        self.assertEqual(response['status_code'], 405)
        # Device ID specified
        response = self.fido.devices.remove(id=1)
        self.assertEqual(response['status_code'], 204)
        # Delete non-existent AED
        response = self.fido.devices.remove(id=2000)
        self.assertEqual(response['status_code'], 405)

    @patch('requests.put', side_effect=mocked_requests_put)
    def test_partial_update_devices(self, mock_patch):
        """
        Update single AEDs
        """
        response = self.fido.devices.update(host='new_aed.arbor.net',
                                            apiToken='new_token',
                                            name='NEW AED')
        self.assertEqual(response['status_code'], 200)

    @patch('requests.patch', side_effect=mocked_requests_patch)
    def test_update_devices(self, mock_patch):
        """
        Partial update single AEDs
        """
        response = self.fido.devices.partial_update(name='NEW PATCHED AED')
        self.assertEqual(response['status_code'], 200)


if __name__ == '__main__':
    unittest.main()
