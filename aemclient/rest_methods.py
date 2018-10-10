#
# Common HTTP methods
#

import requests
import json

PREFIX = '/api/'
HTTPS = 'https://'


class Rest(object):
    """
    Class with methods to make the api calls
    """
    def __init__(self, host, apitoken, api_version):
        self.host = host
        self.apitoken = apitoken
        self.apiversion = api_version
        self._get_headers = {
                    'Authorization': 'NSAPITOKENID {}'.format(self.apitoken),
                    }
        self._post_headers = {
                    'Authorization': 'NSAPITOKENID {}'.format(self.apitoken),
                    'Content-Type': 'application/json'
                    }

    @staticmethod
    def _format_response(response):
        """
        Return a dict containing body,
        status code and headers of the response
        """
        formated = {
                    'body': json.loads(response.content) if response.content
                    else {},
                    'status_code': response.status_code,
                    'headers': response.headers
                   }
        return formated

    def _post(self, **kwargs):
        """
        REST POST method
        """
        url = HTTPS + self.host + PREFIX + self.apiversion \
            + self.base_url
        data = json.dumps(kwargs)
        response = requests.post(url, data=data, headers=self._post_headers,
                                 verify=False)
        return self._format_response(response)

    def _get(self, **kwargs):
        """
        REST GET method
        """
        item = '/' + str(kwargs.pop('item')) if 'item' in kwargs and \
               kwargs['item'] else ''
        url = HTTPS + self.host + PREFIX + self.apiversion \
            + self.base_url + item
        response = requests.get(url, headers=self._get_headers,
                                params=kwargs, verify=False)
        return self._format_response(response)

    def _delete(self, item=None):
        """
        REST DELETE method
        """
        item = '/' + str(item) if item else ''
        url = HTTPS + self.host + PREFIX + self.apiversion \
            + self.base_url + item
        response = requests.delete(url, headers=self._get_headers,
                                   verify=False)
        return self._format_response(response)

    def _patch(self, item=None, **kwargs):
        """
        REST PATCH method
        """
        item = '/' + str(item) if item else ''
        url = HTTPS + self.host + PREFIX + self.apiversion \
            + self.base_url + item
        data = json.dumps(kwargs)
        response = requests.patch(url, data=data, headers=self._post_headers,
                                  verify=False)
        return self._format_response(response)

    def _put(self, item=None, **kwargs):
        """
        REST PUT method
        """
        item = '/' + str(item) if item else ''
        url = HTTPS + self.host + PREFIX + self.apiversion \
            + self.base_url + item
        data = json.dumps(kwargs)
        response = requests.put(url, data=data, headers=self._post_headers,
                                verify=False)
        return self._format_response(response)
