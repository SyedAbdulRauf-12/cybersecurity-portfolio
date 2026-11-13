# Static aint always noise
<details><summary>Click to reveal flag </summary>
<b>Flag: academy{d15a5m_t34s3r_fac3431a}</b>
</details>

## Summary
It was a pretty straight forward challenge. It tests the challengers ability to search through binary files to find the flag.

## Recon / Initial Analysis

- Checked the content of the binary file.
- Cant run grep or find through binary files.
- Will return only Binary matched.
- Need to find the correct command to find the flag.

## Solution
- wget the files.
- Display content.
- Use the `strings <filename> | grep "academy"` command.
-   strings will extract the readable content from the binary file and pipe it to grep command.
- Flag will be extracted.

## Lessons Learned
Binary files cannot be read normally. We need to extract the readable content and then display it.
