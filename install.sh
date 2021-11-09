#!/usr/bin/env bash

echo 'Copying files...'
mkdir -p $HOME/.local/bin
cp -r templates fexplorer.py $HOME/.local/bin/
mkdir -p $HOME/.config/systemd/user
cp fexplorer.service $HOME/.config/systemd/user/

echo 'Starting services...'
systemctl --user daemon-reload
systemctl restart --user fexplorer.service
status=$(systemctl status --user fexplorer.service | grep 'Active: active')
if [[ $status ]]; then
	echo 'Service started successfully.'
else
	echo 'Unexpected error.'
	echo 'Please check the output of `systemctl status --user fexplorer.service`.'
fi
