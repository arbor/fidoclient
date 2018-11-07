[![pipeline status](https://git.arbor.net/df1/api-client/badges/master/pipeline.svg)](https://git.arbor.net/df1/api-client/commits/master)

[![coverage report](https://git.arbor.net/df1/api-client/badges/master/coverage.svg)](https://git.arbor.net/df1/api-client/commits/master)

# Edge Defense Manager Client v0.9

This is a simple client to use Edge Defense Manager's public facing API.

## Requirements
* Python (tested on Python 2.7 and Python 3.6.5)
* Requests

## Installation:
```bash
sudo pip install git+ssh://git@git.arbor.net/df1/api-client.git
```

**Note:** You must have your public key on git.arbor.net

## Using the Client:

Import the package:

```python
from edmclient.edm import EdgeDefenseManager
dev = EdgeDefenseManager(<host>, <apitoken>, api_version=<api_version, eg. 'v1'>)
```

### Devices

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

Update device:

```python
dev.devices.update(id=1,
                   host='aed_1.example.com',
                   apiToken='WWPi7_',
                   name='AED_1')
```

Partial update device:

```python
dev.devices.update(id=1, name='NEW_AED_1')
dev.devices.update(id=1, apiToken='sdf79_kjI')
```

### Alerts

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

### Traffic

View traffic:

```python
dev.traffic.edge.show(start='2018-09-08T00:00:00Z')
```

### Contextual Threat Intelligence (CTI)

View CTI data:

```python
dev.cti.insights.show(indicatorValue='1.2.3.4')
```

### CTI Configuration

View CTI configuration:

```python
dev.configuration.cti.show()
```

Add or Update CTI configuration:

```python
dev.configuration.cti.update(cti_token='ajfdgFJGFGmh27hnbv')
```

## Running unit tests

Make sure you have `nose` installed:

```bash
pip3 install nose
```

Then from the package directory run:

```bash
nosetests
```