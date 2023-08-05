#!usr/bin/python3

import nmap

scanner= nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<--------------->")

ip_addr= input("Please enter the IP address you want to scan:")
print("The IP you entered is:", ip_addr)
type(ip_addr)

resp= input("""\n Please enter the type of scan yu want to run:
            1. SYN ACK SCAN
            2. UDP SCAN
            3. Comprehensive Scan \n""")

print("you have selected option:", resp)

if(resp=='1'):
    print("Nmap Version:", scanner.nmap_version)
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip status:" ,scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports:", scanner[ip_addr]['tcp'].keys())

elif(resp=='2'):
    print("Nmap Version:", scanner.nmap_version)
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Ip status:" ,scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports:", scanner[ip_addr]['udp'].keys())

elif(resp=='3'):
    print("Nmap Version:", scanner.nmap_version)
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip status:" ,scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports:", scanner[ip_addr]['tcp'].keys())

elif(resp>='4'):
    print("Plese enter valid option")
