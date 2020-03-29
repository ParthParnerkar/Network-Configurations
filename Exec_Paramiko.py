import paramiko
import getpass

# Create the SSH Client or SSH Object to whom you are gonna SSH


client = paramiko.SSHClient()
passwd = getpass.getpass()

# Now SSH Into the object

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("192.168.122.62", port=22, username="parth", password=passwd, look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = client.exec_command("Show version")

output = stdout.read().decode()

with open("Configuration.txt", "w") as f:
    f.write(output)



