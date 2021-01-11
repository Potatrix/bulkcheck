import ipaddress
import os

# Requests doesn't seem to come included with Windows Python install
# https://github.com/psf/requests/archive/master.zip
# Should add a way to install the package automatically
import requests
import json
#import pickle


# Would be nice if the user only had to input this once, 
# Maybe I can use the pickle library to do this
csvPath = input("CSV File PATH: ")
print(csvPath)

OpSys = os.name

if os.name == "nt":
    print("You are running Windows")
else:
    print("You must be running Linux")