# 🌐 IP Address Validator

A Python-based tool that validates IPv4 and IPv6 addresses and displays useful network information using Python's built-in `ipaddress` module.

## ✨ Features

- ✅ Validate IPv4 and IPv6 addresses
- 🌍 Detect IP version
- 🔒 Identify Private or Public IP
- 🔁 Detect Loopback addresses
- 📡 Detect Multicast addresses
- 🛡️ Detect Reserved addresses
- 🌐 Display Network Address
- 📢 Display Broadcast Address (IPv4)
- 🎭 Display Subnet Mask
- 📏 Display Prefix Length
- 📊 Show Total Number of Addresses

## 🛠️ Technologies Used

- Python 3
- `ipaddress` (built-in module)

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/ip-address-validator.git
```

2. Navigate to the project directory:

```bash
cd ip-address-validator
```

3. Run the script:

```bash
python ip_validator.py
```

## 📷 Example Output

```text
Enter an IP Address: 192.168.1.10

===== IP Information =====
IP Address : 192.168.1.10
Version    : IPv4
Private    : Yes
Loopback   : No
Multicast  : No
Reserved   : No

===== Network Information =====
Subnet Prefix     : /24
Network Address   : 192.168.1.0
Broadcast Address : 192.168.1.255
Subnet Mask       : 255.255.255.0
Total Addresses   : 256
```

## 📚 Learning Outcomes

- Python fundamentals
- Exception handling
- Working with the `ipaddress` module
- IPv4 and IPv6 concepts
- Basic network automation

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, open an issue, or submit a pull request.

## 📄 License

This project is licensed under the MIT License.
