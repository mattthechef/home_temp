#*****************************************#
# This script was created to facilitate the 
# main function for the home_temp automation.
# See README.md for futher explination.
# 
#
# Author: Max Anderson 
# Date: 03/16/2019
#
#*****************************************#


from smbus2 import SMBus 
import time as t
import mysql.connector as mariadb

DEVICE_ADDR = 0x8		#configured arduino i2c address
bus = SMBus(1) 			# 0 = /dev/i2s-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

#connect to the mariaDB that has been configured on the raspberry pi 
mariadb_connection = mariadb.connect(user='root', password='mta77821',database='home_temp')
cursor = mariadb_connection.cursor()


while True: 
	data = bus.read_byte_data(DEVICE_ADDR,0)	#read data from bus at DEVICE_ADDR
	print(data)
	t.sleep(1)
