import tkinter

window = tkinter.Tk()
window.title ("Login Form")
window.geometry ('600x400')
window.configure(bg='#D3D3D3')

frame = tkinter.Frame(bg='#D3D3D3')

login_label = tkinter.Label(frame, text='Login', bg='#333333', fg='#EEEDEB', font=("Arial", 30))

User_label = tkinter.Label(frame, text='Username', bg='#333333', fg='#EEEDEB', font=("Arial", 16))
User_entry = tkinter.Entry(frame,font=("Arial", 14))

Password_label = tkinter.Label(frame, text="Password", bg='#333333', fg='#EEEDEB', font=("Arial", 16))
Password_entry = tkinter.Entry(frame, show="*", font=("Arial", 14)) 

login_button = tkinter.Button(frame, text="Login", bg='#333333', fg='#EEEDEB', font=("Arial", 16))


login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
User_label.grid(row=1, column=0, padx=15)
User_entry.grid(row=1, column=1, pady=20)
Password_label.grid(row=2, column=0, padx=15)
Password_entry.grid(row=2, column=1, pady=20)                               
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
   