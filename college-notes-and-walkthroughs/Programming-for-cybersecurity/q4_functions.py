print("Name: Syed Abdul Rauf\nID: 260121001\n\n")
D = 1


def check_length(password):
    if len(password) <= 8+D:
        return "Too Short"
    else:
        return "OK\n"
        
result = check_length("qwerty12434")
print(result)

def count_failed(lines):
    count = 0
    for line in lines:
        if "Failed" in line:
            count+=1
    return count
                
sample_logs = [
    "[INFO] 2026-11-14 09:00:01 - Server startup sequence initiated.",
    "[ERROR] 2026-11-14 09:05:12 - Database connection Failed: timeout after 30s.",
    "[WARN] 2026-11-14 09:10:45 - Memory usage reached 85% threshold.",
    "[ERROR] 2026-11-14 09:15:30 - User authentication Failed for ID: 4092.",
    "[ERROR] 2026-11-14 09:20:11 - Payment gateway sync Failed with status 503."
]
result_2 = count_failed(sample_logs)
print(f"Total failed lines: {result_2}")

while True:
    try:
        port_number = int(input("Enter a port Number: "))
        print(port_number)
        break
    except ValueError:
        print("ValueError: Enter a valid Port Number!")
