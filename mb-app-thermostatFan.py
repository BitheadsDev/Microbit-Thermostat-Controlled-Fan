from microbit import*

fanOnTemp = 20
temp = 0
fanSpeed = 12

stage = 'start'
funcStage = 'start'

#APP ULTILITY FUNCTIONS
def increaseFanOnTemp():
	print('increaseFanOnTemp')

def decreaseFanOnTemp():
	print('decreaseFanOnTemp')

def increaseFanSpeed():
	print('increaseFanSpeed')

def decreaseFanSpeed():
	print('decreaseFanSpeed')

#APP STAGE FUNCTIONS
def setTemp():
	print('setTemp')

def fan():
	print('fan')

#MAIN APP LOOP
while True:
	if stage == 'start':
		setTemp()
	else:
		fan()
