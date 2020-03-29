from netmiko import ConnectHandler
import getpass
import time


passwd = getpass.getpass()
cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username':'parth',
    'password': passwd,
    'port': 22,
    'secret':'cisco',
    'verbose':True
}

# Establish a SSH connection to the dictionary

connection = ConnectHandler(**cisco_device)


# Enter the enable mode
print("Entering Enable mode ")
connection.enable()

connection.send_config_from_file('hostname.txt')

connection.disconnect()