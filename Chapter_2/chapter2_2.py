#!/usr/bin/python3

import getpass
from pexpect import pxssh

devices = {'SW1': {'prompt': 'SW1#', 'ip': '192.168.122.254'},
           'SW2': {'prompt': 'SW2#', 'ip': '192.168.122.253'}}
commands = ['term length 0', 'show version', 'show run']

username = input('Username: ')
password = getpass.getpass('Password: ')

# starts the loop for devices
for i in devices.keys():
    outputFileName = i + '_output.txt'
    device_prompt = devices[i]['prompt']
    child = pxssh.pxssh()
    child.login(devices[i]['ip'], username.strip(), password.strip(), auto_prompt_reset=False)
    # starts the loop for command to be written to output
    with open(outputFileName, 'wb') as f:
        for command in commands:
            child.sendline(command)
            child.expect(device_prompt)
            f.write(child.before)

    child.logout()
