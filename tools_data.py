# tools_data.py — KaliCMD Toolkit learning/reference database
#
# Each tool entry contains:
#   name  : tool name
#   cat   : category
#   desc  : short learning-oriented description
#   cmds  : list of (description, command) pairs
#
# Commands are intended for authorized labs, CTFs, and systems you own
# or have explicit permission to test.

TOOLS = [
    {
        "name": "Nmap",
        "cat": "Information Gathering",
        "desc": "Network discovery and security auditing tool. Use it to learn how hosts, ports, services, and versions are identified.",
        "cmds": [
            ("Basic host scan", "nmap 192.168.1.10"),
            ("Scan selected ports", "nmap -p 22,80,443 192.168.1.10"),
            ("Service/version detection", "nmap -sV 192.168.1.10"),
            ("OS detection (authorized targets)", "nmap -O 192.168.1.10"),
            ("Default safe scripts", "nmap -sC 192.168.1.10"),
        ],
    },
    {
        "name": "Netcat",
        "cat": "Networking",
        "desc": "A networking utility useful for learning TCP/UDP connections, listeners, and simple data transfer in controlled environments.",
        "cmds": [
            ("Connect to a TCP service", "nc 192.168.1.10 80"),
            ("Listen on a TCP port", "nc -lvnp 4444"),
            ("UDP connection", "nc -u 192.168.1.10 53"),
        ],
    },
    {
        "name": "Nikto",
        "cat": "Web Security",
        "desc": "Web server scanner that checks for common configuration problems and potentially interesting files on authorized web servers.",
        "cmds": [
            ("Basic web server scan", "nikto -h http://192.168.1.10"),
            ("Scan an HTTPS site", "nikto -h https://192.168.1.10"),
        ],
    },
    {
        "name": "Gobuster",
        "cat": "Web Security",
        "desc": "Directory and DNS enumeration tool commonly used in web-security labs to discover exposed paths or subdomains.",
        "cmds": [
            ("Discover web directories", "gobuster dir -u http://192.168.1.10 -w /usr/share/wordlists/dirb/common.txt"),
            ("Discover DNS subdomains", "gobuster dns -d example.com -w /usr/share/wordlists/dns/subdomains-top1million-5000.txt"),
        ],
    },
    {
        "name": "WhatWeb",
        "cat": "Web Security",
        "desc": "Identifies technologies, frameworks, servers, and other fingerprints used by websites.",
        "cmds": [
            ("Identify web technologies", "whatweb http://192.168.1.10"),
            ("Verbose identification", "whatweb -v http://192.168.1.10"),
        ],
    },
    {
        "name": "WhatIs",
        "cat": "Information Gathering",
        "desc": "Use the standard whatis database to quickly learn what an installed Linux command is designed to do.",
        "cmds": [
            ("Describe a command", "whatis nmap"),
            ("Search descriptions", "whatis network"),
        ],
    },
    {
        "name": "Whois",
        "cat": "Information Gathering",
        "desc": "Queries domain registration information where publicly available.",
        "cmds": [
            ("Query a domain", "whois example.com"),
            ("Query an IP address", "whois 8.8.8.8"),
        ],
    },
    {
        "name": "DNSRecon",
        "cat": "Information Gathering",
        "desc": "DNS enumeration tool for authorized domains and security labs.",
        "cmds": [
            ("Enumerate a domain", "dnsrecon -d example.com"),
            ("Reverse lookup range", "dnsrecon -r 192.168.1.0/24"),
        ],
    },
    {
        "name": "theHarvester",
        "cat": "Information Gathering",
        "desc": "Collects publicly available information such as emails, hosts, and related data from supported sources.",
        "cmds": [
            ("Search a domain", "theHarvester -d example.com -b duckduckgo"),
            ("Limit result count", "theHarvester -d example.com -b duckduckgo -l 50"),
        ],
    },
    {
        "name": "Amass",
        "cat": "Information Gathering",
        "desc": "Performs DNS and subdomain enumeration for authorized domains and research environments.",
        "cmds": [
            ("Passive subdomain enumeration", "amass enum -passive -d example.com"),
            ("Save results", "amass enum -passive -d example.com -o amass.txt"),
        ],
    },
    {
        "name": "Subfinder",
        "cat": "Information Gathering",
        "desc": "Fast passive subdomain discovery tool for domains you are authorized to assess.",
        "cmds": [
            ("Find subdomains", "subfinder -d example.com"),
            ("Save results", "subfinder -d example.com -o subdomains.txt"),
        ],
    },
    {
        "name": "WafW00f",
        "cat": "Web Security",
        "desc": "Detects whether a web application is protected by a known web application firewall.",
        "cmds": [
            ("Detect a WAF", "wafw00f http://192.168.1.10"),
        ],
    },
    {
        "name": "WPScan",
        "cat": "Web Security",
        "desc": "WordPress security scanner for authorized WordPress installations.",
        "cmds": [
            ("Basic WordPress scan", "wpscan --url http://192.168.1.10"),
            ("Enumerate common users", "wpscan --url http://192.168.1.10 --enumerate u"),
        ],
    },
    {
        "name": "SQLMap",
        "cat": "Web Security",
        "desc": "Automates SQL injection testing and database assessment in authorized labs and applications.",
        "cmds": [
            ("Test a URL parameter", "sqlmap -u 'http://192.168.1.10/item?id=1'"),
            ("List available databases after confirmed injection", "sqlmap -u 'http://192.168.1.10/item?id=1' --dbs"),
        ],
    },
    {
        "name": "Burp Suite",
        "cat": "Web Security",
        "desc": "Web application testing platform with tools for inspecting and modifying HTTP requests in authorized environments.",
        "cmds": [
            ("Launch Burp Suite", "burpsuite"),
        ],
    },
    {
        "name": "Hydra",
        "cat": "Password & Authentication",
        "desc": "Online authentication auditing tool. Use only against accounts and services you are explicitly authorized to test.",
        "cmds": [
            ("Show Hydra help", "hydra -h"),
            ("SSH lab example", "hydra -l testuser -P /path/to/passwords.txt ssh://192.168.1.10"),
        ],
    },
    {
        "name": "John the Ripper",
        "cat": "Password & Authentication",
        "desc": "Password auditing and recovery tool for hashes you own or are authorized to test.",
        "cmds": [
            ("Show John help", "john --help"),
            ("Audit a hash file", "john hashes.txt"),
            ("Show recovered passwords", "john --show hashes.txt"),
        ],
    },
    {
        "name": "Hashcat",
        "cat": "Password & Authentication",
        "desc": "High-performance password recovery and auditing tool for authorized hash files.",
        "cmds": [
            ("Show Hashcat help", "hashcat --help"),
            ("Identify hash modes", "hashcat --example-hashes"),
        ],
    },
    {
        "name": "Aircrack-ng",
        "cat": "Wireless Security",
        "desc": "Wireless security auditing suite for authorized networks and wireless labs.",
        "cmds": [
            ("Show wireless adapter interfaces", "airmon-ng"),
            ("List nearby access points in a lab", "airodump-ng wlan0"),
            ("Show Aircrack help", "aircrack-ng --help"),
        ],
    },
    {
        "name": "Tshark",
        "cat": "Network Analysis",
        "desc": "Command-line packet analyzer from the Wireshark project.",
        "cmds": [
            ("List capture interfaces", "tshark -D"),
            ("Capture packets on an interface", "tshark -i eth0"),
            ("Read a capture file", "tshark -r capture.pcap"),
        ],
    },
    {
        "name": "Tcpdump",
        "cat": "Network Analysis",
        "desc": "Command-line packet capture and analysis utility.",
        "cmds": [
            ("List capture interfaces", "tcpdump -D"),
            ("Capture on an interface", "tcpdump -i eth0"),
            ("Read a PCAP file", "tcpdump -r capture.pcap"),
        ],
    },
    {
        "name": "Wireshark",
        "cat": "Network Analysis",
        "desc": "Graphical network protocol analyzer used to inspect packet captures.",
        "cmds": [
            ("Launch Wireshark", "wireshark"),
            ("Open a capture file", "wireshark capture.pcap"),
        ],
    },
    {
        "name": "Traceroute",
        "cat": "Networking",
        "desc": "Shows the network hops between your machine and a destination.",
        "cmds": [
            ("Trace a route", "traceroute example.com"),
        ],
    },
    {
        "name": "Ping",
        "cat": "Networking",
        "desc": "Basic connectivity and latency testing utility.",
        "cmds": [
            ("Ping a host", "ping -c 4 192.168.1.10"),
        ],
    },
    {
        "name": "Curl",
        "cat": "Networking",
        "desc": "Transfers data over many network protocols and is useful for learning HTTP requests.",
        "cmds": [
            ("Fetch a web page", "curl https://example.com"),
            ("Show response headers", "curl -I https://example.com"),
            ("Follow redirects", "curl -L https://example.com"),
        ],
    },
    {
        "name": "Wget",
        "cat": "Networking",
        "desc": "Command-line utility for downloading files and resources over supported protocols.",
        "cmds": [
            ("Download a file", "wget https://example.com/file.txt"),
            ("Continue an interrupted download", "wget -c https://example.com/file.zip"),
        ],
    },
    {
        "name": "SSH",
        "cat": "Remote Administration",
        "desc": "Secure remote shell client for systems where you have authorized access.",
        "cmds": [
            ("Connect to an SSH server", "ssh user@192.168.1.10"),
            ("Connect on a custom port", "ssh -p 2222 user@192.168.1.10"),
        ],
    },
    {
        "name": "SCP",
        "cat": "Remote Administration",
        "desc": "Securely copies files between systems over SSH.",
        "cmds": [
            ("Copy a file to a server", "scp file.txt user@192.168.1.10:/tmp/"),
            ("Copy a file from a server", "scp user@192.168.1.10:/tmp/file.txt ."),
        ],
    },
    {
        "name": "Git",
        "cat": "Development",
        "desc": "Version-control system useful for downloading and managing security-learning projects.",
        "cmds": [
            ("Clone a repository", "git clone https://github.com/user/repository.git"),
            ("Show repository status", "git status"),
        ],
    },
    {
        "name": "Python",
        "cat": "Development",
        "desc": "General-purpose programming language widely used for scripting, automation, and security learning.",
        "cmds": [
            ("Check Python version", "python3 --version"),
            ("Run a Python script", "python3 script.py"),
            ("Start the interactive shell", "python3"),
        ],
    },
    {
        "name": "Bash",
        "cat": "Linux Basics",
        "desc": "A common Linux shell. Learning Bash is essential for understanding command-line workflows.",
        "cmds": [
            ("Show the current shell", "echo $SHELL"),
            ("Print the current directory", "pwd"),
            ("List files", "ls -la"),
        ],
    },
    {
        "name": "Find",
        "cat": "Linux Basics",
        "desc": "Searches for files and directories based on useful criteria.",
        "cmds": [
            ("Find files by name", "find . -name '*.txt'"),
            ("Find executable files", "find . -type f -executable"),
        ],
    },
    {
        "name": "Grep",
        "cat": "Linux Basics",
        "desc": "Searches text using patterns and is one of the most useful Linux command-line tools.",
        "cmds": [
            ("Search a file", "grep 'password' notes.txt"),
            ("Case-insensitive search", "grep -i 'error' logfile.txt"),
            ("Recursive search", "grep -R 'TODO' ."),
        ],
    },
    {
        "name": "Sudo",
        "cat": "Linux Basics",
        "desc": "Runs commands with elevated privileges when your account is permitted to do so.",
        "cmds": [
            ("Run a command as administrator", "sudo command"),
            ("List permitted sudo commands", "sudo -l"),
        ],
    },
    {
        "name": "Chmod",
        "cat": "Linux Basics",
        "desc": "Changes file and directory permissions.",
        "cmds": [
            ("Make a script executable", "chmod +x script.sh"),
            ("Set common private file permissions", "chmod 600 private.txt"),
        ],
    },
    {
        "name": "Ps",
        "cat": "System Administration",
        "desc": "Displays running processes and their information.",
        "cmds": [
            ("Show your processes", "ps"),
            ("Show all processes", "ps aux"),
        ],
    },
    {
        "name": "Top",
        "cat": "System Administration",
        "desc": "Interactive process and resource monitor.",
        "cmds": [
            ("Start process monitor", "top"),
        ],
    },
    {
        "name": "Df",
        "cat": "System Administration",
        "desc": "Reports filesystem disk-space usage.",
        "cmds": [
            ("Show disk usage", "df -h"),
        ],
    },
    {
        "name": "Du",
        "cat": "System Administration",
        "desc": "Estimates file and directory space usage.",
        "cmds": [
            ("Show directory size", "du -sh ."),
            ("Show sizes of items", "du -h --max-depth=1 ."),
        ],
    },
    {
        "name": "File",
        "cat": "File Analysis",
        "desc": "Identifies the type of a file from its contents.",
        "cmds": [
            ("Identify a file", "file sample.bin"),
        ],
    },
    {
        "name": "Strings",
        "cat": "File Analysis",
        "desc": "Extracts printable strings from binary or other files and is useful for basic file inspection.",
        "cmds": [
            ("Extract printable strings", "strings sample.bin"),
            ("Search strings for a keyword", "strings sample.bin | grep -i 'flag'"),
        ],
    },
    {
        "name": "Binwalk",
        "cat": "File Analysis",
        "desc": "Analyzes firmware and binary files for embedded data and signatures.",
        "cmds": [
            ("Scan a file", "binwalk firmware.bin"),
            ("Extract recognized data in a lab", "binwalk -e firmware.bin"),
        ],
    },
    {
        "name": "ExifTool",
        "cat": "Digital Forensics",
        "desc": "Reads and writes metadata in many image, media, and document formats.",
        "cmds": [
            ("View metadata", "exiftool image.jpg"),
            ("View selected metadata", "exiftool -FileName -FileSize -CreateDate image.jpg"),
        ],
    },
    {
        "name": "Steghide",
        "cat": "Digital Forensics",
        "desc": "Steganography utility for embedding or extracting data from supported media files in authorized labs.",
        "cmds": [
            ("Inspect supported stego information", "steghide info image.jpg"),
        ],
    },
    {
        "name": "OpenSSL",
        "cat": "Cryptography",
        "desc": "Command-line toolkit for TLS, certificates, hashing, encryption, and other cryptographic operations.",
        "cmds": [
            ("Show OpenSSL version", "openssl version"),
            ("Calculate a SHA-256 digest", "openssl dgst -sha256 file.txt"),
        ],
    },
    {
        "name": "Hashid",
        "cat": "Cryptography",
        "desc": "Helps identify likely hash algorithms from a hash string.",
        "cmds": [
            ("Identify a hash type", "hashid '5f4dcc3b5aa765d61d8327deb882cf99'"),
        ],
    },
    {
        "name": "Searchsploit",
        "cat": "Vulnerability Research",
        "desc": "Searches the local Exploit-DB archive for vulnerability research and proof-of-concept references.",
        "cmds": [
            ("Search for a product", "searchsploit apache 2.4"),
            ("Show exact matches", "searchsploit -e 'apache 2.4'"),
        ],
    },
    {
        "name": "Metasploit Framework",
        "cat": "Security Testing",
        "desc": "Security testing framework used in controlled labs to study vulnerabilities, modules, payloads, and exploitation concepts.",
        "cmds": [
            ("Launch the console", "msfconsole"),
            ("Search modules", "search type:auxiliary name:scanner"),
        ],
    },
    {
        "name": "Msfvenom",
        "cat": "Security Testing",
        "desc": "Metasploit payload-generation utility. Use only in isolated labs and systems you control.",
        "cmds": [
            ("Show help", "msfvenom --help"),
            ("List payload formats", "msfvenom --list formats"),
        ],
    },
    {
        "name": "Yara",
        "cat": "Malware Analysis",
        "desc": "Pattern-matching tool used to identify files based on custom rules.",
        "cmds": [
            ("Scan a file with a rule", "yara rule.yar sample.bin"),
            ("Scan a directory recursively", "yara -r rule.yar ./samples"),
        ],
    },
    {
        "name": "Radare2",
        "cat": "Reverse Engineering",
        "desc": "Open-source framework for binary analysis and reverse engineering.",
        "cmds": [
            ("Open a binary", "r2 sample.bin"),
            ("Analyze a binary in quiet mode", "r2 -A sample.bin"),
        ],
    },
    {
        "name": "Ghidra",
        "cat": "Reverse Engineering",
        "desc": "Software reverse-engineering framework for analyzing compiled programs.",
        "cmds": [
            ("Launch Ghidra", "ghidra"),
        ],
    },
    {
        "name": "GDB",
        "cat": "Reverse Engineering",
        "desc": "GNU debugger used to inspect and debug programs.",
        "cmds": [
            ("Open a program in GDB", "gdb ./program"),
            ("Show registers", "info registers"),
        ],
    },
    {
        "name": "Ltrace",
        "cat": "Reverse Engineering",
        "desc": "Traces dynamic library calls made by a program.",
        "cmds": [
            ("Trace a program", "ltrace ./program"),
        ],
    },
    {
        "name": "Strace",
        "cat": "System Analysis",
        "desc": "Traces Linux system calls and signals made by a program.",
        "cmds": [
            ("Trace system calls", "strace ./program"),
            ("Trace file-related calls", "strace -e trace=file ./program"),
        ],
    },
    {
        "name": "SSH-Audit",
        "cat": "Security Auditing",
        "desc": "Audits SSH server configuration and protocol settings on authorized hosts.",
        "cmds": [
            ("Audit an SSH server", "ssh-audit 192.168.1.10"),
        ],
    },
    {
        "name": "Enum4linux",
        "cat": "Network Enumeration",
        "desc": "Enumerates information from Windows/Samba environments in authorized labs.",
        "cmds": [
            ("Enumerate a lab host", "enum4linux 192.168.1.10"),
        ],
    },
    {
        "name": "SMBClient",
        "cat": "Network Enumeration",
        "desc": "Command-line client for interacting with SMB/CIFS shares where you have authorization.",
        "cmds": [
            ("List SMB shares", "smbclient -L //192.168.1.10 -N"),
            ("Connect to a share", "smbclient //192.168.1.10/share"),
        ],
    },
    {
        "name": "SNMPWalk",
        "cat": "Network Enumeration",
        "desc": "Queries SNMP information from devices when SNMP access is authorized.",
        "cmds": [
            ("Query an SNMP host", "snmpwalk -v2c -c public 192.168.1.10"),
        ],
    },
    {
        "name": "LDAPSearch",
        "cat": "Directory Services",
        "desc": "Queries LDAP directories for authorized directory-service research and administration.",
        "cmds": 
