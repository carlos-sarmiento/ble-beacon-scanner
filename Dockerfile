FROM arm32v5/python:3
RUN apt-get update -y 
RUN apt-get install -y bluetooth libbluetooth-dev python-dev libbluetooth-dev libcap2-bin 
RUN python3 -m pip install requests pybluez beacontools beacontools[scan]

ADD ble-scanner.py /

CMD [ "python", "./ble-scanner.py" ]
