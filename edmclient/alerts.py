from .rest_methods import Rest


class Threats(Rest):
    """
    """
    base_url = '/alerts/threats'

    def show(self, **kwargs):
        """
        Keyword Arguments
        -----------------
        size: number (optional) Default: 100 Example: 1000
              The maximum number of matches to return.

        skip: number (optional) Example: 0
              The number of records to skip before returning results.
              You can use this parameter to paginate the results.

        descriptions: boolean (optional) Default: true Example: true
                      Indicates whether the response should include
                      threatDescriptions.

        sort: string (optional) Default: -time
              Example: -time,pkt.src,-pkt.dport
              A comma-separated list of field names for sorting the query
              results. The fields are sorted from left to right. Prefix a
              field name with - to sort that field's values in descending
              order, otherwise the field values are sorted in ascending
              order.

        start: string or number (optional) Default: 24 hours ago
               Example: 2018-08-08T00:00:00Z
               The start of the query time period. ISO 8601 format or epoch
               seconds is required.

        end: string or number (optional) Default: now
             Example: 2018-08-09T00:00:00Z
             The end of the query time period. ISO 8601 format or
             epoch seconds is required.

        q: string (optional)
           Example: pkt.proto:tcp and -pkt.appStr:http
           A Lucene-syntax query string. If this string is provided,
           then the dynamic parameters are ignored and only the
           Lucene query is used to filter the results.

        aggregate: string (optional) Example: reason
                   Generates an aggregation for the specified field
                   within the requested time period. This feature requires
                   that the agg_type parameter is included.

        agg_type: string (optional) Example: groupby
                  The aggregation method to use if the aggregate
                  parameter is included.

                  - groupby: generates an aggregated count for all members
                             of the specified field within the requested
                             time period. The results appear in data.bins.

                  - timeline: generates a timeseries that breaks down counts
                              for the specified field within the requested
                              time period. The results appear in
                              data.timeline.

                  Choices: groupby timeline

        Returns
        -------
        Dictionary

        Examples
        --------
        >>> from edm_sdk.edm import EdgeDefenseManager
        >>> dev = EdgeDefenseManager('fido_1.example.com', 'wxY8fM3')
        >>> dev.alerts.threats.show(start='2018-09-08T00:00:00Z')
        """
        return self._get(**kwargs)


class Counts(Rest):
    """
    All operations for /alerts/ddos/counts
    """
    base_url = '/alerts/ddos/counts'

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
        >>> dev.alerts.ddos.counts.show(start='2018-09-08T00:00:00Z')
        """
        return self._get(**kwargs)


class Ddos(Rest):
    """
    All operations for /alerts/ddos
    """
    base_url = '/alerts/ddos'

    def __init__(self, *args, **kwargs):
        super(Ddos, self).__init__(*args, **kwargs)
        self.counts = Counts(*args, **kwargs)

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

        page: number (optional) Example: 0
              The page number to start with when returning results.

        pageSize: number (optional) Example: 25
                  The number of alerts to include per page of results.

        Returns
        -------
        Dictionary

        Examples
        --------
        >>> from edm_sdk.edm import EdgeDefenseManager
        >>> dev = EdgeDefenseManager('fido_1.example.com', 'wxY8fM3')
        >>> dev.alerts.ddos.show(start='2018-09-08T00:00:00Z')
        """
        return self._get(**kwargs)


class Alerts(object):
    """
    All operations for alerts
    """
    def __init__(self, *args, **kwargs):
        self.threats = Threats(*args, **kwargs)
        self.ddos = Ddos(*args, **kwargs)
