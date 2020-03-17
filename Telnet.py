import telnetlib
import getpass


host = '10.0.0.1' # Enter the IP address to connect to
user = 'xyz'   # Enter the username which was used while configuring Telnet
password = getpass.getpass()

tn = telnetlib.Telnet(host)

tn.read_until("Username: ")
tn.write(user.encode() + b'\n')

if password:
    tn.read_until('Password: ')
    tn.write(password.encode() + b'\n')

tn.write(b"enable\n")
tn.write(b'terminal length 0\n')
tn.write(b'show ip int br\n')
tn.write(b'exit\n')

print(tn.read_all().decode())


