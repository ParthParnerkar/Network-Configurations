from netmiko import ConnectHandler
import getpass



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
# Establish a SSH Connection to the device using the dictitonary
connection = ConnectHandler(**cisco_device)

prompt = connection.find_prompt()

if '>' in prompt:
    connection.enable()

connection.send_config_set(["int loopback 0",'ip address 1.1.1.1 255.255.255.255','end'])


connection.disconnect()