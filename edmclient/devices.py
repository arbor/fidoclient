from .rest_methods import Rest


class Devices(Rest):
    """
    All operations for devices
    """
    base_url = '/devices'

    def add(self, **kwargs):
        """
        Add device

        Keyword Arguments
        -----------------
        host: Hostname of the AED
        apiToken: API token of the AED
        name: Optional. Name or alias for the AED

        Returns
        -------
        Dictionary

        Examples
        --------
        >>> from edm_sdk.edm import EdgeDefenseManager
        >>> dev = EdgeDefenseManager('fido_1.example.com', 'wxY8fM3')
        >>> dev.devices.add(host='aed_1.example.com',
                            apiToken='WWPi7_',
                            name='AED_1')
        """
        return self._post(**kwargs)

    def remove(self, id=None):
        """
        Remove device.

        Keyword Arguments
        -----------------
        id: ID of the device to remove

        Returns
        -------
        Dictionary

        Examples
        --------
        >>> from edm_sdk.edm import EdgeDefenseManager
        >>> dev = EdgeDefenseManager('fido_1.example.com', 'wxY8fM3')
        >>> dev.devices.remove(id=1)
        """
        return self._delete(item=id)

    def show(self, id=None, **kwargs):
        """
        Show a specific device or all devices.

        Keyword Arguments
        -----------------
        id: Optional. If not provided, show all devices.
            If supplied, show only that device.

        Returns
        -------
        Dictionary

        Examples
        --------
        >>> from edm_sdk.edm import EdgeDefenseManager
        >>> dev = EdgeDefenseManager('fido_1.example.com', 'wxY8fM3')
        >>> dev.devices.show()
        >>> dev.devices.show(id=1)
        """
        return self._get(item=id, **kwargs)

    def update(self, id=None, **kwargs):
        """
        Updated device

        Keyword Arguments
        -----------------
        host: Hostname of the AED
        apiToken: API token of the AED
        name: Optional. Name or alias for the AED

        Returns
        -------
        Dictionary

        Examples
        --------
        >>> from edm_sdk.edm import EdgeDefenseManager
        >>> dev = EdgeDefenseManager('fido_1.example.com', 'wxY8fM3')
        >>> dev.devices.update(id=1,
                               host='aed_1.example.com',
                               apiToken='WWPi7_',
                               name='AED_1')
        """
        return self._put(item=id, **kwargs)

    def partial_update(self, id=None, **kwargs):
        """
        Partial update device

        Keyword Arguments
        -----------------
        host: Optional. Hostname of the AED
        apiToken: Optional. API token of the AED
        name: Optional. Name or alias for the AED

        Returns
        -------
        Dictionary

        Examples
        --------

        >>> from edm_sdk.edm import EdgeDefenseManager
        >>> dev = EdgeDefenseManager('fido_1.example.com', 'wxY8fM3')
        >>> dev.devices.update(id=1,
                               name='NEW_AED_1')
        >>> dev.devices.update(id=1,
                               apiToken='sdf79_kjI')
        """
        return self._patch(item=id, **kwargs)
