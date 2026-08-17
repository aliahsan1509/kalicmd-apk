"""KaliCMD Academy — Linux Fundamentals curriculum.

This module contains the first learning-path track.
Commands are intended for learning on the user's own Linux system,
VM, or authorized training environment.
"""

LINUX_FUNDAMENTALS = {
    "id": "linux-fundamentals",
    "title": "Linux Fundamentals",
    "level": "Beginner",
    "description": (
        "Learn the Linux command line, files, directories, permissions, "
        "processes, users, packages, networking basics, and safe terminal habits."
    ),
    "lessons": [
        {
            "id": "linux-01",
            "title": "01 — Meet the Terminal",
            "difficulty": "Beginner",
            "objective": "Understand what a shell is and run your first commands.",
            "concepts": [
                "Terminal vs shell",
                "Command structure",
                "Options and arguments",
                "Absolute vs relative paths",
            ],
            "commands": [
                {
                    "name": "Print the current directory",
                    "command": "pwd",
                    "explanation": "Shows the full path of your current working directory.",
                },
                {
                    "name": "List files",
                    "command": "ls",
                    "explanation": "Lists files and directories in the current directory.",
                },
                {
                    "name": "Detailed listing",
                    "command": "ls -la",
                    "explanation": "Shows a detailed listing, including hidden files.",
                },
                {
                    "name": "Show help",
                    "command": "ls --help",
                    "explanation": "Displays command-line help for ls.",
                },
            ],
            "practice": [
                "Open a terminal.",
                "Run pwd and identify your current directory.",
                "Run ls -la and identify at least three entries.",
            ],
        },
        {
            "id": "linux-02",
            "title": "02 — Files and Directories",
            "difficulty": "Beginner",
            "objective": "Create, inspect, copy, move, and remove files safely.",
            "concepts": [
                "Files and directories",
                "Paths",
                "Creating files",
                "Copying and moving",
                "Safe deletion",
            ],
            "commands": [
                {
                    "name": "Create a directory",
                    "command": "mkdir academy-practice",
                    "explanation": "Creates a directory named academy-practice.",
                },
                {
                    "name": "Enter the directory",
                    "command": "cd academy-practice",
                    "explanation": "Changes the current working directory.",
                },
                {
                    "name": "Create an empty file",
                    "command": "touch notes.txt",
                    "explanation": "Creates an empty file if it does not already exist.",
                },
                {
                    "name": "Copy a file",
                    "command": "cp notes.txt notes-backup.txt",
                    "explanation": "Creates a copy of notes.txt.",
                },
                {
                    "name": "Rename or move a file",
                    "command": "mv notes-backup.txt backup.txt",
                    "explanation": "Renames the file in the same directory.",
                },
                {
                    "name": "Remove a file",
                    "command": "rm backup.txt",
                    "explanation": "Deletes the specified file. Always verify the path before using rm.",
                },
            ],
            "practice": [
                "Create academy-practice.",
                "Create notes.txt inside it.",
                "Make a copy and rename the copy.",
                "Remove only the copy you created.",
            ],
        },
        {
            "id": "linux-03",
            "title": "03 — Reading and Searching Text",
            "difficulty": "Beginner",
            "objective": "Read text files and find information from the command line.",
            "concepts": [
                "Standard output",
                "Text files",
                "Pipes",
                "Searching",
            ],
            "commands": [
                {
                    "name": "Print a file",
                    "command": "cat notes.txt",
                    "explanation": "Prints the contents of notes.txt.",
                },
                {
                    "name": "Read a file page by page",
                    "command": "less notes.txt",
                    "explanation": "Opens a scrollable text viewer.",
                },
                {
                    "name": "Show the beginning",
                    "command": "head notes.txt",
                    "explanation": "Displays the beginning of a file.",
                },
                {
                    "name": "Show the end",
                    "command": "tail notes.txt",
                    "explanation": "Displays the end of a file.",
                },
                {
                    "name": "Search text",
                    "command": "grep \"Linux\" notes.txt",
                    "explanation": "Searches notes.txt for the word Linux.",
                },
                {
                    "name": "Combine commands with a pipe",
                    "command": "ls -la | less",
                    "explanation": "Sends ls output into the less viewer.",
                },
            ],
            "practice": [
                "Put a few lines of text into notes.txt.",
                "Read it with cat and less.",
                "Search for a word using grep.",
            ],
        },
        {
            "id": "linux-04",
            "title": "04 — Users and Permissions",
            "difficulty": "Beginner",
            "objective": "Understand Linux users, groups, ownership, and permission bits.",
            "concepts": [
                "Users",
                "Groups",
                "File ownership",
                "Read/write/execute permissions",
            ],
            "commands": [
                {
                    "name": "Show current user",
                    "command": "whoami",
                    "explanation": "Shows the username of the current account.",
                },
                {
                    "name": "Show user and group IDs",
                    "command": "id",
                    "explanation": "Displays your user ID and group memberships.",
                },
                {
                    "name": "Inspect permissions",
                    "command": "ls -l",
                    "explanation": "Shows ownership and permission information.",
                },
                {
                    "name": "Change file permissions",
                    "command": "chmod u+x script.sh",
                    "explanation": "Adds execute permission for the file owner.",
                },
            ],
            "practice": [
                "Run whoami and id.",
                "Create a practice file and inspect it with ls -l.",
                "Experiment with permissions only on files you created.",
            ],
        },
        {
            "id": "linux-05",
            "title": "05 — Processes and System Information",
            "difficulty": "Beginner",
            "objective": "Inspect running processes and basic system information.",
            "concepts": [
                "Processes",
                "Process IDs",
                "System information",
                "Resource monitoring",
            ],
            "commands": [
                {
                    "name": "List processes",
                    "command": "ps aux",
                    "explanation": "Displays currently running processes.",
                },
                {
                    "name": "Interactive process viewer",
                    "command": "top",
                    "explanation": "Provides a live view of processes and resource usage.",
                },
                {
                    "name": "Show kernel/system information",
                    "command": "uname -a",
                    "explanation": "Displays kernel and system information.",
                },
                {
                    "name": "Show disk usage",
                    "command": "df -h",
                    "explanation": "Shows filesystem disk usage in a human-readable format.",
                },
                {
                    "name": "Show memory usage",
                    "command": "free -h",
                    "explanation": "Shows memory and swap usage.",
                },
            ],
            "practice": [
                "Run uname -a and identify the kernel.",
                "Use ps aux to observe running processes.",
                "Check disk and memory usage.",
            ],
        },
        {
            "id": "linux-06",
            "title": "06 — Networking Basics",
            "difficulty": "Beginner",
            "objective": "Inspect your own machine's network configuration.",
            "concepts": [
                "IP addresses",
                "Network interfaces",
                "Routes",
                "DNS",
                "Connectivity",
            ],
            "commands": [
                {
                    "name": "Show network interfaces",
                    "command": "ip addr",
                    "explanation": "Displays network interfaces and assigned addresses.",
                },
                {
                    "name": "Show routing table",
                    "command": "ip route",
                    "explanation": "Displays the system's routing information.",
                },
                {
                    "name": "Test local network stack",
                    "command": "ping -c 4 127.0.0.1",
                    "explanation": "Sends four ICMP requests to your own loopback interface.",
                },
                {
                    "name": "Show listening sockets",
                    "command": "ss -tuln",
                    "explanation": "Lists listening TCP/UDP sockets without resolving names.",
                },
            ],
            "practice": [
                "Identify your network interface.",
                "Find your local IP address.",
                "Inspect the route table.",
                "Check which local ports are listening.",
            ],
        },
        {
            "id": "linux-07",
            "title": "07 — Packages and Software",
            "difficulty": "Beginner",
            "objective": "Understand package managers and safely inspect installed software.",
            "concepts": [
                "Package managers",
                "Repositories",
                "Installed packages",
                "Software updates",
            ],
            "commands": [
                {
                    "name": "Find an installed package",
                    "command": "dpkg -l | less",
                    "explanation": "Lists installed Debian packages and sends the output to a viewer.",
                },
                {
                    "name": "Find a command",
                    "command": "which python3",
                    "explanation": "Shows the executable path when the command is available in PATH.",
                },
                {
                    "name": "Check Python version",
                    "command": "python3 --version",
                    "explanation": "Displays the installed Python 3 version.",
                },
                {
                    "name": "Refresh Debian package metadata",
                    "command": "sudo apt update",
                    "explanation": "Refreshes package metadata. Review what the system is doing before confirming privileged actions.",
                },
            ],
            "practice": [
                "Check whether Python 3 is installed.",
                "Use which to locate a command.",
                "Explore installed packages without modifying the system.",
            ],
        },
        {
            "id": "linux-08",
            "title": "08 — Shell Productivity",
            "difficulty": "Beginner",
            "objective": "Become comfortable navigating and combining simple commands.",
            "concepts": [
                "Command history",
                "Environment variables",
                "Pipes",
                "Redirection",
            ],
            "commands": [
                {
                    "name": "View command history",
                    "command": "history",
                    "explanation": "Displays commands recorded in the current shell history.",
                },
                {
                    "name": "Show PATH",
                    "command": "echo $PATH",
                    "explanation": "Displays directories searched for executable commands.",
                },
                {
                    "name": "Redirect output to a file",
                    "command": "ls -la > listing.txt",
                    "explanation": "Writes ls output to listing.txt, replacing its previous contents.",
                },
                {
                    "name": "Append output to a file",
                    "command": "date >> listing.txt",
                    "explanation": "Appends the current date to listing.txt.",
                },
            ],
            "practice": [
                "Create a listing file.",
                "Append a date to it.",
                "Read the result with cat.",
            ],
        },
    ],
}
