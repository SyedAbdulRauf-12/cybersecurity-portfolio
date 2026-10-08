# WHAT IS GREP?

grep stands for "Global Regular Expression Print".
It searches through files and prints every line that matches what you're looking for. Think of it like Ctrl+F but for
the terminal, and way more powerful.

Basic syntax:
`grep [options] "search_term" [file or path]`

---

## CHEAT SHEET — QUICK COPY-PASTE COMMANDS
| COMMANDS | ACTION |
|----------|--------|
| grep "term" file.txt               |     Single file search |
| grep "term" *                      |     All files in current folder |
| grep -r "term" .                   |     Recursive from current folder |
| grep -i "term" file.txt            |     Case insensitive |
| grep -n "term" file.txt            |     Show line numbers |
| grep -w "term" file.txt            |     Whole word only |
| grep -l "term" *                   |     Filenames only |
| grep -v "term" file.txt            |     Lines that don't match |
| grep -c "term" file.txt            |     Count matches |
| grep -rni "term" . 2>/dev/null     |     Recursive, no errors, case insensitive, line numbers |
| grep -C 3 "term" file.txt          |     3 lines of context around match |
| grep -E "term1|term2" file.txt     |     Search for multiple terms |

---

# Descriptions and Explanations:

## 1. SEARCHING A SINGLE FILE
`grep "word" filename.txt`

- Prints every line in filename.txt that contains "word".
- Examples:
    grep "password" notes.txt
    grep "error" system.log
    grep "admin" users.txt

---

## 2. SEARCHING MULTIPLE FILES
- Search all files in the current folder:
`grep "word" *`

- Search inside a specific directory (not subfolders):`
grep "word" /path/to/folder/*`

- Search recursively (current folder + all subfolders):
`grep -r "word"` 

- Search recursively from a specific path:
`grep -r "word" /path/to/directory/`

- The dot (.) always means "current directory you are in".

  ---

## 3. USEFUL FLAGS (OPTIONS)
You can mix and match these flags together.

| FLAG | WHAT IT DOES |
|------|--------------|
| -i | Ignore case — matches "Word", "WORD", "word" all the same |
|-w | Whole word only — won't match "password" if you search "pass" |
| -n | Show line numbers where the match was found |
| -l | Show only filenames, not the matching lines themselves |
| -r | Search recursively through folders and subfolders |
| -v | Invert — show lines that DON'T match (very useful) |
| -c | Count how many lines matched instead of showing them |
| -A 3 | Show 3 lines AFTER the match (context) | 
| -B 3 | Show 3 lines BEFORE the match (context) | 
| -C 3 | Show 3 lines BEFORE and AFTER the match (context) |

---

## 4. COMBINING FLAGS — EXAMPLES
- Case-insensitive + line numbers:
`grep -in "error" logfile.txt`

- Recursive + case-insensitive + show filenames only:
`grep -ril "password"`

- Whole word + line numbers:`
grep -wn "admin" users.txt`

- Recursive + show line numbers + case-insensitive:
`grep -rni "failed login" /var/log/`

- Find lines that DON'T contain a word:
`grep -v "success" logfile.txt`

- Count how many times "error" appears:
`grep -c "error" logfile.txt`

---

## 5. HIDING ERRORS (USEFUL FOR PERMISSION DENIED MESSAGES)
When searching system folders, you get a lot of "Permission denied" errors cluttering the output.
Add this to the end of your command to hide them:
`2>/dev/null`
Example:
`grep -r "password" /etc/ 2>/dev/null`
This redirects error messages away so you only see real results.

---
## GREP FOR SOC / CYBERSECURITY WORK
These are patterns you will actually use:

- Search logs for failed logins:
`grep -i "failed" /var/log/auth.log`

- Search for a specific IP address:
`grep "192.168.1.100" access.log`

- Search for multiple terms using OR:
`grep -E "error|warning|critical" logfile.txt`

- Show 3 lines of context around each match:
`grep -C 3 "suspicious" logfile.txt`

- Find files containing the word "password" in a directory:
`grep -rl "password"`

- Search for lines starting with a specific word:
`grep "^ERROR" logfile.txt`

- Search for lines ending with a specific word:
`grep "failed$" logfile.txt`

The ^ means "starts with" and $ means "ends with".

---












  
