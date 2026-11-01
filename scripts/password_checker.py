import tkinter as tk

window = tk.Tk()
window.title("LoginTest")
window.geometry("400x500")

def handle_submit():
    user = input_boxx.get()
    password = password_input.get()
    
    if  (user.strip() == "") and (len(user)<=5):
        output_label1.config(text="Enter USERNAME!!")
    else:
        output_label1.config(text="Valid Username")
        
    def validate_string(p):
        has_upper = any(c.isupper() for c in p)
        has_lower = any(c.islower() for c in p)
        has_digit = any(c.isdigit() for c in p)
        has_symbol = any(not c.isalnum() and not c.isspace() for c in p)
        
        return has_upper and has_lower and has_digit and has_symbol
    VSP = validate_string(password)
    if (VSP) and (len(password) >= 8): 
        output_label2.config(text="Password is Strong!")
    else:
        output_label2.config(text="Password is missing a few requirements or is too short.\n Please make sure to fulfill all requirements")
        
    
        
Head = tk.Label(window, text = "<--- Welcome to Login Tester! --->\nThis application simulates a login screen to check\nif your password is strong enough!", font=("Times New Roman", 12))
Head.grid(row=0, columnspan=2, padx=10, pady=10)

username_display = tk.Label(window, text = "Enter your Username", font=("Times New Roman", 12))
username_display.grid(row=1, column=0, padx=10, pady=10)

input_boxx = tk.Entry(window, font=("Times New Roman", 8))
input_boxx.grid(row=1, column=1, padx=10, pady=10)

password_display = tk.Label(window, text = "Enter your password", font=("Times New Roman", 12))
password_display.grid(row=2, column=0, padx=10, pady=10)

password_input = tk.Entry(window, show="*")
password_input.grid(row=2, column=1, padx=10, pady=10)

submit_btn = tk.Button(window, text="Submit", command=handle_submit)
submit_btn.grid(row=3, column=0, columnspan=2)

output_label1 = tk.Label(window, text="", font=("Times New Roman", 10))
output_label1.grid(row=4,column=0, columnspan=2, padx=10, pady=10)

output_label2 = tk.Label(window, text="", font=("Times New Roman", 10))
output_label2.grid(row=5,column=0, columnspan=2, padx=10, pady=10)

Req_label = tk.Label(window, text="Password requirements:\n->Has combination OF UPPER, lowercase, digits and symbols!", font=("Times New Roman", 10))
Req_label.grid(row=6,column=0, columnspan=2, padx=10, pady=10)

window.mainloop()