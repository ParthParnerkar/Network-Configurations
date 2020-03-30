from netmiko import ConnectHandler
import getpass

passwd = getpass.getpass()

with open('config.txt','r') as f:
    device_list = f.read().splitlines()
    print(device_list)

my_list = list()

for ip in device_list:
    cisco_device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'parth',
        'password': passwd,
        'port': 22,
        'secret': 'cisco',
        'verbose': True
    }

    my_list.append(cisco_device)


for items in my_list:
    print("Connecting to " + items['ip'])
    connection = ConnectHandler(**items)

    print("Entering Enable mode now")
    connection.enable()
    connection.send_config_from_file()

    connection.disconnect()