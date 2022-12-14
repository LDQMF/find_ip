# find_ip
Python script that takes an input of a Mac Address and returns the associated IP Address.
Will sanitize input of Mac Address format to allow all accepted Mac Address formats.

# Requirements
- Python 3.7+
- isc_dhcp_leases

# Setup
Lease file path may vary from system to system. Make sure to set the correct path.

# Running find_ip
python3 find_ip.py "MAC ADDRESS"

# Examples
$ python3 find_ip.py 123456789abc
$ python3 find_ip.py 12-34-56-78-9a-bc
$ python3 find_ip.py 12:34:56:78:9a:bc
