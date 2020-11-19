attempts = int(input("Enter no of attempts: "))
while attempts > 0:
    IP = input("IP Address: ")
    IP = IP.split(".")
    for val in IP:
        if int(val) > 255:
            print("Invalid IP address")
            break
        continue
    IP = list(map(int, IP))
    for mask in IP:
        if IP[0] >= 192:
            print("This is a Class C IP address")
            print("Subnet Mask: 255.255.255.0")
            break
        if IP[0] == 127:
            print("This is a loopback address")
            break
        elif 192 > IP[0] > 127:
            print("This is a Class B IP address")
            print("Subnet Mask: 255.255.0.0")
            break
        elif IP[0] < 127:
            print("This is a Class A IP address")
            print("Subnet Mask: 255.0.0.0")
            break
    attempts = attempts - 1
