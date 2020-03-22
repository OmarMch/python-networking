#!/usr/bin/python3

import pexpect

devices = {'SW1': {'prompt': 'SW1#', 'ip': '192.168.122.254'},
           'SW2': {'prompt': 'SW2#', 'ip': '192.168.122.253'}}
username = 'omar'
password = 'cisco'

for device in devices.keys(): 
    device_prompt = devices[device]['prompt']
    child = pexpect.spawn('telnet ' + devices[device]['ip'])
    child.expect('Username:')
    child.sendline(username)
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt)
    child.sendline('show ip interface brief | i up')
    child.expect(device_prompt)
    print(child.before)
    child.sendline('exit')
