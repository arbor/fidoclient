#
# Common HTTP methods
#

import requests
import json
from .exceptions import EdmApiClientError, EdmApiServerError

PREFIX = '/api/'
HTTPS = 'https://'
ERR_STR = 'EDM API Call failed with status {status_code}: {body}'


class Rest(object):
    """
    Class with methods to make the api calls
    """
    def __init__(self, host, apitoken, api_version, raise_on_error=False):
        self.host = host
        self.apitoken = apitoken
        self.apiversion = api_version
        self.raise_on_error = raise_on_error
        self._headers = {
                    'Authorization': 'NSAPITOKENID {}'.format(self.apitoken),
                    }

    @staticmethod
    def _format_response(response):
        """
        Return a dict containing body,
        status code and headers of the response
        """
        # If content is not json then it is
        # probably an error. So return
        try:
            # Decoding from UTF-8 is necessary for Python versions below 3.6
            # https://docs.python.org/3/whatsnew/3.6.html#json
            body = json.loads(response.content if type(response.content) == str
                              else response.content.decode('utf-8'))
        except ValueError:
            body = {'error': response.reason}
        formated = {
                    'body': body,
                    'status_code': response.status_code,
                    'headers': response.headers
                   }
        return formated

    @staticmethod
    def _raise_on_error(response):
        """
        Raise an exception if the response contains an unsuccessful status code
        """
        if 400 <= response['status_code'] < 500:
            raise EdmApiClientError(ERR_STR.format(
                status_code=response['status_code'],
                body=response['body']))
        elif 500 <= response['status_code'] < 600:
            raise EdmApiServerError(ERR_STR.format(
                status_code=response['status_code'],
                body=response['body']))

    def _make_request(self, rest_method, item=None, **kwargs):
        """
        Make requests
        """
        s = requests.Session()
        url = HTTPS + self.host + PREFIX + self.apiversion \
            + self.base_url
        url = url + (item if item else '')
        req = requests.Request(rest_method,
                               url,
                               headers=self._headers,
                               **kwargs)
        prepped = s.prepare_request(req)
        if rest_method in ['POST', 'PUT', 'PATCH']:
            prepped.headers['Content-Type'] = 'application/json'
        response = self._format_response(s.send(prepped, verify=False))
        if self.raise_on_error:
            self._raise_on_error(response)
        return response

    def _post(self, **kwargs):
        """
        REST POST method
        """
        return self._make_request('POST', data=json.dumps(kwargs))

    def _get(self, **kwargs):
        """
        REST GET method
        """
        item = '/' + str(kwargs.pop('item')) if 'item' in kwargs and \
               kwargs['item'] else ''
        return self._make_request('GET', item=item, params=kwargs)

    def _delete(self, item=None):
        """
        REST DELETE method
        """
        item = '/' + str(item) if item else ''
        return self._make_request('DELETE', item=item)

    def _patch(self, item=None, **kwargs):
        """
        REST PATCH method
        """
        item = '/' + str(item) if item else ''
        return self._make_request('PATCH', item=item, data=json.dumps(kwargs))

    def _put(self, item=None, **kwargs):
        """
        REST PUT method
        """
        item = '/' + str(item) if item else ''
        return self._make_request('PATCH', item=item, data=json.dumps(kwargs))
