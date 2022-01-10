#import ibm_db
import random
import sched
import subprocess
import time
from datetime import date
from tkinter import *
import matplotlib.pyplot as plt

import mysql.connector
import numpy as np
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
def Listen():
    
    q=[]
    while(1):	

        try:
            with sr.Microphone() as source2:

                r.adjust_for_ambient_noise(source2, duration=0.2)

                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                if "stop" in MyText:
                    SpeakText("Assistank stopped")
                    break
                if "refresh" in MyText:
                    refresh()
                if ("veda" in MyText or "weather" in MyText ) and "2021" in MyText:#== "show reports of veda 2020":
                    SpeakText("Showing reports of Vetha")
                    dispgraph("vetha","2021")
                    continue
                if ("dat" in MyText or "dad" in MyText ) and "2021" in MyText:#== "show reports of veda 2020":
                    SpeakText("Showing reports of dad")
                    dispgraph("dad","2021")
                    continue
                if ("mom" in MyText or "p" in MyText ) and "2021" in MyText:#== "show reports of veda 2020":
                    SpeakText("Showing reports of mom")
                    dispgraph("mom","2021")
                    continue
                if ("tv" in MyText or "dv" in MyText ) and "2021" in MyText:#== "show reports of veda 2020":
                    SpeakText("Showing reports of tv")
                    dispgraph("tv","2021")
                if ("veda" in MyText or "weather" in MyText ) and "2020" in MyText:#== "show reports of veda 2020":
                    SpeakText("Showing reports of Vetha")
                    dispgraph("vetha","2020")
                    continue
                if ("dat" in MyText or "dad" in MyText ) and "2020" in MyText:#== "show reports of veda 2020":
                    SpeakText("Showing reports of dad")
                    dispgraph("dad","2020")
                    continue
                if ("mom" in MyText or "p" in MyText ) and "2020" in MyText:#== "show reports of veda 2020":
                    SpeakText("Showing reports of mom")
                    dispgraph("mom","2020")
                    continue
                if ("tv" in MyText or "dv" in MyText ) and "2020" in MyText:#== "show reports of veda 2020":
                    SpeakText("Showing reports of tv")
                    dispgraph("tv","2020")
                    
                print(MyText)
                SpeakText(MyText)
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occured")


def SpeakText(command):

	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

mydb = mysql.connector.connect(
  host="sql6.freemysqlhosting.net",
  user="sql6464330",
  password="gkEzXRg4Ip",database="sql6464330"
)
mycursor = mydb.cursor()

from datetime import date, timedelta

'''
n=["Vetha","Dad","Mom","Server","TV"]
today = date.today()
# today = date.today()
for i in range(365+365):
    yesterday = timedelta(-i)
    d = today.strftime("%d/%m/%Y")
    k=today+yesterday
    p=k.strftime("%d/%m/%Y")
    print(p)
    for u in n:
        k=random.choice(["1","0"])
        mycursor.execute('INSERT INTO data (Date,name,Details) VALUES ("{}","{}","{}");'.format(p,u,k))
        mydb.commit()


exit()
'''
#mycursor.execute("CREATE TABLE data (Date VARCHAR(255), name VARCHAR(255),Details VARCHAR(255))")
#mycursor.execute('INSERT INTO mapping (ip,mac,name) VALUES ("192.168.1.1","7C:A9:6B:E8:B1:FC","Server");')
#mycursor.execute('INSERT INTO mapping (ip,mac,name) VALUES ("192.168.1.2","6E:CE:26:D9:E7:F1","Mom");')
#mycursor.execute('INSERT INTO mapping (ip,mac,name) VALUES ("192.168.1.3","04:92:26:A3:8F:DF","Vetha");')
#mycursor.execute('INSERT INTO mapping (ip,mac,name) VALUES ("192.168.1.4","48:46:C1:85:AB:DE","TV");')
#mycursor.execute('INSERT INTO mapping (ip,mac,name) VALUES ("192.168.1.6","F6:54:15:AE:FC:B3","Dad");')


def current_attendence(mac):
    mycursor.execute('SELECT * FROM mapping')
    #mydb.commit()
    out=[]
    current_students = mycursor.fetchall()
    for i in current_students:
        out+=[list(i)]
    for ele in out:
        if mac in ele:
            name = ele[-1]
    return name
    
def login(username,password):
    mycursor.execute('SELECT * FROM details')
    o=[]
    curr = mycursor.fetchall()
    for i in curr:
        o+=[list(i)]
    for ele in o:
        if [username,password] == ele:
            loginframe.grid_forget()
            mainframe.grid()
            return 1
    messagebox.showerror("Error","Invalid credentials")
    return 0



def do_something(): 
    
    output = str(subprocess.run(["nmap", "-sP","192.168.1.1/24"], capture_output=True))
    sliced =output.split()
    #print(sliced)
    ip=[];mac=[]
    for i in range(len(sliced)):
        if sliced[i] == "for":
            ip+=[sliced[i+1]]
        elif sliced[i]=="Address:":
            mac+=[sliced[i+1]]
    #print(sliced[1:])
    for i in range(len(ip)):
        ip[i]=ip[i][:11].split()[0]
        #mac[i]=mac[i].split()[1]
    ip=ip[:-1]
    return ip,mac



def graph(name,month,year):
    mycursor.execute('SELECT name,Details,date FROM data where name="{}" and date like "%{}" and date like "%/{}/%";'.format(name,year,month))
    o=[];p=[]
    curr = mycursor.fetchall()
    for i in curr:
        o+=[list(i)]
        p+=[int(i[1])]
    if o==[]:
        messagebox.showerror("showerror", "Invalid student name")
        exit()
    return sum(p)
    
