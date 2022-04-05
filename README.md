 zombieGmail

Using tkinter gui libary for window design.
Used .entry(Creates a small box that allows user input),made three entrys. 
One was for the person you wanted to gmail, another one was for the subject of the gmail. The next one was the main body of the gmail.

Used smtplib libary to send the messages,after reading documents and learning about it I created a function and got the user inputs, used the stmplib:

msg = MIMEText(body_of_email, 'html')
        msg['Subject'] = theSubject
        msg['From'] = sender
        msg['To'] = ','.join(receivers)
smtp = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
        smtp.login(user = sender, password = f" ")
        smtp.sendmail(sender, receivers, msg.as_string())
        smtp.quit()

theSubject,sender and receivers are variables for the user input.

A button was created to send the gmail using tkinter to call the gmail function.

After testing and making ure it worked, there were many problems with the .entry, .entry does not start at the left top right of it's box when typing. It starts in the 
middle and does not wrap. So I used the .Text, Text allowed me to still get user input and allowed wrap and started at the correct place.  

After testing again,  worked to add a start screen just for fun, the start screen so far holds a image background and one button the starts the main screen. 
A new button for settings may be added.


