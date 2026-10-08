# WINDOWS CMD LINE — QUICK REFERENCE

---

## 1. BASIC SYSTEM & INFORMATION COMMANDS

### SET

Displays all environment variables on the system.
Environment variables store system information such as file paths and usernames.

```
set                         List all environment variables
set USERNAME                Show a specific variable (USERNAME)
set NEWVAR=hello            Create a temporary variable
```

Example output:
COMPUTERNAME=WIN-THM
USERNAME=Administrator
OS=Windows_NT

### VER

Displays the current Windows version.

```
ver
```

Example output:
Microsoft Windows [Version 10.0.19041.1415]

### SYSTEMINFO

Shows detailed system information — OS version, hostname,
RAM, network adapters, installed hotfixes, and boot time.

```
systeminfo                  Full system info dump
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
                            Filter for OS info only
```

### MORE

Displays output one page at a time so it doesn’t flood the screen.
Press Space to go to the next page, or Q to quit.

```
more filename.txt           Read a file page by page
systeminfo | more           Pipe long output through more
```

### HELP

Displays help information for any command.

```
help                        List all available commands
help dir                    Help for a specific command
dir /?                      Alternative: show help for a command
```

### CLS

Clears the Command Prompt screen.

```
cls
```

## 2. NETWORK CONFIGURATION & TROUBLESHOOTING

### IPCONFIG

Shows network adapter information — IP address, subnet mask,
and default gateway. Essential for checking network configuration.

```
ipconfig                    Basic info (IP, subnet, gateway)
ipconfig /all               Full info including MAC, DNS, DHCP
ipconfig /release           Release current IP address (DHCP)
ipconfig /renew             Request a new IP address (DHCP)
ipconfig /flushdns          Clear the DNS cache
```

### PING

Tests connectivity to another host by sending packets and waiting for a response.
Shows whether a target is reachable and the latency (in milliseconds).

```
ping google.com             Ping by hostname
ping 10.10.10.1             Ping by IP address
ping -n 10 google.com       Send exactly 10 packets (default is 4)
ping -t google.com          Ping continuously until you press Ctrl+C
```

What to look for:
Reply from x.x.x.x          = target is reachable
Request timed out           = target is unreachable or blocking ping
100% packet loss            = no connection at all

### TRACERT

Traces the route packets take to reach a target.
Shows each hop (router) along the path and the response time for each hop.
Useful for finding where a connection is failing.

```
tracert google.com          Trace route to google.com
tracert 10.10.10.1          Trace route to an IP
```

Output format:
Hop number | Time (x3) | Router IP/hostname

### NSLOOKUP

Queries DNS servers for domain name information.
Use it to find the IP address a domain resolves to, or to look up mail servers.

```
nslookup google.com         Find IP address of a domain
nslookup 8.8.8.8            Reverse lookup — find domain from IP
nslookup                    Interactive mode (type domains one by one)
nslookup google.com 8.8.8.8 Query a specific DNS server
```

### NETSTAT

Shows active network connections, listening ports, and network statistics.
Useful for spotting suspicious connections — a core SOC and pentesting tool.

```
netstat                     Show active connections
netstat -a                  All connections + listening ports
netstat -b                  Show program associated with each connection (run as admin)
netstat -o                  Show Process ID (PID) for each connection
netstat -n                  Show addresses as numbers (no DNS resolution)
netstat -an                 Combine: all connections, numerical format
netstat -ano                Most useful: all, numerical, with PIDs
```

Flag summary:
-a    All established connections and listening ports
-b    Program/executable associated with each connection
-o    Process ID (PID) associated with each connection
-n    Numerical addresses and port numbers (faster, no DNS lookup)

Combine flags freely: netstat -anob shows everything at once

## 3. FILE & DISK MANAGEMENT

### CD

Change Directory. Navigate between folders.

```
cd                          Show current directory
cd foldername               Move into a folder
cd ..                       Go up one level (parent folder)
cd \                        Go to root of current drive (C:\)
cd /d D:\folder             Change drive AND directory at the same time
```

### DIR

Lists the contents of a directory. Similar to `ls` in Linux.

```
dir                         List files in current folder
dir C:\Users                List files in a specific path
dir /a                      Show hidden and system files too
dir /s                      Show files in current folder AND all subfolders
dir /s /b                   Same but bare format (just file paths)
dir *.txt                   List only .txt files
dir /o:s                    Sort by file size
dir /o:d                    Sort by date
```

### TREE

Displays a directory structure as a visual tree.

```
tree                        Show folder tree from current location
tree C:\Users               Show tree from a specific path
tree /f                     Include files in the tree (not just folders)
```

### MKDIR

Creates a new directory (folder).

