#name=AKAI APC Mini (Mixer Control/FPC)

# Import the required modules

import mixer
import midi
import device
import ui

selectedColour = 'Red'

def OnInit():
	global selectedBank #Make the selectedBank Variable
	selectedBank = 1 #Default the bank selector to 1
	clearAllLEDs() #Clear LEDs that may have been left on by other programs force-closing
	device.midiOutMsg(0x90 + (0x40 << 8) + (0x01 << 16)) #Turn on the LED for bank 1
	lightFPC() #Turn on the 4*4 matrix for the FPC controller in the top corner.
	#startTransport() #Start polling the transport

def OnDeInit(): #When FL is closed, clean up everything
	clearAllLEDs()


def OnNoteOn(event):   #Let's tell FL what to do when it recieves a note on event through midi
	print('Midi note on:', event.data1, " ", event.data2)
	if event.data1 > 63 and event.data1 < 81 or event.data1 > 81 and event.data1 < 88:	#Check to see if the note is in the range used by the patch selector
		event.handled = True #Start by telling FL we are dealing with this note to stop it from playing a tone
		setPatchBank(event.data1) #If it is, pass it through to the function that selects patches
		ui.setHintMsg("Bank " + str(selectedBank) + " selected (" + str(((selectedBank-1)*9)) + "-" + str(((selectedBank-1)*9)+8) + ")")
	elif event.data1 == 98:
		ui.setHintMsg("LEDs Turned off")
		clearAllLEDs()
		event.handled = True
	else:
		event.handled = False #Allows you to continue to use the pads inside of the FPC if you want to

def OnNoteOff(event):	#Tell FL what to do with note off data
	event.handled = True	#Not much here, just stop FL from getting too excited and playing a tone



def OnControlChange(event):	 #Let's define what FL will do when a slider moves
	if (event.pmeFlags & midi.PME_System != 0):	#Not entirely sure what this does, (pretty certian it rate limits) but it seems to improve performance, so I'll leave it in.
		mixer.setTrackVolume(bankSliderToChan(selectedBank, event.data1), event.data2/127) #Set the mixer track volume according to the input

def setPatchBank(bank): 	#This allows us to set the patch bank we are using
	global selectedBank #Makes the variable accessable everywhere
	if bank < 80:	#See if we are in the bottom row
		selectedBank = bank - 63	#perform the expression needed to convert from midi to mixer channel data
		clearAllLEDs() #Clears the LEDs that are on
		lightFPC() #Reilluminates the FPC
		device.midiOutMsg(0x90 + (bank << 8) + (0x01 << 16)) #Turns on the appropriate LED
	if bank > 80:	#See if we are in the side row
		selectedBank = bank - 73	#perform the expression needed to convert from midi to mixer channel data
		clearAllLEDs() #Clears all of the LEDs
		lightFPC() #Reilluminates the FPC
		device.midiOutMsg(0x90 + (bank << 8) + (0x01 << 16))
	return selectedBank	#Return the selected bank as an integer.

def bankSliderToChan(bank, slider):
	slider = slider-47 #Convert from midi to channel number
	return (((bank-1)*9)+slider-1) # Get the base number in the bank by subtracting 1 from it and multiplying by 9. Then add the slider -1 to this to get the channel number.
def clearAllLEDs():
	LEDNumber = 0
	for LEDNumber in range(0, 89):
		device.midiOutMsg(0x90 + (LEDNumber << 8) + (0x00 << 16))

def lightFPC():
	fpcpadsbase = [60, 52, 44, 36]
	for x in range(0, len(fpcpadsbase)):
		for y in range(0, 4):
			device.midiOutMsg(0x90 + (fpcpadsbase[x]+y << 8) + (ledColour(selectedColour) << 16))

def tempoUp():
	pass

def tempoDown():
	pass

def ledColour(colourText):
	if colourText == 'Green':
		return(1)
	elif colourText == 'GreenFlashing':
		return(2)
	elif colourText == 'Red':
		return(3)
	elif colourText == 'RedFlashing':
		return(4)
	elif colourText == 'Yellow':
		return(5)
	elif colourText == 'YellowFlashing':
		return(6)
