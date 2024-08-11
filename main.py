from scapy.all import *
import time


def detect_ddos(pkt):
    if IP in pkt:
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst

        # Check if the source IP address has been seen before
        if ip_src in ip_dict:
            ip_dict[ip_src] += 1
        else:
            ip_dict[ip_src] = 1

        # Check if the destination IP address has been seen before
        if ip_dst in ip_dict:
            ip_dict[ip_dst] += 1
        else:
            ip_dict[ip_dst] = 1

        # If the source or destination IP address has been seen more than 100 times in the last 60 seconds, block the IP address
        if ip_dict[ip_src] > 100 or ip_dict[ip_dst] > 100:
            print(f"Blocking IP address: {ip_src}")
            os.system(f"iptables -A INPUT -s {ip_src} -j DROP")
        if ip_dict[ip_dst] > 100:
            print(f"Blocking IP address: {ip_dst}")
            os.system(f"iptables -A INPUT -s {ip_dst} -j DROP")


def reset_dict():
    global ip_dict
    ip_dict = {}


# Dictionary to keep track of IP addresses and their packet counts
ip_dict = {}

# Start sniffing packets
print("Starting DDOS detection...")
while True:
    sniff(prn=detect_ddos, count=1000)
    reset_dict()
    time.sleep(60)