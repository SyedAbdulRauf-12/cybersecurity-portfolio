# Module 3: Operating System Basics
We have all been using Windows, Mac, Linux even on our computer devices. But what exactly are they?

# Operating Systems Intro
An Operating System is system software that manages hardware resources and provides common services for user programs. It acts as an abstraction intermediary: programs call the OS kernel via system calls instead of writing raw voltage to disk controllers or memory buses directly.

## Linux Command Line Interface Basics
Linux powers the vast majority of web servers, cloud infrastructure, and security tooling (such as Kali Linux).

**Key Navigation & Inspection Commands:**

- pwd: Print working directory.
- ls -la: List all files including hidden files with permissions and ownership.
- cd /path/to/dir: Change active directory.
- cat file.txt / less file.txt: View contents of a file.

**File Management & Permissions:**

- mkdir folder_name: Create a directory.
- cp source.txt dest.txt: Copy a file.
- mv old.txt new.txt: Move or rename a file.
- rm -r directory: Recursively remove a directory.
- chmod 755 script.sh: Modify permissions (Read, Write, Execute for Owner/Group/Others).
- grep "keyword" log.txt: Search for patterns inside text files.

## Windows CLI Basics

Windows provides two primary command-line environments: the legacy Command Prompt (cmd.exe) and PowerShell (powershell.exe), an object-oriented shell environment.

**Command Prompt Basics:**

- dir: List directory contents.
- cd: Change directory.
- ipconfig /all: Display full network interface details.
- netstat -ano: Display open connections and associated process IDs (PIDs).
- tasklist: View running processes.

## PowerShell Basics:
- Get-Process: Display active processes.
- Get-Service: Inspect status of Windows services.
- Test-NetConnection -ComputerName target.com -Port 80: Perform network diagnostics.

## Windows Basics
- File System: Uses drive-letter mappings (C:\) and the NTFS file system, which enforces granular Access Control Lists (ACLs).
- Registry: A hierarchical database storing system-wide and user-specific configuration settings, boot parameters, and application preferences. Attackers often target the Registry to establish persistence (e.g., Run keys).
- Event Viewer: Centralized tool where Windows records Application, Security, and System logs. Crucial for tracing failed logon attempts (Event ID 4625).

## OS Security

- Authentication vs. Authorization: Authentication confirms identity (e.g., password, biometrics); authorization dictates access rights (e.g., read vs. modify).
- Principle of Least Privilege (PoLP): Users and programs should only be granted the minimum permissions required to perform their explicit function.
- Updates & Patching: Operating systems regularly release updates to remediate vulnerabilities (such as privilege escalation bugs) discovered in kernel or service code.
