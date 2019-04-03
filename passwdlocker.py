# passwdlocker.py - An insecure password locker program.

#sys module is required to receive command line argument 
#pyperclip enables to copy & paste stuff to machine's clipboard
#pip install pyperclip 

import sys
import pyperclip

PASSWORDS = {'email':'user12324@gmail.com',
			'usr':'admin',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',	
			'github':'something',
             'admin': '1234045'}

#sys.argv is a list containing commandline arguments,including the name of the file as 0th item in list 

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name 

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
