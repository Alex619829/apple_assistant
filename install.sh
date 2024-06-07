#!/bin/bash
if test -d /usr/local/bin/apple_assistant; then
    rm -r /usr/local/bin/apple_assistant
fi
mkdir /usr/local/bin/apple_assistant
cp -r * /usr/local/bin/apple_assistant
touch /usr/local/bin/apple_assistant/.env
cd /usr/local/bin/apple_assistant
python3.10 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
