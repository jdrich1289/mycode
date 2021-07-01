#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

def custom(choice):
    for i in netifaces.interfaces():
        if choice == 'IP':
            print('IP: ', end='')  # This print statement will always print IP without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'])
        elif choice == 'MAC':
            print('MAC: ', end='') # This print statement will always print MAC without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'])
        else:
            print("Incorrect selection. Exitting program...")

#for i in netifaces.interfaces():
#    print('\n****** details of interface - ' + i + ' ******')
#    try:
#        print('MAC: ', end='') # This print statement will always print MAC without an end of line
#        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
#        print('IP: ', end='')  # This print statement will always print IP without an end of line
#        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
#    except:          # This is a new line
#        print('Could not collect adapter information') # Print an error message

asking = input("What do you want to see IP/MAC:  ")

custom(asking)
