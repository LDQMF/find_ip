#!/usr/bin/env python
from isc_dhcp_leases import Lease, IscDhcpLeases
import os
import sys

def reformatInput(macAddress):
    macAddress = macAddress.replace(':','')
    macAddress = macAddress.replace('-','')
    macAddress = macAddress.lower()   
    
    macAddress = (':'.join(macAddress[i:i+2] for i in range(0, len(macAddress), 2)))

    return macAddress

def grabInput():
    if len(sys.argv) > 1:
        macAddress  = sys.argv[1]
    else:
        macAddress = input("Enter Mac Address:")

    macAddress = reformatInput(macAddress)
    return macAddress

def getIP(macAddress):
    
    lease_file = '/var/lib/dhcp/dhcpd.leases'

    if os.path.exists(lease_file):
        leases = IscDhcpLeases(lease_file)
    else:
        lease_file = os.path.basename(lease_file)
        leases = IscDhcpLeases(f'./{lease_file}')
    hold = leases.get_current()

    if (macAddress in hold):
        print (hold[macAddress].ip)
    else:
        print ('Mac Address not found')
    return

if __name__ == "__main__":
   macAddress = grabInput()
   getIP (macAddress)
