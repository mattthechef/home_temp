You have found my home automation project. This project is oriented around tinkering with 
many different home automation senors. This project will continue to evolve as I continue to tinker. Thanks for chekcing out my project!

Hardware: 
+--------------------+---------------------------+
Raspberry Pi 3 B      Central mircocomputer
Arduino Uno           Mirco controller 
TMP36                 Temperature Sensor 
+--------------------+---------------------------+

Technology: 
+-------------------------+----------------------+
Apache 2.4.25 (Raspbian)   Used as web server 
MariaDB 10.2.23		   SQL database 
Wordpress		   Content management

Summary:
Raspberry pi used to host web server and databse to store temperature data. 
Arduino used to read mV TMP36 signal and translate to a temperatuer(F) measurement. 
Arduino communicates with the Raspberry Pi via  i2c communication protcol. 
Raspberry Pi picks up temperature measurement over i2c stores it in the MariaDB. 
Wordpress then accesses MariaDB to display temperature(F).
Wordpress page is hosted on the Raspberry Pi  locally on the house wifi network. 


Hope you enjoyed this! mattthechef

