import os

try:
	# Checking the current status of wifi (on/off)
	cmd = os.popen('nmcli r wifi')
	output = cmd.read()

	# Condition for making the wifi turn on or off
	isWifiOn = 'enabled' in output
	
	#Notification timout duration
	duration = 3

	#By default assuming that plyer is installed further it will be checked.
	plyer_install = True

	# If it is installed then it will import the library otherwise throw an ImportError
	from plyer import notification


# Excepting the error and attempting to install plyer module in python
except Exception as e :
	# Command to install plyer module
	installing = os.popen('python -m pip install plyer',mode='w')
	# print(installing.read())
	
	# If not connected to internet then it will not be installed in the previous command
	# Thus to double check it (because of network connection) we try again to import the module
	try:
		# If it was installed from the previoud command, then it will import it here
		from plyer import notification

		#Notify regarding the installation of plyer module
		notification.notify(title="Downloading",message=' Required Files For Notification',timeout=3)
		notification.notify(title="Done",message=' Downloaded Required Files',timeout=3)


	# If it is not installed due to no Internet Connection, then simlpy contiue without it and popup an alert.
	except Exception as e :
		
		# Getting the wifi status and storing it in a variable for displaying in alert message
		on_or_off = ( lambda : 'Off' if isWifiOn else 'On' ) 

		# Alert message to be displayed in case of no internet and unsuccesful plyer installation.
		NotiMsg = "Continuing Without PLyer Installation. It will be installed when internet connection\
will be established next time.\n\n For Now :\n\n-You can turn Wifi on and Off \n-But You Will not get the notification for that.\
\n-Manually Check For That.\
\n\n[For Now, Your Wifi Connection will be Turned {res} ] ".format(res=on_or_off())

		# Using zenity for displayin system alter notification
		os.popen("sudo zenity --title 'Notification Error' --info  --width=400 --height=200 --text '{msg}' ".format(msg=NotiMsg))
		
		# Setting it to flase so that the upcoming notification statements will not be executed on the basis of this condition.
		plyer_install = False
	

# If wifi is on then turn it off otherwise turn it on.
if isWifiOn:
	os.popen("nmcli r wifi off")
	print("Turning Off Wifi..")

	# Wifi on icon
	wifiOff_icon = '/Wifi_on-off_python_file/network-wireless-disconnected.svg'
	# Disply notification if and only if plyer is installed in the system
	if plyer_install:
		notification.notify(title="Turning Wifi Off...",
		message="Wifi Turned Off.",timeout = duration,
		app_icon=wifiOff_icon)
else:
	os.popen("nmcli r wifi on ")
	print("Turning On Wifi...")

	# Wifi off icon

	wifiOn_icon = 'network-wireless-connected-100.svg'

	# Disply notification if and only if plyer is installed in the system
	if plyer_install:
		notification.notify(title="Turning Wifi On...",
		message="Wifi Turned On.",timeout = duration,app_icon=wifiOn_icon)