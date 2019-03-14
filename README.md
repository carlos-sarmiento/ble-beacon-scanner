# ble-beacon-scanner

`docker run --rm -it -v "$pwd/config.json:/config/config.json:ro" --cap-add=NET_RAW --cap-add=NET_ADMIN --net=host ble-beacon-scanner`

## config.json

```json
{
  "minTime": 30,
  "reportUrl": "http://someurl.com",
  "beacons": [
    {
      "label": "someLabel",
      "name": "Some Name",
      "uuid": "iBeacon UUID"
    }
  ]
}
```
