# Nice netcat...

*CTF:* Nice netcat... | *Category:* General Skills |
*Points:* NA | *Difficulty:* Easy | *Solves:* 165,828 |
*Flag:* <details><summary>Click to reveal flag </summary>
academy{g00d_k1tty!_n1c3_k1tty!_7ef52}</details>

## Summary
This challenge was about using netcat to stream ascii values and then convert those values into human readable format.

## Challenge Description
There is a nice program that you can talk to by using this command in a shell:   
`$ nc chatelaine.cylabacademy.net <port number>`  
but it doesn't speak English...

## Recon / Initial Analysis
I ran the instance given to me and checked the details. I ran the given command and it displayed multiple lines of ASCII values.
I concluded that I need a command that will convert the ASCII to human-readable format.

## Solution
- I launched the instance provided for the netcat challenge.
- I ran the command `nc <host> <port no.>` (replace the host and port no. with the one provided in the challenge). The output was a bunch of numbers (ASCII value).
- But I didn't know what command I need to run, so I google what I need to do.
- I had to run the following code: `nc <host> <port no.> | awk '{printf "%c", $1} END{print ""}'` which returned the flag I needed.

## Lessons Learned
I learned a new command that will help me in the future.  
The `awk` command is a highly versatile text-processing and data extraction tool built into Linux and Unix-like operating systems.
It reads input line by line, breaks each line into individual fields, and performs specified actions.  
syntax: `awk [options] 'pattern { action }' filename`
- The netcat command opens a tcp connection to the instance and reads whatever it sends. 
- The pipe ` | ` takes output of the netcat command and gives it as input to the next command.
- `awk` reads line by line, `$1` is the first column on that line.
- `printf "%c"` is a C language style print statement, it interprets the ASCII value and prints the character.
- `END {print ""}` prints a new line so our terminal prompt isnt stuck on the same line as the flag.

## References
Google search.
