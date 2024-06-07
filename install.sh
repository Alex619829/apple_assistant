#!/bin/bash
if test -d /usr/local/bin/apple_assistant; then
    rm -r /usr/local/bin/apple_assistant
fi

mkdir /usr/local/bin/apple_assistant
cp -r * /usr/local/bin/apple_assistant
touch /usr/local/bin/apple_assistant/.env

file="/usr/local/bin/apple_assistant/config.py"
old_string="DIR = os.getcwd()"
new_string="DIR = '/usr/local/bin/apple_assistant'"
sed -i -e "s|$old_string|$new_string|g" $file

if test -d /usr/local/bin/apple_assistant/venv; then
    rm -r /usr/local/bin/apple_assistant/venv
fi

cd /usr/local/bin/apple_assistant
python3.10 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
