# Aruba-Central-BSSID-Report
Script to capture the current list of BSSIDs from Aruba Central and create a corresponding CSV file
```
% python3 bssid.py
2022-08-26 12:18:04 - ARUBA_BASE - INFO - Loaded token from storage from file: 
--- Starting ---
Office-AP,Wifi-Guy,d0:d4:f0:ee:2c:31
Office-AP,Wifi-Guy,d0:d4:f0:ee:2c:21
Bedroom-AP,Wifi-Guy,d0:d4:f0:ee:2e:b0
Bedroom-AP,Wifi-Guy,d0:d4:f0:ee:2e:a0
--- Finished ---
NOTE: Output saved to bssid_data.txt
```

Download the repo, make sure Python is installed.
Edit creds.py and enter the credentials for Aruba Central.
Also enter the wireless ESSID name you want to filter on.
Then execute the script 'python3 bssid.py'

The script will first generate a valid API key, then create a list of every active AP in Central. It will then query the BSSID info for each AP and output AP Name, ESSID Name and BSSID MAC detail. This will be shown on the screen as the script executes and written to a file called 'bssid_data.csv'.

Please feel free to modify or provide any comments or feedback.

Thank you - Will Smith
will@wifi-guys.com