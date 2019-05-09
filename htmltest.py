#Test script that reads the html page of the borderrouter, takes the
#IPv6 addresses under routing links and stores them in a list

from urllib.request  import urlopen

link = "http://[fd00::212:4b00:aff:4b01]/"
f = urlopen(link)
foil = f.readlines()
posistion = 0
addresses = []

length = len(foil)

for i in range(length):
    print(foil[i].decode('utf-8'))
    if "Routing links" == foil[i].decode('utf-8').strip():
        posistion = i
        break
        


for i in range(posistion+2, length-3):
    line = foil[i].decode('utf-8')
    beginPos = line.find(">") + 1
    endPos = line.find(" ", beginPos)
    address = line[beginPos:endPos]
    addresses.append(address)

print(addresses)



