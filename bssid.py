#!/usr/bin/python3
#(c) 2022 Will Smith

#First populate creds.py with Central info + API keys
#Enter the ESSID name to filter the resuslts for a specific SSID
#Output will be shown on the screen and a file called ap_data.txt is also generated in CSV format

from pycentral.base import ArubaCentralBase
import creds as creds

central_info = creds.central_info
central = ArubaCentralBase(central_info=central_info, ssl_verify=True)
essid_filter = creds.essid['essid_filter']

#This function will generate a list of all BSSIDs
def bssid():
    bssid_data = open("bssid_data.csv", "w")
    offset = 0
    while True:
        bssid_response = central.command(apiMethod="GET", apiPath="/monitoring/v2/bssids", apiParams={"limit": 1000, "offset": offset})
        for aps in bssid_response["aps"]:
            ap_name = aps["name"]
            for radio_bssids in aps["radio_bssids"]:
                for bssids in radio_bssids["bssids"]:
                    if bssids["essid"] == essid_filter:
                        essid = bssids["essid"]
                        macaddr = bssids["macaddr"]
                        print(ap_name + "," + essid + "," + macaddr)
                        bssid_data.write(ap_name + "," + essid + "," + macaddr + "\n")
        offset = offset + 1000
        if int(bssid_response['count']) == 0:
            break

if __name__ == "__main__":
    print("--- Starting ---")
    bssid()
    print("--- Finished ---")
    print("NOTE: Output saved to bssid_data.csv")
