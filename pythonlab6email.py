# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
# creates SMTP session
server = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
server.starttls()
 
# Authentication
server.login("sufiya.17cs@cmr.edu.in", "zubairahmed")
 
# message to be sent
message = "hi hello"
 
# sending the mail
server.sendmail("sufiya.17cs@cmr.edu.in", "sufiya.17cs@cmr.edu.in", message)
print("sss")
 
# terminating the session
server.quit()
