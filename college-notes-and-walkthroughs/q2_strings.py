print("Name: Syed Abdul Rauf\nID: 260121001\n\n")
#Store this line, replacing firstname with your first name and D with your
#digit: line = "Failed password for firstname from 10.0.0.D"

line = "Failed password for Syed from 10.0.0.1"
has_failed = False

# Use split() to print the username and the IP address on separate lines
list = line.split(' ')

for word in list:
    if word == 'Syed':
        print("Username: "+ word)
    if word == '10.0.0.1':
        print("IP: "+ word)

    
#Print the line in capital letters, print how many characters it has, and
#print True or False for whether it contains the word "Failed".

print(line.upper())
word_count = 0
for c in line:
    word_count+=1
print(f"The sentence has {word_count} characters.")
if "Failed" in list:
    has_failed = True
print(f"Contains 'Failed'? : {has_failed}")


