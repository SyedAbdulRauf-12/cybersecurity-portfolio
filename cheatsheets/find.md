# FIND command:
The basic structure is: 
`find [where to look] [what to look for]`

## Where to look:

- find .        # current folder and everything inside it
- find /home    # start from /home
- find /        # search the entire system

## What to look for — by name:

- find . -name "hello.txt"        # exact name
- find . -name "*.txt"            # anything ending in .txt
- find . -name "*password*"       # anything with "password" in the name

## What to look for — by type:

- find . -type f      # only files
- find . -type d      # only directories

## What to look for — by size:

- find . -size +1M    # larger than 1 megabyte
- find . -size -500c  # smaller than 500 bytes
- find . -size 1033c  # exactly 1033 bytes

## What to look for — by permissions and ownership:

- find /path -perm 644
- find /path -user john
- find /path -group developers

## Combining rules:
- find . -type f -size 1033c

Finds a file that is exactly 1033 bytes
