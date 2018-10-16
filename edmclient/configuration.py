from .rest_methods import Rest


class Cti(Rest):
    """
    All operations for /cti/insights
    """
    base_url = '/configuration/cti'

    def show(self):
        """
        Returns
        -------
        Dictionary

        Examples
        --------
        >>> from aem_sdk.aem import ArborEnterpriseManager
        >>> dev = ArborEnterpriseManager('defone_1.example.com', 'wxY8fM3')
        >>> dev.configuration.cti.show()
        """
        return self._get()

    def update(self, **kwargs):
        """
        Add or update CTI configuration

        Keyword Arguments
        -----------------
        cti_token: Secret cti token
        passivetotal_token: Secret Passivetotal token
        passivetotal_user: Passivetotal username
        shodan_token: Secret Shodan token

        Returns
        -------
        Dictionary

        Examples
        --------
        >>> from aem_sdk.aem import ArborEnterpriseManager
        >>> dev = ArborEnterpriseManager('defone_1.example.com', 'wxY8fM3')
        >>> dev.configuration.cti.update(cti_token='ajfdgFJGFGmh27hnbv')
        """
        return self._post(**kwargs)


class Configuration(object):
    """
    All operations for CTI configuration
    """
    def __init__(self, *args, **kwargs):
        self.cti = Cti(*args, **kwargs)
