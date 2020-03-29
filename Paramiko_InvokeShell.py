import paramiko
import getpass
import time

# Create the SSH Client or SSH Object to whom you are gonna SSH


client = paramiko.SSHClient()
passwd = getpass.getpass()

# Now SSH Into the object

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("192.168.122.62", port=22, username="parth", password=passwd, look_for_keys=False, allow_agent=False)

remote_client = client.invoke_shell()

remote_client.send('enable \n')
remote_client.send('conf t \n')
remote_client.send('router ospf 1 \n')
remote_client.send('network 1.0.0.0 0.0.0.255 area 0\n')
remote_client.send('end\n')

time.sleep(3)

output = remote_client.recv(4096)

with open("Output.txt",'w') as op:
    op.write(output)