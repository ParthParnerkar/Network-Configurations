import paramiko
import getpass
import time





def connection(host,port,username,passwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    passwd = getpass.getpass()
    client.connect(host, port=port, username=username, password=passwd, look_for_keys=False, allow_agent=False)
    return client

def remote(client):
    conn = client.invoke_shell()
    return conn

def send_command(conn):
    conn.send("enable \n")
    conn.send("show version")
    time.sleep(10)
    return conn

op1 = connection('192.168.122.141',22,'parth')
op2 = remote(op1)
output = send_command(op2)
print(output.recv(4096))
