# Arbor Enterprise Manager SDK

This is a simple SDK to use Arbor Edge Manager's public facing API.

## Installation:
```bash
sudo pip install git+ssh://git@git.arbor.net/df1/aem_sdk.git
```

**Note:** You must have your public key on git.arbor.net

## Using the SDK:

Import the package:

```python
from aem_sdk.aem import ArborEnterpriseManager
dev = ArborEnterpriseManager(<host>, <apitoken>, api_version=<api_version, eg. 'v1'>)
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
