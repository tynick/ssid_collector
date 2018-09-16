#!/usr/bin/python
# program to scan and store SSIDs automatically while driving around
from wifi import Cell, Scheme
import os
import csv
import config
import time
import mysql.connector

# these variables should be set in the config.py file
db_url = config.database['url']
db_name = config.database['name']
db_table = config.database['table']
db_user = config.database['user']
db_pw = config.database['passwd']
data_file = config.csv # file to save SSIDs
conn_test_url = config.conn['url']
conn_test_port = config.conn['port']


# get current time/date
def get_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
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

    # iterate through all SSIDs found
    for cell in cells:
        ssid = cell.ssid
        # ignore hidden SSIDs
        # string will be empty if SSID is hidden
        if ssid:
            # avoid duplicate SSIDs from multiple APs
            if ssid not in ssid_list:
                # add SSID to csv
                ssid_data = '"{0}", "{1}"\n'.format(get_time(), ssid)
                stage_info(ssid_data)
    return ssid_list

# insert ssid into DB
def insert_to_db():
# mysql connection info
    print("sending SSIDs to database")
    cnx = mysql.connector.connect(user=db_user,
          password=db_pw,
          database=db_name,
          host=db_url)
    cursor = cnx.cursor()
    with open(data_file, 'rb') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='"', skipinitialspace=True)
        for row in data:
            time_taken = row[0]
            ssid = row[1]
            print time
            print ssid
            query = ("INSERT INTO {0} (time_taken, ssid) VALUES ('{1}', '{2}');").format(db_table, time_taken, ssid)
            print query
            cursor.execute(query)
            cnx.commit()
    cursor.close()
    cnx.close()
    os.remove(data_file)

# stage SSID info in a csv file
def stage_info(data):
    with open(data_file,'a') as fd:
        fd.write(data)

def main ():
    # get nearby SSIDs
    ssids = get_ssids()
    # if we have internet, send data to DB
    if check_wifi_conn:
        print "connected"
        insert_to_db()
    

main()
