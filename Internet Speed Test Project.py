#import speedtest module using "pip install speedtest-cli" command in terminal

from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_best_server()
    down = str(round(sp.download()/(10**6), 3))+" Mbps"
    up = str(round(sp.upload()/(10**6), 3))+" Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title(" Internet Speed Test ")
sp.geometry("500x650")
sp.config(bg="Yellow")

lab = Label(sp,text="Internet Speed Test", font=("Times New Roman",30, "bold"), bg="Yellow", fg="Black")
lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp,text="Download Speed", font=("Times New Roman",30, "bold"))
lab.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp,text="00", font=("Times New Roman",30, "bold"))
lab_down.place(x=60, y=200, height=50, width=380)

lab = Label(sp,text="Upload Speed", font=("Times New Roman",30, "bold"))
lab.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp,text="00", font=("Times New Roman",30, "bold"))
lab_up.place(x=60, y=360, height=50, width=380)

button = Button(sp,text="GO", font=("Times New Roman",30, "bold"), relief=RAISED, bg="Green", command=speedcheck, activeforeground="Purple", activebackground="Sky Blue")
button.place(x=20, y=500, height=50, width=100)

lab = Label(sp,text="Click on Go to check the internet speed", font=("Times New Roman",15), bg="Yellow", fg="Black")
lab.place(x=60, y=620, height=25, width=380)

sp.mainloop()
