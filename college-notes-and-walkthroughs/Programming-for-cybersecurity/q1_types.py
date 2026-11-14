print("Name: Syed Abdul Rauf\nID: 260121001\n\n")
#Create these variables and print each one together with its type(): your
#name (str), your port number 2000 + D (int), a CVSS score of your choice
#with a decimal point (float), and is_patched (bool).

D = 1

name = 'Syed'
port_number = 2000
cvss_score = 7.8
is_patched = True

port_number += D

print(f"\nName: {name}              Type:{type(name)}")
print(f"Port Number: {port_number}       Type:{type(port_number)}")
print(f"CVSS Score: {cvss_score}         Type:{type(cvss_score)}")
print(f"Status: {is_patched}            Type:{type(is_patched)}\n")



#Create a list of three port numbers that includes your port, and a
#dictionary for a server with the keys "ip", "os" and "owner" (use your
#name as the owner). Print the first port in the list and the server owner.

port_list = [port_number, 443, 80, {'ip':'192.168.10.1', 'os':'Windows', 'owner':'Syed'}]
first_port = port_list[0]
owner = port_list[3]['owner']

print(f"Port Number: {first_port} | Owner: {owner}")


#Convert the text "8080" to a number, add D to it and print the result

string = "8080" 
integer = int(string)
print(f"String {string} converted to integer {integer+D}")
