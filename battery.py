from coapthon.client.helperclient import HelperClient
import time
from datetime import datetime as dt

host = "fd00::212:4b00:11a7:3206"
port = 5683
path ="sensors/battery"


client = HelperClient(server=(host, port))

while True:
    response = client.get(path)
    print(response.source[0])
    print(response.payload)
    with open("./3206battery.log", "a") as log:
        log.write("{}\t\t{}\t\t{}\n".format(response.source[0], dt.now().strftime("%Y-%m-%d %H:%M:%S"), response.payload))
    time.sleep(600)

client.stop()