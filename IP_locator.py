import re
import os
from urllib.request import urlopen
import json

regexp = '^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?).(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?).(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?).(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'

def IPCheck(ip):
	if(re.search(regexp,ip)):
		return True
	else:
		return False
def IP_Locator():
	try:
		IPAddr=str(input("Enter IP address: "))
		if(IPCheck(IPAddr)):
			site="http://ip-api.com/json/"
			res=urlopen(site+IPAddr)
			info=res.read()
			value=json.loads(info)
			print("IP: "+value['query']+ " status: "+value['status'])
			print("Country: "+value['country'])
			print("Region: "+value['regionName'])
			print("City: "+value['city'])
			print("Zipcode: "+value['zip'])
			print("Longitude: ",value['lon']," Latitude: ",value['lat'])
			print("ISP: "+value['isp'])
			print("Organization: "+value['org'])
			
		else:
			raise Exception("Incorrect IP Address")

	except Exception as e:
		print(e)
	except:
		print("Unable to retrieve info")

IP_Locator()