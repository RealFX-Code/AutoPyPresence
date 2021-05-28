from pypresence import Presence
import time
import json
import os

# This is where the two lines will be located.
# Edit "line1" to change the contents of the first line.
# Edit "line2" to change the contents of the second line.

line1 = "You really clicked on me?"
line2 = "WOW..."

def presence_open():
    with open('settings.json') as myfile:
        data = myfile.readline()
        #client_id = p['client_id2']
        print('Your client_id is', data)
        print('Opening Precense...')
        RPC = Presence(data)
        RPC.connect()
        RPC.update(state=line2, details=line1)
        print('Presence Opened!')
        print('Press Any Key To Close Presence...')
        os.system('pause>nul')

presence_open()
exit()
