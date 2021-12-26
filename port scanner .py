
import sys
import socket
import tkinter 
from tkinter import messagebox



main=tkinter.Tk()
  
def error(text):
        messagebox.showerror("Error",f"{text}")
def resultbox(text):
        messagebox.showinfo("port scanner",f"{text}")

 

def check(): # function to chek the ip 
    list=[21, 22, 23, 25, 50, 51, 53, 67, 68, 69, 80, 110, 119, 123, 135, 136, 137, 138, 139, 143, 161, 162, 189, 344, 433, 443, 545, 989, 990, 2121, 3389, 8888]
    target=targett.get()
    
    if len(target)==0:
            error("please enter the ip ")
        
    try:
        
        # will scan ports between 1 to 65,535
        for port in list:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            # returns an error indicator
            result = s.connect_ex((target,port))
            if result ==0:
                resultbox("Port {} is open".format(port))
            s.close()
        

    except KeyboardInterrupt:
            error(" Exiting Program !!!!")
            sys.exit()
    except socket.gaierror:
            error("Hostname Could Not Be Resolved !!!!")
            sys.exit()
    except socket.error:
            error("Server not responding !!!!")
            sys.exit()







# design GUI
targett=tkinter.StringVar()
main.title("port scanner")
main.resizable(False,False)
main.geometry("200x200")
lbl1=tkinter.Label(text=" Enter the ip ",width=20).grid(row=0,column=0,pady=20)
ent1=tkinter.Entry(textvariable=targett).grid(row=1,columnspan=2,pady=20,padx=30)
btn1=tkinter.Button(text="check",command=check).grid(row=2,columnspan=2)



main.mainloop()