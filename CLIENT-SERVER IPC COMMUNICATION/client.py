#IBRAHIM ALI

import xmlrpc.client
   #Use your LAN IP address 
with xmlrpc.client.ServerProxy("http://192.168.137.216:8000/") as proxy:
    print ("Remote Procedure Calls (RPC) used! ...\n")
    print ("Creators: \n")
    print ("IBRAHIM ALI \n")
    print ("Book Sales Client Server communication\n")
    print ("This is a system that lets the server compute commissions from daily sales when clients enter purchases\n")
    print ("What would you like to do? ...\n")
    print ("a). Enter Daily Sales\n")
    print ("b). Exit System\n")
    value = input()

    if value == 'a':
        print ("Enter Daily sales for Adventure Books..\n")
        adventure = input()
        adventure = float(adventure)
        advent = proxy.adventService(adventure)
        print ("\nEnter Daily Sales for Comic Books...\n")
        comic = input()
        comic = float(comic)
        com = proxy.comicService(comic)
        print ("\nEnter Daily Sales for Science Books...\n")
        science = input()
        science = float(science)
        sci = proxy.scienceService(science)
        print("Your Commissions are as follows..\n")
        print ("For selling Adventure books you made a commission of Ksh " + str(advent))
        print ("\nFor selling Comic books you made a commission of Ksh " + str(com))
        print ("\nFor selling Science books you made a commission of Ksh " + str(sci))
        
    if value == 'b':
          sys.exit()
        

   
