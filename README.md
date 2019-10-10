# ble-beacon-scanner

This is a docker image running BeaconScanner from beacontools to detect and report Bluetooth Beacons. It is designed to run in a Raspberry PI, but can be compiled to run in other systems supported by pibluez.

# To run

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
    },
    ...
  ]
}
```
## Future features

I'm considering adding support for detecting beacons based on MAC address. This would be useful to also detect Tile bluetooth beacons (which do not use the iBeacon protocol).
