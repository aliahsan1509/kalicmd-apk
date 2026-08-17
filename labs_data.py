"""KaliCMD Academy — Step 8: Practice Labs.

Labs are designed for local machines, CTF platforms, intentionally vulnerable
training environments, or systems the learner owns/has explicit permission to test.
"""

LABS = [
    {
        "id": "linux-navigation",
        "title": "Linux Navigation",
        "category": "Linux",
        "level": "Beginner",
        "xp": 50,
        "objective": "Practice navigating directories and inspecting files from a terminal.",
        "scenario": "You are working inside a local practice folder and need to understand its structure.",
        "tasks": [
            "Print your current working directory.",
            "List the files and directories in it.",
            "Create a directory named academy_lab.",
            "Enter the new directory and verify your location.",
        ],
        "hints": [
            "Think about pwd, ls, mkdir and cd.",
            "Use pwd again after changing directories."
        ],
        "expected_learning": "You can move around a Linux filesystem and verify paths.",
        "completion": "Complete all four tasks in a local terminal."
    },
    {
        "id": "file-permissions",
        "title": "File Permissions",
        "category": "Linux",
        "level": "Beginner",
        "xp": 60,
        "objective": "Understand basic read, write and execute permissions.",
        "scenario": "A script in your own practice directory cannot be executed. Investigate its permissions.",
        "tasks": [
            "Create a small local text file or script.",
            "Inspect its permissions with a long directory listing.",
            "Identify the owner, group and permission bits.",
            "In your practice directory, change permissions so the owner can execute the script."
        ],
        "hints": [
            "ls -l shows permission bits.",
            "chmod changes permissions. Only modify files in your own lab directory."
        ],
        "expected_learning": "You understand the meaning of common Linux permission bits.",
        "completion": "Explain the permission bits and successfully change the practice file's owner execute permission."
    },
    {
        "id": "network-interface",
        "title": "Know Your Network",
        "category": "Networking",
        "level": "Beginner",
        "xp": 60,
        "objective": "Identify your own machine's network interfaces and routing information.",
        "scenario": "You are troubleshooting connectivity on your own Linux machine.",
        "tasks": [
            "List the network interfaces on your own machine.",
            "Find the IPv4 address of the interface you are using.",
            "Display the local routing table.",
            "Identify the default route."
        ],
        "hints": [
            "The ip command has subcommands for addresses and routes.",
            "Do this on your own machine or a dedicated lab VM."
        ],
        "expected_learning": "You can identify local interfaces, addresses and the default route.",
        "completion": "Record the interface, private IP address and default route for your lab machine."
    },
    {
        "id": "dns-basics",
        "title": "DNS Lookup Basics",
        "category": "Networking",
        "level": "Beginner",
        "xp": 60,
        "objective": "Understand how a domain name can be resolved.",
        "scenario": "You are diagnosing DNS on a machine you control.",
        "tasks": [
            "Resolve a harmless domain such as example.com using a normal DNS lookup tool.",
            "Record the returned address information.",
            "Check whether your machine has configured DNS resolver information.",
            "Explain in your own words what DNS did."
        ],
        "hints": [
            "getent hosts can perform a simple lookup.",
            "Keep the exercise to ordinary public domains or your own lab."
        ],
        "expected_learning": "You understand the basic relationship between a domain name and DNS resolution.",
        "completion": "Provide the lookup result and a one-sentence explanation of DNS."
    },
    {
        "id": "http-inspection",
        "title": "Inspect an HTTP Response",
        "category": "Web",
        "level": "Beginner",
        "xp": 70,
        "objective": "Read basic HTTP response metadata without attacking a site.",
        "scenario": "You are learning how a web client receives headers from a site intended for public access.",
        "tasks": [
            "Use curl to request response headers from example.com.",
            "Find the HTTP status code.",
            "Identify at least two response headers.",
            "Explain the difference between a request and a response."
        ],
        "hints": [
            "curl has an option for showing response headers.",
            "Use example.com or a local web server."
        ],
        "expected_learning": "You can recognize an HTTP status code and common response headers.",
        "completion": "Identify the status code and two headers and explain their purpose."
    },
    {
        "id": "log-analysis",
        "title": "Basic Log Analysis",
        "category": "Forensics",
        "level": "Beginner",
        "xp": 80,
        "objective": "Practice reading a log file and finding useful patterns.",
        "scenario": "A training VM contains a sample application log. Your job is to summarize normal and unusual entries.",
        "tasks": [
            "Open the supplied sample log in your lab.",
            "Count or identify repeated event types.",
            "Search for entries containing the word ERROR.",
            "Write a short summary of what you found."
        ],
        "hints": [
            "less, grep and wc are useful for local text analysis.",
            "Do not use this exercise to collect logs from systems you are not authorized to inspect."
        ],
        "expected_learning": "You can filter text logs and turn raw entries into a simple finding.",
        "completion": "Submit a short summary with the number or examples of error entries."
    },
    {
        "id": "hash-integrity",
        "title": "File Integrity with SHA-256",
        "category": "Cryptography",
        "level": "Beginner",
        "xp": 70,
        "objective": "See how a file hash changes when the file changes.",
        "scenario": "You need to verify whether a local practice file has been modified.",
        "tasks": [
            "Create a small practice file.",
            "Calculate its SHA-256 digest.",
            "Change one character in the file.",
            "Calculate the digest again and compare the two values."
        ],
        "hints": [
            "sha256sum is available on many Linux systems.",
            "A tiny change should produce a different digest."
        ],
        "expected_learning": "You understand the basic role of hashes in integrity checking.",
        "completion": "Show that the digest before and after the change is different."
    },
    {
        "id": "security-review",
        "title": "Local Security Review",
        "category": "Security",
        "level": "Beginner",
        "xp": 100,
        "objective": "Combine basic Linux and security concepts into a safe self-audit.",
        "scenario": "You are reviewing your own Linux practice VM before using it for learning.",
        "tasks": [
            "Identify the current user.",
            "Review basic file permissions in your practice directory.",
            "Review listening network services on your own machine.",
            "List available package updates without installing anything.",
            "Write three observations and three hardening ideas."
        ],
        "hints": [
            "whoami and id show identity information.",
            "ss can show listening sockets.",
            "Use package-manager read-only commands to inspect updates."
        ],
        "expected_learning": "You can combine identity, permissions, services and update awareness in a basic self-audit.",
        "completion": "Produce a short self-audit report based only on your own lab machine."
    },
    {
        "id": "web-lab-observation",
        "title": "Web Lab Observation",
        "category": "Web Security",
        "level": "Beginner",
        "xp": 100,
        "objective": "Learn to observe a deliberately provided training application's behavior.",
        "scenario": "You have a local intentionally vulnerable training application. Your task is observation, not exploitation.",
        "tasks": [
            "Open the local training application.",
            "Identify the main pages and forms.",
            "Record which HTTP methods are used during normal interaction.",
            "Note visible input fields and response status codes.",
            "Write two questions you would investigate in a later authorized lab."
        ],
        "hints": [
            "Use browser developer tools or a local proxy in your own lab.",
            "Do not test random public websites."
        ],
        "expected_learning": "You can map basic application behavior before attempting any security testing.",
        "completion": "Create a small application map containing pages, forms and observed methods."
    },
    {
        "id": "beginner-capstone",
        "title": "Beginner Cybersecurity Capstone",
        "category": "Capstone",
        "level": "Beginner",
        "xp": 150,
        "objective": "Demonstrate the core skills learned in the beginner modules.",
        "scenario": "You are given a fresh local Linux practice VM and must produce a short learning report.",
        "tasks": [
            "Document the current user and filesystem location.",
            "Document one network interface and the default route.",
            "Perform a safe DNS lookup.",
            "Inspect an HTTP response from a permitted training/public example.",
            "Calculate a SHA-256 hash for a local practice file.",
            "Write a five-point security observation report."
        ],
        "hints": [
            "Reuse commands and concepts from earlier labs.",
            "Keep every activity inside your own machine or an explicitly authorized training environment."
        ],
        "expected_learning": "You can connect Linux, networking, web, cryptography and security fundamentals into one workflow.",
        "completion": "Submit a concise report containing evidence for all six tasks."
    },
]
