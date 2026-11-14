print("Name: Syed Abdul Rauf\nID: 260121001\n\n")
D = 1
#Ask the user to type a CVSS score (use float(input(...))) and print its
#severity: Critical (9.0 or more), High (7.0 or more), Medium (4.0 or
#more), otherwise Low. Run it with three different scores.

cvss_score = float(input("Enter CVSS Score: "))

if cvss_score >= 9.0:
    print("Critical\n")
elif cvss_score >= 7.0:
    print("High\n")
elif cvss_score >= 4.0:
    print("Medium\n")
else:
    print("Low\n")
    
list = [21, 22, 80, 443, 2000 + D]
for port in list:
    if port < 1024:
        print(f"Well Known {port}\n")
    else:
        print(f"registered {port}\n")


count = D+3
while count > 1:
    count -=1
    print(count)
print("Done")
