import ipaddress

ip = input("Enter an IP address: ")

try:
    ip_obj = ipaddress.ip_address(ip)

    print("\n===== IP Address Information =====")
    print(f"IP Address : {ip_obj}")
    print(f"Version    : IPv{ip_obj.version}")

    # Private or Public
    if ip_obj.is_private:
        print("Type       : Private")
    else:
        print("Type       : Public")

    # Loopback
    print(f"Loopback   : {'Yes' if ip_obj.is_loopback else 'No'}")

    # Multicast
    print(f"Multicast  : {'Yes' if ip_obj.is_multicast else 'No'}")

    # Reserved
    print(f"Reserved   : {'Yes' if ip_obj.is_reserved else 'No'}")

    # Network (User enters subnet prefix)
    prefix = input("\nEnter subnet prefix: ")

    network = ipaddress.ip_network(f"{ip}/{prefix}", strict=False)

    print("\n===== Network Information =====")
    print(f"Network Address   : {network.network_address}")
    print(f"Broadcast Address : {network.broadcast_address if network.version == 4 else 'N/A'}")
    print(f"Subnet Mask       : {network.netmask}")
    print(f"Prefix Length     : /{network.prefixlen}")
    print(f"Total Addresses   : {network.num_addresses}")

except ValueError:
    print("Invalid IP Address or Prefix!")