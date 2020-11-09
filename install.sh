#!/usr/bin/bash
echo Installing........
echo
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
unzip ngrok-stable-linux-arm.zip
apt install pyinstaller
python3 escalator.py
