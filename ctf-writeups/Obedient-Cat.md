# Obedient Cat - picoCTF/CyLab Academy

**CTF:** Obedient Cat | Category: General Skills | Points: NA | Difficulty: Easy | Solves: 377,850 | Flag: <details><summary>Click here to reveal hidden text</summary>
academy{s4n1ty_v3r1f13d_61ddac22}
</details> 

## Summary
The challenge is a very basic introduction to what a flag is and how to use linux commands to read files.

## Description
This file has a flag in plain sight (aka "in-the-clear"). [Link to Original](https://learn.cylabacademy.org/library/147?page=1&search=obedient&workspace=true)

## Recon/Initial Analysis
I first looked at what was present in my Linux webshell provided by CyLabs Academy. There was only one file. So I had to download the file which contained the flag.

## Solution
- I downloaded the "flag" file to my Linux webShell using the command: `wget`. 
- I listed the files to verify if download was successful. I used the command `ls -l`
- I used the command `cat flag` to display the contents of the file and retrieve the flag.

## Lessons Learned
I was not able to figure out what I had to do because this is my first CTF and a new environment as well. 
I played around a bit with the webshell and eventually clicked on the hints that were provided and then realized what I had to do.
So next time, when doing ctfs on CyLabs, I will always use the `wget` command to download the files.
