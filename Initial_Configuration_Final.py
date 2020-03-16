import serial
import time


# Establish a connection to the console

def Open_Connection(port='/dev/tty.usbserial0',baudrate=9600):
    console = serial.Serial(port='/dev/tty.usbserial0',baudrate=9600,bytesize=8,parity='N',stopbits=1,timeout=8)
    if console.is_open():
        print("Connection established successfully")
        return console
    else:
        return False

# Sending Commands to the Console of a Networking Device

def Send_Command(console,cmd='\n',sleep=15):
    print("Sending Commands to the console" + cmd)
    console.write(cmd.encode() + b'\n')
    time.sleep(sleep)

# Recieving Commands from the Device on the Screen

def Recv_Command(console):
    bytes_recieved = console.in_waiting()
    if bytes_recieved:
        output = console.read(bytes_recieved)
        print(output.decode())
        return True
    else:
        return False

# Checking the initial commands from the output

def Inital_Command(console):
    Send_Command(console)
    prompt = Recv_Command(console)
    if "Would you like to enter the initial Configuration mode ?" in prompt:
        Send_Command(console,'no',sleep=20)
        Send_Command(console,'\r\n')
        return True
    else:
        return False
