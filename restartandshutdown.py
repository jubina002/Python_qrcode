from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logOut():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()
st.title(" Shutdown")
st.geometry("500x500")
st.config(bg = "plum")

r_button = Button(st, text="Restart", font=("Times New Roman", 30, "bold"),
                  relief = RAISED, cursor="plus", command = restart) 
r_button.place(x=150, y=60, height=50, width= 200)

rt_button = Button(st, text="Restart Time", font=("Times New Roman", 20, "bold"), 
                   relief = RAISED, cursor="plus", command = restart_time)
rt_button.place(x=150, y=170, height=50, width= 200)

lg_button = Button(st, text="LogOut", font=("Times New Roman", 30, "bold"), 
                   relief = RAISED, cursor="plus", command = logOut)
lg_button.place(x=150, y=270, height=50, width= 200)

st_button = Button(st, text="ShutDown", font=("Times New Roman", 27, "bold"),
                    relief = RAISED, cursor="plus", command=shutdown)
st_button.place(x=150, y=370, height=50, width= 200)
st.mainloop()