# FL Studio AKAI APC Mini Script
A script to get the AKAI APC Mini to work with FL. 

1) Download the script, unzip it and follow the Image-Line instructions for setting up a custom midi controller profile (Basically save the Python file to {User data folder}\FL Studio\Settings\Hardware\APC Mini\device_apcmini.py).

2) Select the APC profile in F10 MIDI settings.

3) Use the round buttons along the bottom to select banks 1-8 left to right (the shift button turns off LEDs nothing.). When you select a new bank, the information box at the top of FL will tell you the bank you have selected, and the channels in that bank EG: Bank 2 selected (9-17)

4) Banks 9-14 are the buttons on the side, starting at the top, working your way down. They will also display the hint.

5) Move the sliders to move the mixer channels. Sliders are assigned per bank, left to right, so in bank 4, slider 8 will control channel 34.

Hope you enjoy this as much as I enjoyed making it. The script file is open source, so feel free to make any changes you like, and share them if you want to. :D
PS: Thanks to Scott for including this on the official list of user scripts!
