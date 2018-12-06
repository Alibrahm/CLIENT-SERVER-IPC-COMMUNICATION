
#IBRAHIM ALI
#Assignment 1

from xmlrpc.server import SimpleXMLRPCServer

def adventService(adventure):
    commission = 0
    commission = 5.0/100 * adventure
    return commission

def comicService(comic):
    commission = 0
    commission = 5.0/100 * comic
    return commission

def scienceService(science):
    commission = 0
    commission = 5.0/100 * science
    return commission
    

server = SimpleXMLRPCServer(("192.168.137.216", 8000))
print("Listening on port 8000...")
server.register_function(adventService, "adventService")
server.register_function(comicService, "comicService")
server.register_function(scienceService, "scienceService")
server.serve_forever()
