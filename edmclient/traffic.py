from .rest_methods import Rest


class Edge(Rest):
    """
    All operations for /traffic/edge
    """
    base_url = '/traffic/edge'

    def show(self, **kwargs):
        """
        Keyword Arguments
        -----------------
        start: string (required) Example: 2018-08-08T00:00:00Z
               The start of the search time period, based on the alert
               timestamp. ISO 8601 format is required.

        end: string (optional) Example: 2018-08-09T00:00:00Z
             The end of the search time period, based on the alert
             timestamp. ISO 8601 format is required.

        Returns
        -------
        Dictionary

        Examples
        --------
        >>> from edm_sdk.edm import EdgeDefenseManager
        >>> dev = EdgeDefenseManager('fido_1.example.com', 'wxY8fM3')
        >>> dev.traffic.edge.show(start='2018-09-08T00:00:00Z')
        """
        return self._get(**kwargs)


class Traffic(object):
    """
    All operations for alerts
    """
    def __init__(self, *args, **kwargs):
        self.edge = Edge(*args, **kwargs)
