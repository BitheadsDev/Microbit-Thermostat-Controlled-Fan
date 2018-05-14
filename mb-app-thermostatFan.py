from microbit import*

fanOnTemp = 25
temp = 0
fanSpeed = 2
wait = 2000
minTemp = 0
maxTemp = 40

stage = 'start'
funcStage = 'start'
action = False
timeCompare = 0
fanSpeedConv = 204 #1023 / fanSpeed convert the 25 user selected fan speeds to the 0-1023 values of the pin voltage signals
fanSpeedAnalog = fanSpeed * fanSpeedConv
maxSpeed = 4

#List of pin positions for the fan speed
powerImg1 = Image("00000:00000:00000:00000:99999")
powerImg2 = Image("00000:00000:00000:99999:99999")
powerImg3 = Image("00000:00000:99999:99999:99999")
powerImg4 = Image("00000:99999:99999:99999:99999")
powerImg5 = Image("99999:99999:99999:99999:99999")

powerImgs = (powerImg1,powerImg2,powerImg3,powerImg4,powerImg5)

#APP ULTILITY FUNCTIONS

def ifWait(timeCompare, wait):
	#Return true if 3000ms have passed. Can adjust wait variable to lessen or lengthen wait period.
	if running_time() - timeCompare >= wait:
		# print(str(timeCompare))
		# print(str(running_time()))
		# print(str(wait))
		return True
	else:
		return False

def increaseFanOnTemp(fanOnTemp, maxTemp, minTemp):
	if fanOnTemp <= maxTemp:
		fanOnTemp += 1
	else:
		fanOnTemp = minTemp
	return fanOnTemp

def decreaseFanOnTemp(fanOnTemp, maxTemp, minTemp):
	if fanOnTemp >= minTemp:
		fanOnTemp -= 1
	else:
		fanOnTemp = maxTemp
	return fanOnTemp

def increaseFanSpeed(fanSpeed):
	if fanSpeed <= 4:
		fanSpeed += 1
	else:
		fanSpeed = 0
	return fanSpeed

def decreaseFanSpeed(fanSpeed):
	if fanSpeed >= 0:
		fanSpeed -= 1
	else:
		fanSpeed = 4
	return fanSpeed

def showFanSpeed(fanSpeed):
	display.show(powerImgs[fanSpeed])

def calcFanSpeedAnalog(fanSpeed, fanSpeedConv):
	return fanSpeed * fanSpeedConv

#MAIN APP LOOP
while True:
	#STAGE 1: SET TEMPERATURE
	if stage == 'start':
		if button_a.was_pressed():
			timeCompare = running_time()
			display.clear()
			fanOnTemp = decreaseFanOnTemp(fanOnTemp, maxTemp, minTemp)
			display.scroll(str(fanOnTemp))
			action = True
		elif button_b.was_pressed():
			timeCompare = running_time()
			display.clear()
			fanOnTemp = increaseFanOnTemp(fanOnTemp, maxTemp, minTemp)
			display.scroll(str(fanOnTemp))
			action = True
		elif action == False:
			display.show('T?')
		elif ifWait(timeCompare, wait):
			action = False
			stage = 'fan'

	#STAGE 2: Fan
	else:
		if temperature() >= fanOnTemp:
			pin0.write_analog(fanSpeedAnalog)
		else:
			pin0.write_analog(0)
			#Display fan speed if first iteration (as no actions have taken place)
			#Also display if button has been pressed and 3s have passed
		if funcStage == 'start' or (ifWait(timeCompare, wait) and action == True):
			showFanSpeed(fanSpeed)
			action = False
			funcStage = 'controls'

		sleep(40) #attempt to keep the CPU cool and seems to help with reading or sending the voltage value properly
		if button_a.was_pressed():
			timeCompare = running_time()
			display.clear()
			fanOnTemp = decreaseFanOnTemp(fanOnTemp, maxTemp, minTemp)
			display.scroll(str(fanOnTemp))
			action = True
		elif button_b.was_pressed():
			timeCompare = running_time()
			display.clear()
			fanOnTemp = increaseFanOnTemp(fanOnTemp, maxTemp, minTemp)
			display.scroll(str(fanOnTemp))
			action = True
		else:
			while pin2.is_touched():
				if fanSpeed < maxSpeed:
				    fanSpeed += 1
				else:
				    fanSpeed = 0
				display.show(powerImgs[fanSpeed])
				fanSpeedAnalog = calcFanSpeedAnalog(fanSpeed, fanSpeedConv)
				sleep(400)
				action = True