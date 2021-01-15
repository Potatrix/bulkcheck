import ipaddress
import os

# Requests doesn't seem to come included with Windows Python install
# https://github.com/psf/requests/archive/master.zip
# Should add a way to install the package automatically
import requests
import json
import csv
#import pickle

def setCSVPath():
    # Would be nice if the user only had to input this once, 
    # Maybe I can use the pickle library to do this
    # Setting path for CSV File
    csvPath = input("CSV File PATH: ")
    print(csvPath)
    return(csvPath)

def getRequestsLibrary():
    # I had to install requests library manually when running on windows, so thinking a function to check that the library is installed
    # would be helpful, this section is not complete yet
    OpSys = os.name

    if os.name == "nt":
        print("You are running Windows")
    else:
        print("You must be running Linux")

def openCSVFile(csvPath):
    with open(csvPath, newline='') as csvfile:
        IPreader = csv.reader(csvfile, delimiter='\n', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        ipList = []
        for IP in IPreader:
            #print(IP)

            # I decided to store each IP in an array so we could use it more flexibly later, for a very large file this is a bad idea
            # May be better to run the Web Requests while it's reading the file, we just wouldn't be able to work with the IPs later in some other way
            ipList.append(IP)
            print(ipList)
        return(ipList)
    
# Grab CSV path and store in variable
csvPath = setCSVPath()

# Grab list of IPs in CSV. If the file is HUGE this may be a bad idea
ipList = openCSVFile(csvPath)

