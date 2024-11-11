# Initialize

## Installing Dependencies
```
sudo pip install -r requirement.txt
```
_if error, can use this command_
```
sudo pip3 install -r requirement.txt
```

## Change the following data

```
nano main.py
```
```
---
token_slack = "TOKEN_OAUTH"
channel_id = "CHANNEL_ID_SLACK"
name_bot = "NAME_BOT"
---
```

## Setup for Script Python

Setup for the service that runs this python program in the backgroud
```
sudo cp python-slack.service /etc/systemd/system/
sudo cp main.py /usr/local/bin/
```
```
sudo systemctl daemon-reload
sudo systemctl start python-slack.service
sudo systemctl status python-slack.service
