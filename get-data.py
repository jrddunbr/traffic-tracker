#!/usr/bin/python3

from pathlib import Path
import urllib.request

IP_FILE = "ip-list.txt"
DATA_DIRECTORY = "data"

iplist = []

def getipFilename(ip):
    return DATA_DIRECTORY + "/" + ip

def hasIPFile(ipfilename):
    file = Path(ipfilename)
    if file.is_file():
        return True
    return False

# do not call this function more than needed or +1000 times per day
def fetch(ip):
    #response = urllib2.urlopen("http://ipinfo.io/{}/loc".format(ip))
    #resp = response.read()
    local_filename, headers = urllib.request.urlretrieve("http://ipinfo.io/{}/loc".format(ip))
    html = open(local_filename)
    resp = html.readline()
    html.close()
    filename = getipFilename(ip)
    ipfs = open(filename, 'w')
    ipfs.write(resp)
    ipfs.close()

ipf = open(IP_FILE)

for line in ipf:
    iplist.append(line[:-1])

ipf.close()

for ip in iplist:
    if hasIPFile(getipFilename(ip)):
        print("A file for {:15s} already exists".format(ip))
    else:
        print("A file for {:15s} does not exist".format(ip))
        fetch(ip)
        print("A file for {:15s} has been created".format(ip))
