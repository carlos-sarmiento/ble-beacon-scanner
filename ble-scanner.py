from threading import Event
import time
import json
import uuid
from beacontools import BeaconScanner, IBeaconFilter
import datetime
import requests

configuration = {}

with open('/config/config.json') as json_file:
    configuration = json.load(json_file)

beacons = configuration['beacons']

for conf in beacons:
    conf['uuid'] = uuid.UUID(conf['uuid'])
    conf["lastSeen"] = 0


def callback(bt_addr, rssi, packet, additional_info):
    try:
        ts = time.time()
        for record in beacons:
            if record == None or additional_info == None:
                continue

            if str(record['uuid']) != str(additional_info['uuid']):
                # print("%s != %s" % (record['uuid'], additional_info['uuid']))
                continue

            if ts - record["lastSeen"] < configuration['minTime']:
                continue

            payload = {'label': record['label'],
                       'name': record['name'], 'rssi': rssi}

            r = requests.post(configuration['reportUrl'], data=payload)
            record["lastSeen"] = ts
            print("[%s] <%s> Detected and Reported: '%s' {iBeacon: %s} - rssi: %s" %
                  (str(datetime.datetime.now()), str(r.status_code),
                   record['label'], str(additional_info['uuid']), str(rssi)))

    except Exception as e:
        print("Exiting due to callback exception" + str(e))
        exit.set()


exit = Event()


def main():
    try:
        print("Starting")

        scanner = BeaconScanner(callback)
        print("Scanning")

        scanner.start()

        while not exit.is_set():
            exit.wait(60)

        print("All done!")
        scanner.stop()
        # perform any cleanup here
    except:
        return


def quit(signo, _frame):
    print("Interrupted by %d, shutting down" % signo)
    exit.set()


if __name__ == '__main__':

    import signal
    for sig in ('TERM', 'HUP', 'INT'):
        signal.signal(getattr(signal, 'SIG' + sig), quit)

    main()
