from napalm import get_network_driver
import getpass
import json

passwd = getpass.getpass()

# SPECIFY THE TYPE OF DRIVER YOU ARE USING

driver = get_network_driver('ios')

opt_args = {'secret':'cisco'} # Only for Cisco-IOS where it needs enable secret. Might not be true for JunOS

ios = driver('192.168.122.1','parth',passwd,optional_args=opt_args)

# TO OPEN THE CONNECTION
ios.open()

# THE CODE GOES HERE

#THIS CODE DISPLAYS THE BGP INFORMATION
output = ios.get_bgp_neighbors()

for item in output:
    print(item)

dump = json.dumps(output,sort_keys=4, indent=2)
print(dump)

# TO SAVE THE CONFIGURATION IN A FILE
with open('arp.txt', 'w') as f:
    f.write(dump)

# THE CONNECTION IS CLOSED

ios.close()