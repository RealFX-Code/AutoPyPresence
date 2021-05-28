import pypresence 
import json
import os

settingsfile = ".\\Settings.json"

def ask_id():
    clientid_tosave = input("Please Enter Application Id > ")
    print("Ok, your Application Id is %s Right?" % clientid_tosave)
    print("Press Enter To Confirm...")
    df30cb178eb8e37728f39b3e6551c8de = input()
    with open ("settings.json", "w") as f:
        f.write(clientid_tosave)
        f.close()

ask_id()
os.system('cls' if os.name == 'nt' else 'clear')
print("Sucsesfully saved your application-id!")
print("You can now open/edit Main.py.")
print("Your settings are at %s!", settingsfile)
c005d21e6f74e5515ab798ff251bcb88 = input("Press Enter To Exit.")
