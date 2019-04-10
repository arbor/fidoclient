Edge Defense Manager Client
===========================

This simple client allows you to use Edge Defense Manager's public API.

Requirements
------------

-  Python (tested on Python 2.7 and Python 3.6.5)
-  Requests

Installation:
-------------

.. code:: bash

    sudo pip install edm-client

Source code is available on `GitHub
<https://github.com/arbor/fidoclient>`_.

Generating an API Token From Edge Defense Manager
-------------------------------------------------

Access to the Edge Defense Manager API requires an API token for authentication. You generate the token in the EDM command line interface (CLI).

The API token is associated with the user account under which it is generated. Any user can generate an EDM API token, except for the root user.

To generate an EDM API token:

#. Establish an SSH connection to EDM.

#. Log in to the operating system CLI with your EDM credentials.

#. To create the token, enter **edm\_apitoken\_gen**.

   The system responds with the new API token, for example:

   .. code:: json

    { "admin": "LMttPZ45FXnJT6IokVh6Px-otiKGDMkUdyQmJMWmWGz" }
    

#. For later use, copy the token and then paste it to a text file.

#. To log out of the CLI, enter **exit**

To View or delete a token, use one of the following commands.

* edm\_apitoken\_show

* edm\_apitoken\_delete

Using the Client
----------------

Import the package:

.. code:: python

    from edmclient.edm import EdgeDefenseManager
    dev = EdgeDefenseManager(<host>, <apitoken>, api_version=<api_version, eg. 'v1'>, raise_on_error=<True|False>)

Managing Devices
~~~~~~~~~~~~~~~~

Add a device:

.. code:: python

    dev.devices.add(host='aed_1.example.com',
                    apiToken='WWPi7_',
                    name='AED_1')

View devices:

.. code:: python

    dev.devices.show()
    dev.devices.show(id=1)

Remove devices:

.. code:: python

    dev.devices.remove(id=1)

Update a device:

.. code:: python

    dev.devices.update(id=1,
                       host='aed_1.example.com',
                       apiToken='WWPi7_',
                       name='AED_1')

Partially update a device:

.. code:: python

    dev.devices.update(id=1, name='NEW_AED_1')
    dev.devices.update(id=1, apiToken='sdf79_kjI')

Viewing Alerts
~~~~~~~~~~~~~~

View threats:

.. code:: python

    dev.alerts.threats.show(start='2018-09-08T00:00:00Z')

View DDoS alerts:

.. code:: python

    dev.alerts.ddos.show(start='2018-09-08T00:00:00Z')

View DDoS counts:

.. code:: python

    dev.alerts.ddos.count.show(start='2018-09-08T00:00:00Z')

Viewing Traffic
~~~~~~~~~~~~~~~

View traffic:

.. code:: python

    dev.traffic.edge.show(start='2018-09-08T00:00:00Z')

Viewing Contextual Threat Intelligence (CTI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

View CTI data:

.. code:: python

    dev.cti.insights.show(indicatorValue='1.2.3.4')

Configuring CTI
~~~~~~~~~~~~~~~

View the CTI configuration:

.. code:: python

    dev.configuration.cti.show()

Add or Update the CTI configuration:

.. code:: python

    dev.configuration.cti.update(cti_token='ajfdgFJGFGmh27hnbv')

Running Unit Tests
------------------

If ``nose`` is not installed, then run:

.. code:: bash

    pip3 install nose

Run the following command from the package directory:

.. code:: bash

    nosetests

