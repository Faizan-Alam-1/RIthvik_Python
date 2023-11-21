from tkinter import *


win  = Tk()
win.title("Password strength checker")

def check_strength_pass(password):
    min_length  = 9
    pass_Uppercase =  any(c.isupper() for c in password)
    pass_lowercase =  any(c.islower() for c in password)
    pass_num_val = any(c.isdigit() for c in password)

    if len(password) < min_length or not  pass_Uppercase or not pass_lowercase or not pass_num_val :
        return "Weak"
    else:
        return "Strong"

def check_pass():
   
  
   password =  entry_pass.get()
   strength = check_strength_pass(password)
   print(strength)
   pass_Label.config(text=f"{  strength}")
  




# creat entry widget

entry_Label = Label(win ,  text="Enter you password")
entry_Label.pack(pady=0)

entry_pass = Entry(win , show="*")
entry_pass.pack(pady=10)



# creat the button

check_btn  =  Button(win ,  text="Check my password" ,  command= check_pass)
check_btn.pack(pady=10)


pass_Label= Label(win ,  text=f"PASWORD")
pass_Label.pack(pady=0)




win.mainloop()