from coapthon.client.helperclient import HelperClient
import time

host = "fd00::212:4b00:c46:9280"
port = 5683
path ="sensors/light"


client = HelperClient(server=(host, port))

while True:
    response = client.get(path)
    print(response.source[0])
    print(response.payload)
    time.sleep(120)




#print(response.pretty_print())
client.stop()