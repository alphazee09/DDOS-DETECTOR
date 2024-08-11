# DDOS Detector

This script uses the Scapy library to detect and prevent Distributed Denial of Service (DDOS) attacks on a server.

## Usage

1. Make sure you have Scapy installed (`pip install scapy`).
2. Run the script with root privileges (`sudo python ddos_detector.py`).
3. The script will start sniffing packets and detect DDOS attacks based on the number of packets coming from each IP address.
4. If an IP address is seen more than 100 packets in the last 60 seconds, it will be blocked using iptables (`iptables -A INPUT -s <ip_address> -j DROP`).

## Configuration

You can adjust the following parameters in the script:
- `ip_dict`: Dictionary to keep track of IP addresses and their packet counts.
- `count`: Number of packets to sniff in each iteration (default: 1000).
- `time.sleep(60)`: Time interval (in seconds) to reset the `ip_dict` (default: 60 seconds).
- `ip_dict[ip_src] > 100 or ip_dict[ip_dst] > 100`: Threshold for the number of packets from an IP address to consider it a potential DDOS attack (default: 100 packets).

## Note

- The script uses iptables to block IP addresses, so it requires root privileges to run.
- The script is a basic example and may need to be adapted based on your specific network setup and requirements.
- It's important to monitor the server's performance and adjust the threshold values based on your network traffic patterns.

## License

This script is licensed under the MIT License.
