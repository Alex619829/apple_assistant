#!bin/bash
source /usr/local/bin/apple_assistant/venv/bin/activate
if [[ $2 == "" ]]; then
    python /usr/local/bin/apple_assistant/main.py $1
fi
python /usr/local/bin/apple_assistant/main.py $1 "$2"
