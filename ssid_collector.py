#!/usr/bin/python
# program to scan and store SSIDs automatically while driving around
from wifi import Cell, Scheme
import csv
import config

# these variables should be set in the config.py file
db_url = config.database['url']
db_pw = config.database['passwd']
data_file = config.csv # file to save SSIDs
conn_test_url = config.conn['url']
conn_test_port = config.conn['port']

print db_url
print db_pw
print data_file
print conn_test_url
print conn_test_port

# get current time/date
def get_time():
    current_time = "current time"
    return current_time

def check_wifi_conn():
    try:
        socket.create_connection((conn_test, conn_test_port))
        return True
    except OSError:
        pass
    return False

# get available SSIDs
def get_ssids():
    ssid_list = []
    # get list of all SSIDs in the area
    cells = Cell.all('wlan0')
    print cells

    # iterate through all SSIDs found
    for cell in cells:
        ssid = cell.ssid
        # ignore hidden SSIDs
        # string will be empty if SSID is hidden
        if ssid:
            # avoid duplicate SSIDs from multiple APs
            if ssid not in ssid_list:
                print ssid
                # add SSID to list
                ssid_list.append(ssid)
    return ssid_list

# insert ssid into DB
def insert_to_db():
    print("sending SSIDs to database")

# stage SSID info in a csv file
def stage_info(data):
    with open(data_file,'a') as fd:
        fd.write(data)


def main ():
    ssids = get_ssids()
    if check_wifi_conn:
        print "connected"

main()
