from .devices import Devices
from .alerts import Alerts
from .traffic import Traffic
from .cti import Cti
from .configuration import Configuration


class EdgeDefenseManager(object):
    """
    Define the fido device
    """

    def __init__(self, *args, **kwargs):
        """
        Positional Arguments:
            host: Hostname or FQDN of the device
            apitoken: API token

        Keyword Arguments:
            api_version: API version (Default: v1)
            raise_on_error: Raise exception on failed Rest calls
                            (Default: False)
        """
        if not args or len(args) < 2:
            raise AttributeError('Missing required positional arguments '
                                 '`host` and/or `apitoken`')
        if not kwargs or 'api_version' not in kwargs.keys():
            raise AttributeError('Missing required keyword argument '
                                 '`api_version`')
        self.host = args[0]
        self.apitoken = args[1]
        self.apiversion = kwargs['api_version']
        self.raise_on_error = kwargs.get('raise_on_error', False)
        self.devices = Devices(*args, **kwargs)
        self.alerts = Alerts(*args, **kwargs)
        self.traffic = Traffic(*args, **kwargs)
        self.cti = Cti(*args, **kwargs)
        self.configuration = Configuration(*args, **kwargs)
