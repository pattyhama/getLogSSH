#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Get result via SSH

import paramiko
import datetime
import time
import cmd
import sys

hostname = 'node\'s hostname'  # variable
ipaddress = 'localhost'  # variable
username = 'user'  # variable
password = 'pw'  # variable
date = datetime.date.today().strftime("%Y-%m-%d")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ipaddress, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command('uname -a')
# print stdout.read()

open_file = stdout.read()
config_file = open(hostname + "-" + date + ".log", "wb")
config_file.write(open_file)
config_file.close()
ssh.close()
print(("Finished python wrote ") + hostname + ("-") + date + (".log"))
