# Resources used:
# https://docs.python.org/3/library/socket.html
# https://realpython.com/python-sockets/
# https://www.programiz.com/python-programming/datetime/current-datetime

import socket
from datetime import datetime

# Method to conduct port scanning
# Returns array list_stats: stored result of the scan in tuples
# t[0] is the port number, t[1] is the results (open or closed)
def scanTarget(target, start, end):
    list_stats = []

    # for each port in the range, see if the port is open
    for portnum in range(start,end):
        # get IP address of the target
        # socket.gethostbyname() returns target unchanged if is is already a IPv4
        address = socket.gethostbyname(target)
        # initialize socket and set timeout
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        # try to connect to port
        r = s.connect_ex((address, portnum))
        result = "Open" if r == 0 else "Closed"
        # store result in list_stats
        list_stats.append((portnum, result))
    
    return list_stats

# Method to print out port scan results 
# from array list_stats:  stored result of scan
def printStats(list_stats):
    for t in list_stats:
        print("Port %s:\t%s" % (t[0], t[1]))


# Main driver code
while True:
    # until the user exits by pressing control-C, 
    # keep asking for inputs
    try:
        # ask for target, and range of ports to scan
        target = input("Enter a target to scan: ")
        print("Please enter the range of ports you would like to scan on the target")
        start = int(input("Enter a start port (inclusive): "))
        end = int(input("Enter an end port (exclusive): "))
        # start scan
        print("Scanning started at: %s" % datetime.now())
        print("Please wait, scanning target now: %s" % target )
        list_stats = scanTarget(target, start, end)
        # print out results
        printStats(list_stats)
        print("Port Scanning Completed")
    except KeyboardInterrupt:
        print("\nExiting from portscan.py")
        break