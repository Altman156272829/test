from scapy.all import IP, TCP, send

# Define the source and destination IPs
src_ip = "10.100.102.15"  # Example source IP
dst_ip = "10.100.102.1"    # Example destination IP

# Create the IP and TCP layers
ip = IP(src=src_ip, dst=dst_ip)
tcp = TCP(sport=12345, dport=80, flags="S", seq=1000)

# Combine the IP and TCP layers to create the SYN packet
syn_packet = ip / tcp

# Send the SYN packet
send(syn_packet)

