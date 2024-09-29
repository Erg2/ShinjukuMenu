Scrolling menu for Shinjuku Station restaurant

Open shinjukustationvt.com and sequentially show each of its menu pages

Copyright © Shinjuku Station restaurant 2024

This is a Python app intended to be run on a Raspberry Pi

# Installed these to get it running on Win 11 WSL
sudo apt install python3-pip
pip install selenium
# did all the following on windows, not sure what actually made it work, if any
#wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#sudo apt-get install "fonts-liberation"
#sudo apt-get install libasound2
#sudo apt --fix-broken install

On pi
sudo apt-get install chromium-chromedriver

Create /home/mao/Desktop/Run_ShinjukuStationMenu.sh containing:
#!/bin/bash
source /home/mao/Desktop/ShinjukuStationMenu/env/bin/activate
python /home/mao/Desktop/ShinjukuStationMenu/ShinjukuMenu.py

Make it executable
chmod -x Run_ShinjukuStationMenu.sh

Make it auto start ... Another new way to autostart on PI AUGH!!!!
edit /home/mao/.config/wayfire.ini
add to the end of the file
[autostart]
runMenu = ./Desktop/Run_ShinjukuStationMenu.sh

