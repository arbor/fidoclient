# Edge Defense Manager Client v0.9

This simple client allows you to use Edge Defense Manager's public API.

## Requirements
* Python (tested on Python 2.7 and Python 3.6.5)
* Requests

## Installation:
```bash
sudo pip install -e git://github.com/arbor/fidoclient.git@v0.9#egg=edmclient
```

## Generating an API Token From Edge Defense Manager

Access to the Edge Defense Manager API requires an API token for authentication. You generate the token in the EDM command line interface (CLI).

The API token is associated with the user account under which it is generated. Any user can generate an EDM API token, except for the root user.

To generate an EDM API token:

1. Establish an SSH connection to EDM.

2. Log in to the operating system CLI with your EDM credentials.

3. To create the token, enter **edm\_apitoken\_gen**
    
    The system responds with the new API token, for example:
    ```json
    { "admin": "LMttPZ45FXnJT6IokVh6Px-otiKGDMkUdyQmJMWmWGz" }
    ```

4. For later use, copy the token and then paste it to a text file.

5. To log out of the CLI, enter **exit**

To View or delete a token, use one of the following commands.

* edm\_apitoken\_show

* edm\_apitoken\_delete

## Using the Client

Import the package:

```python
from edmclient.edm import EdgeDefenseManager
dev = EdgeDefenseManager(<host>, <apitoken>, api_version=<api_version, eg. 'v1'>)
```

### Managing Devices

Add a device:

```python
dev.devices.add(host='aed_1.example.com',
                apiToken='WWPi7_',
                name='AED_1')
```

View devices:

```python
dev.devices.show()
dev.devices.show(id=1)
```

Remove devices:

```python
dev.devices.remove(id=1)
```

Update a device:

```python
dev.devices.update(id=1,
                   host='aed_1.example.com',
                   apiToken='WWPi7_',
                   name='AED_1')
```

Partially update a device:

```python
dev.devices.update(id=1, name='NEW_AED_1')
dev.devices.update(id=1, apiToken='sdf79_kjI')
```

### Viewing Alerts

View threats:

```python
dev.alerts.threats.show(start='2018-09-08T00:00:00Z')
```

View DDoS alerts:

```python
dev.alerts.ddos.show(start='2018-09-08T00:00:00Z')
```

View DDoS counts:

```python
dev.alerts.ddos.count.show(start='2018-09-08T00:00:00Z')
```

### Viewing Traffic

View traffic:

```python
dev.traffic.edge.show(start='2018-09-08T00:00:00Z')
```

### Viewing Contextual Threat Intelligence (CTI)

View CTI data:

```python
dev.cti.insights.show(indicatorValue='1.2.3.4')
```

### Configuring CTI

View the CTI configuration:

```python
dev.configuration.cti.show()
```

Add or Update the CTI configuration:

```python
dev.configuration.cti.update(cti_token='ajfdgFJGFGmh27hnbv')
```

## Running Unit Tests

If `nose` is not installed, then run:

```bash
pip3 install nose
```

Run the following command from the package directory:

```bash
nosetests
```
