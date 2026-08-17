"""KaliCMD Academy — Step 8 Part 3: Missions.

Missions combine concepts and safe practice tasks into guided learning goals.
Use them only with your own devices, local labs, CTFs, or systems where you
have explicit authorization.
"""

MISSIONS = [
    {
        "id": "linux-starter",
        "title": "🐧 Linux Starter Mission",
        "category": "Linux",
        "level": "Beginner",
        "xp": 100,
        "description": "Build a solid terminal and filesystem foundation.",
        "steps": [
            "Review the Linux filesystem concept.",
            "Complete the Linux Navigation practice lab.",
            "Complete the File Permissions practice lab.",
            "Write one sentence explaining why permissions matter."
        ],
        "hint": "Focus on paths, users, ownership and permission bits.",
        "success": "All listed learning steps are completed and the explanation is written."
    },
    {
        "id": "networking-starter",
        "title": "🌐 Networking Starter Mission",
        "category": "Networking",
        "level": "Beginner",
        "xp": 120,
        "description": "Learn how your own machine connects to a network.",
        "steps": [
            "Review the IP Address concept.",
            "Review the Ports concept.",
            "Complete the Know Your Network lab.",
            "Complete the DNS Lookup Basics lab."
        ],
        "hint": "Understand the difference between an IP address, a port and a DNS name.",
        "success": "You can describe your local interface, default route and DNS lookup."
    },
    {
        "id": "web-basics",
        "title": "🌍 Web Basics Mission",
        "category": "Web Security",
        "level": "Beginner",
        "xp": 140,
        "description": "Understand the basic request/response model before security testing.",
        "steps": [
            "Review the HTTP concept.",
            "Review HTTP Methods.",
            "Complete the Inspect an HTTP Response lab.",
            "Complete the Web Lab Observation lab in a local training environment."
        ],
        "hint": "First understand normal web behavior; security testing comes later.",
        "success": "You can identify a request method, status code and several response headers."
    },
    {
        "id": "crypto-foundations",
        "title": "🔐 Crypto Foundations Mission",
        "category": "Cryptography",
        "level": "Beginner",
        "xp": 120,
        "description": "Learn the difference between hashing and encryption.",
        "steps": [
            "Review the Hashing concept.",
            "Review the Encryption concept.",
            "Complete the File Integrity with SHA-256 lab.",
            "Explain why a hash is useful for integrity checking."
        ],
        "hint": "A hash and encryption solve different problems.",
        "success": "You can explain the integrity-checking role of a SHA-256 digest."
    },
    {
        "id": "security-observer",
        "title": "🛡️ Security Observer Mission",
        "category": "Security",
        "level": "Beginner",
        "xp": 150,
        "description": "Combine several fundamentals into a safe self-audit.",
        "steps": [
            "Review the Vulnerability concept.",
            "Review the Least Privilege concept.",
            "Complete the Local Security Review lab.",
            "Write three observations and three defensive improvements for your own lab."
        ],
        "hint": "Think about identity, permissions, exposed services and updates.",
        "success": "A short self-audit is completed using only your authorized lab environment."
    },
    {
        "id": "forensics-starter",
        "title": "🕵️ Forensics Starter Mission",
        "category": "Forensics",
        "level": "Beginner",
        "xp": 130,
        "description": "Practice turning local log data into useful observations.",
        "steps": [
            "Review the basic security/log-analysis concepts.",
            "Complete the Basic Log Analysis lab.",
            "Identify repeated events in the sample log.",
            "Summarize the notable entries without making unsupported conclusions."
        ],
        "hint": "Separate what the log proves from what you merely suspect.",
        "success": "You produce a short evidence-based summary of the provided training log."
    },
    {
        "id": "beginner-journey",
        "title": "🏆 Beginner Journey",
        "category": "Capstone",
        "level": "Beginner",
        "xp": 250,
        "description": "Finish a broad beginner cybersecurity learning journey.",
        "steps": [
            "Complete at least five Practice Labs.",
            "Complete the Beginner Cybersecurity Capstone.",
            "Answer at least three Concept quizzes correctly.",
            "Review your Progress page and write three topics to study next."
        ],
        "hint": "Do not rush. Understanding the fundamentals is more valuable than memorizing commands.",
        "success": "The capstone and the required learning milestones are completed."
    },
]