def dispgraph(name,year):
    l=[]
    y=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    for i in "01 02 03 04 05 06 07 08 09 10 11 12".split():
        l+=[graph(name,i,year)]
    fig = plt.figure(figsize = (10, 5))

    plt.bar(y, l, color ='maroon',width = 0.4)
 
    plt.xlabel("Months")
    plt.ylabel("DAYS")  
    plt.title("Report of " +name + " " + year)
    plt.show()
    
    

def win():
    
    newWindow = Toplevel(root)
    newWindow.title("Graph Generator")
    name=Label(newWindow,text="Name :",font=("Times", "24", "bold italic"),bg="black",foreground = 'white')
    year=Label(newWindow,text="Year",font=("Times", "24", "bold italic"),bg="black",foreground = 'white')
    #Label(newWindow,text ="This is a new window").pack()

    
    uname=Entry(newWindow,font=("Times", "24", "bold italic"),bg="#cfccc6")
    pw=Entry(newWindow,font=("Times", "24", "bold italic"),bg="#cfccc6")

    gra = Button(newWindow,text="Submit",font=("Times", "24", "bold italic"),command=lambda :dispgraph(uname.get(),pw.get()),bg="black",foreground = 'white')
    nl=Label(newWindow,text="GRAPH GENERATOR :",font=("Times", "24", "bold italic"),bg="black",foreground = 'white')

    nl.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
    name.grid(row=1,column=0,padx=10,pady=10)
    year.grid(row=2,column=0,padx=10,pady=10)
    uname.grid(row=1,column=1,padx=10,pady=10)
    pw.grid(row=2,column=1,padx=10,pady=10)
    gra.grid(row=3,column=0,padx=10,pady=10)

    
    


def refresh():
    current_class.delete(0,END)
    mylistbox.delete(0,END)

    ip,mac=do_something()
    print(ip,mac)
    present=[]

    for i in mac:
        present+=[current_attendence(i)]

    absent=[]
    for i in whol_mac:
        y=current_attendence(i)
        if y not in present:
            absent+=[y]

    
    today = date.today()
    d = today.strftime("%d/%m/%Y")
    for name in present:
        mycursor.execute('INSERT INTO data (Date,name,Details) VALUES ("{}","{}","{}");'.format(d,name,"1"))
        mydb.commit()

    for name in absent:
        mycursor.execute('INSERT INTO data (Date,name,Details) VALUES ("{}","{}","{}");'.format(d,name,"0"))
        mydb.commit()


    print(present,absent)

    for i in present:
        current_class.insert(END,i)
        #current_class.insert(END,"world0")

    for i in absent:
        mylistbox.insert(END,i)
        #current_class.insert(END,"world0")


graph("vetha","01","2020")



root=Tk()
#root.geometry("600x400")
#root.iconphoto('C:\Users\vetha\Desktop\logo.png')
root.title("WIFI ATTENTENCE SYSTEM")
loginframe=Frame(root)
#loginframe.config(bg='#8705a1')
loginframe.grid()

username=Label(loginframe,text="UserName",font=("Times", "24", "bold italic"),bg="black",foreground = 'white')
password=Label(loginframe,text="Password",font=("Times", "24", "bold italic"),bg="black",foreground = 'white')

uname=Entry(loginframe,font=("Times", "24", "bold italic"),bg="#cfccc6")
pw=Entry(loginframe,show="*",font=("Times", "24", "bold italic"),bg="#cfccc6")

pgeobutton = Button(loginframe,text="login",font=("Times", "24", "bold italic"),command =lambda :login(uname.get(),pw.get()),bg="black",foreground = 'white')

mainframe=Frame(root)

gra = Button(mainframe,text="Graph",font=("Times", "24", "bold italic"),command=win,bg="black",foreground = 'white')
voice = Button(mainframe,text="Assistant",font=("Times", "24", "bold italic"),command=Listen,bg="black",foreground = 'white')


gra.grid(row=4,columnspan=2,column=3,padx=10,pady=10)
voice.grid(row=4,column=1,padx=10,pady=10)



present_label=Label(mainframe,text="IN CLASS",font=("Times", "24", "bold italic"),bg="black",foreground = 'white')
absent_label=Label(mainframe,text="NOT IN CLASS",font=("Times", "24", "bold italic"),bg="black",foreground = 'white')

present_label.grid(row=0,column=0,padx=10,pady=10)
absent_label.grid(row=0,column=1,padx=10,pady=10)

butt = Button(mainframe,text="Refresh",font=("Times", "24", "bold italic"),command=refresh,bg="black",foreground = 'white')

butt.grid(row=2,column=0,columnspan=3,padx=10,pady=10)

current_class = Listbox(mainframe,font=("Times", "24", "bold italic"),bg="#cfccc6")
current_class.grid(row=1,column=0,padx=10,pady=10)


mylistbox = Listbox(mainframe,font=("Times", "24", "bold italic"),bg="#cfccc6")
mylistbox.grid(row=1,column=1,padx=10,pady=10)

wholeip=["192.168.1.1","192.168.1.2","192.168.1.3","192.168.1.4","192.168.1.6"]
whol_mac=["7C:A9:6B:E8:B1:FC","6E:CE:26:D9:E7:F1","04:92:26:A3:8F:DF","48:46:C1:85:AB:DE","F6:54:15:AE:FC:B3"]



username.grid(row=0,column=0,padx=10,pady=10)
password.grid(row=1,column=0,padx=10,pady=10)
uname.grid(row=0,column=1,padx=10,pady=10)
pw.grid(row=1,column=1,padx=10,pady=10)
pgeobutton.grid(row=2,column=1,padx=10,pady=10)



mainloop()