```
mkdir newfolder             Create a folder in current location
mkdir C:\Users\test\logs    Create folder at a specific path
mkdir folder1 folder2       Create multiple folders at once
```

### RMDIR

Removes (deletes) a directory.

```
rmdir emptyfolder           Delete an empty folder
rmdir /s foldername         Delete folder AND everything inside it
rmdir /s /q foldername      Same but no confirmation prompt (/q = quiet)
```

### TYPE

Displays the contents of a text file. Similar to `cat` in Linux.

```
type filename.txt           Show file contents
type file1.txt file2.txt    Show multiple files
type filename.txt | more    Page through a large file
```

### COPY

Copies files from one location to another.

```
copy file.txt D:\backup\            Copy file to another folder
copy file.txt D:\backup\newname.txt Copy and rename
copy *.txt D:\backup\               Copy all .txt files
copy file1.txt + file2.txt combined.txt  Combine two files into one
```

### MOVE

Moves files to a new location (also used to rename files).

```
move file.txt D:\folder\        Move file to another folder
move oldname.txt newname.txt    Rename a file
move *.txt D:\folder\           Move all .txt files
```

### DEL / ERASE

Deletes files. Both commands do the same thing.

```
del filename.txt            Delete a file
del *.txt                   Delete all .txt files in current folder
del /f filename.txt         Force delete (even read-only files)
del /s *.txt                Delete all .txt files including subfolders
del /q filename.txt         Quiet mode — no confirmation prompt
```

Warning: `del` is permanent. No Recycle Bin. Be careful.

---

## TASK MANAGER & SYSTEM MAINTENANCE

### TASKLIST

Lists all currently running processes. Similar to Task Manager, but in the command line.
Useful for spotting suspicious processes.

```
tasklist                    List all running processes
tasklist /?                 Help and all available options
tasklist /FI "STATUS eq RUNNING"     Filter: only running tasks
tasklist /FI "IMAGENAME eq chrome.exe"  Filter: find a specific process
tasklist /SVC               Show services hosted in each process
tasklist /V                 Verbose — include window titles and more
```

`/FI` means filter. Common examples:
/FI "PID eq 1234"           Find a process with a specific PID
/FI "MEMUSAGE gt 50000"     Find processes using more than 50MB RAM

### TASKKILL

Terminates a running process. Use the PID from `tasklist`.

```
taskkill /PID 1234          Kill process with PID 1234
taskkill /PID 1234 /F       Force kill (use if normal kill doesn't work)
taskkill /IM chrome.exe     Kill by process name
taskkill /IM chrome.exe /F  Force kill by name
```

Workflow: tasklist → find the PID → taskkill /PID [number]

### CHKDSK

Checks the file system and disk for errors and bad sectors.
Useful when a drive is behaving strangely.

```
chkdsk                      Check current drive (read only, no fixes)
chkdsk C:                   Check C drive
chkdsk C: /f                Fix file system errors (needs reboot)
chkdsk C: /r                Find bad sectors and recover data (needs reboot)
chkdsk C: /f /r             Fix errors AND check bad sectors
```

### DRIVERQUERY

Lists all installed device drivers on the system.
Useful for spotting unusual or malicious drivers.

```
driverquery                 List all drivers
driverquery /v              Verbose — more detail
driverquery /fo csv         Output in CSV format (easy to parse)
driverquery | findstr "driver_name"    Search for a specific driver
```

### SFC /SCANNOW

System File Checker. Scans protected Windows system files for corruption
and automatically repairs them if possible. Must be run as Administrator.

```
sfc /scannow                Scan and repair system files
sfc /verifyonly             Scan only — don’t repair
sfc /scanfile=C:\path\file  Check a specific file only
```

After it runs, check results in:
C:\Windows\Logs\CBS\CBS.log

---

## QUICK REFERENCE — MOST USED COMBOS

- Check your IP:
`ipconfig /all`

- Find open ports and connections:
`netstat -ano`

- Find what program is using a port:
`netstat -ano | findstr :80`
`then: tasklist /FI "PID eq [PID from above]"`

- List all files including hidden:
`dir /a`

- Search for a file across the whole system:
`dir /s /b filename.txt`

- Kill a process by name:
`tasklist /FI "IMAGENAME eq processname.exe"`
`taskkill /IM processname.exe /F`

- Check if a host is reachable:
`ping -n 4 10.10.10.1`

---

## REMEMBER
- Run CMD as Administrator for commands that need elevated access
- Use /? after any command for full help: netstat /?
- Pipe output through findstr to search: netstat -ano | findstr :443
- Pipe through more for long output: systeminfo | more
- These commands + Linux equivalents = your daily toolkit in SOC and pentesting
