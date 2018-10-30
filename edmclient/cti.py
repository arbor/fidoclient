from .rest_methods import Rest


class Insights(Rest):
    """
    All operations for /cti/insights
    """
    base_url = '/cti/insights'

    def show(self, **kwargs):
        """
        Keyword Arguments
        -----------------
        indicatorValue: string (required) Example: 1.2.3.4
                        The domain, IP address, or HTTP URI for which to
                        receive intelligence.

        Returns
        -------
        Dictionary

        Examples
        --------
        >>> from edm_sdk.edm import EdgeDefenseManager
        >>> dev = EdgeDefenseManager('fido_1.example.com', 'wxY8fM3')
        >>> dev.cti.insights.show(indicatorValue='1.2.3.4')
        """
        return self._get(**kwargs)


class Cti(object):
    """
    All operations for CTI insights
    """
    def __init__(self, *args, **kwargs):
        self.insights = Insights(*args, **kwargs)
