''' Update Lot_Zone table Proof of Concept
	v1 - First version - Select records based on last_update_date filter working
	v1a - Unable to make tabulation work with lot layer (no OID)
	v2 - New version, processes Zones in 30 (or custom via day_chunk variable) day chunks
'''

import logging
import sys
import os
import config

username = sys.argv[1]

#Set local or shared directory and Environments
#h_dir = os.getcwd() #Directory where script is is
h_dir = "C:\\TMP\\Python\\Lot_Zone" #Set directory as Local drive
log_dir = os.getcwd() #Directory for Log
f_dir = os.path.dirname(os.getcwd())
env_mode = config.env_mode #Get Environment setting

#SET LIMITS
zoneShp = 1 #Total number of zones to extract lots each round (Need to be set to 1, overlapped bbox's will exclude lots)
day_backtrack = 1 #How many days back should 'get_updated_lots' function go, this is due to the SIX Maps REST Service for lot cadastre being updated daily, lots can be missing if lot_zone process is run before lots in date range is updated to service
lotLimit = 200 #Total number of lots to query each round
day_chunk = 10 #Set to process x days at a time
int_limit = 1000 #Limit on number of lots before performing intersect query
json_limit = 1000 #Limit on number of lots to add to JSON

#Logging settings
logger = logging.getLogger("LotPlanningLog")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('{}\\log.txt'.format(log_dir))
formatter = logging.Formatter("%(asctime)s - {} - %(message)s".format(username),'%d/%m/%Y %H:%M:%S')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.debug("Importing Python Packages...")
logger.info("[START] Lot_Zone Update process started - [{}]".format(env_mode))

try:
	import arcpy
except:
	print("Error Importing arcpy module, make sure OpenVPN is connected and licences are available!")
	logger.info("[STOPPED] Unable to import arcpy module, Lot Planning update Stopped")
	sys.exit()

import shutil
from arcpy import env
import pandas as pd
from datetime import datetime, timedelta
import cx_Oracle
import requests
import json

logger.debug("Python packages imported successfully")

# Define the maximum number of retries and delay between retries
MAX_RETRIES = 5
RETRY_DELAY = 5  # in seconds

def loadingBar(p: int, msg: str) -> str:

	progress = ""
	togo = "          "
	
	if p > 0:
		togo = togo[:-p] #reduce empty space based on progress
	
	for i in range(p):
		progress += "■"

	print("[{}{}] {}".format(progress, togo, msg), end="\r")
	#sys.stdout.write("\r[{}{}] {}".format(progress, togo, msg))
	#sys.stdout.flush()

def getNextId(column: str, table: str) -> int:
	c.execute("select max({}) from {}".format(column, table))
	result = c.fetchone()

	#If records exist, increment next id, else start at 1
	if result[0] != None:
		nextId = result[0] + 1
	else:
		nextId = 1

	return nextId
			
if __name__ == "__main__":
	
	logger.info("[FINISH] Lot_Zone Update process finished")
	print("Done!")