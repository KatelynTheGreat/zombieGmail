from email import message
import tkinter as tk
from smtplib import SMTP
import smtplib, ssl
from email.mime.text import MIMEText
from tkinter import *
import os



root= tk.Tk()
root.title("Zombie Apocalypse Gmail")
photo = PhotoImage(file = "Untitled-2.png")
root.iconphoto(False, photo)
root.config(cursor="plus")
root.resizable(False, False)
canvas = tk.Canvas(root, width = 500, height = 400)
canvas.pack()

startbgimage = PhotoImage(file="bgzomb.png")
background_label = tk.Label(image=startbgimage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



def startprogram():
    startButton.after(10,startButton.destroy)
    background_label.after(10,background_label.destroy)
    canvas.config(bg="black")

    Gmailentry = tk.Text (root,width=40,height=1.5)
    canvas.create_window(250, 70, window=Gmailentry)
    Gmailentry.config(bg="gray")

    entry = tk.Text (root,height=6, width=40) 
    canvas.create_window(250, 260, window=entry)
    entry.config(bg="gray")

    subjectline = tk.Text(root,height=1.5, width=40)
    canvas.create_window(250,148,window=subjectline)
    subjectline.config(bg="gray")

    gmailtext = tk.Label(root,text = "Gmail Here:")
    canvas.create_window(250,30, window=gmailtext)
    gmailtext.config(font=('Fixedsys',20),foreground="red",bg="black")

    Subjecttext = tk.Label(root,text = "Subject Here:")
    canvas.create_window(250,110, window=Subjecttext,width=400)
    Subjecttext.config(font=('Fixedsys',20),foreground="red",bg="black")

    Bodytext = tk.Label(root,text = "Body Here:")
    canvas.create_window(250,190, window=Bodytext,width=400)
    Bodytext.config(font=('Fixedsys',20),foreground="red",bg="black")

    def playing ():  
        userinput = entry.get("1.0","end")
        gUserinput = Gmailentry.get("1.0","end")
        theSubject = subjectline.get("1.0","end")

        sender = 'zombieapocalypsesends@gmail.com'
        receivers = [gUserinput]
        body_of_email = userinput

        msg = MIMEText(body_of_email, 'html')
        msg['Subject'] = theSubject
        msg['From'] = sender
        msg['To'] = ','.join(receivers)

        smtp = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
        smtp.login(user = sender, password = f"Tardis{3663}")
        smtp.sendmail(sender, receivers, msg.as_string())
        smtp.quit()
        #bottomtext = tk.Label(root,text = f"Message will be sent to {gUserinput}")
        #canvas.create_window(250,530, window=bottomtext)

    button = tk.Button(text='Send Message', command=playing)
    canvas.create_window(250, 360, window=button)


startButton = tk.Button(text='Start', command=startprogram)
canvas.create_window(250, 200, window=startButton)
startButton.config(width=20, height=3)

root.mainloop()

