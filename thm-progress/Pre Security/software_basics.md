# Topic 4: Software Basics
## Data Representation
Computers process data purely through electrical on/off states represented as binary:
- Bit: The smallest unit of data (0 or 1).
- Byte: 8 bits. Can represent 2^8 = 256$ distinct values (0 to 255).
- Hexadecimal (Base 16): Uses characters 0-9 and A-F. Represents bytes cleanly: 1 byte = 2 hex digits (e.g., binary 11111111 equals decimal 255 and hex 0xFF). Common in memory addresses and shellcode.

## Data Encoding
Encoding converts human data into defined formats for reliable processing, storage, and transmission across systems.
- ASCII: 7-bit character encoding mapping numbers to characters (e.g., decimal 65 is 'A').
- UTF-8: Variable-length unicode encoding supporting global character sets and symbols.
- Base64: Encodes binary data into 64 printable ASCII characters. Frequently used in email attachments and web authentication headers.
  - Important Distinction: Encoding is not encryption. Encoding is publicly reversible without a key; encryption requires a secret key to decrypt.

## Python & A Simple Demo
Python is a readable, versatile scripting language widely used in cybersecurity for automated tooling, port scanning, and exploit development.
