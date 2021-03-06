from coapthon.client.helperclient import HelperClient
import time
from datetime import datetime as dt


host = "fd00::212:4b00:c46:9280"        #IPv6 address of a node
port = 5683                             #
path ="sensors/light"                   #Name of resource, sensors/light or sensors/battery

client = HelperClient(server=(host, port))

while True:
    response = client.get(path)
    print(response.source[0])
    print(response.payload)
    with open("./9280.log", "a") as log:
        log.write("{}\t\t{}\t\t{}\n".format(response.source[0], dt.now().strftime("%Y-%m-%d %H:%M:%S"), response.payload))
    time.sleep(60)


client.stop()