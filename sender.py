# NOTE: Some of the current Anaconda software does not support the encryption done by the starttls command.
# Therefore, you must use conda install python=3.7.1=h33f27b4_4 to downgrade from 3.7.3-h8c8aaf0_0 in order to rectify this problem.

# Import necessary modules and packages
import pandas as pd
from smtplib import SMTP

# Read the Excel file (NOTE: The information given is not real)
emailList = pd.read_excel("email-list.xlsx")

# Grab all data from the Excel file
emails = emailList["Email"]
firstNames = emailList["Recipient First Name"]
lastNames = emailList["Recipient Last Name"]

# Configure SMTP
s = SMTP("smtp.gmail.com", 587)
s.starttls()
s.ehlo()

# Get login information
senderEmail = input("What email address should the messages be sent from? ")
senderPassword = input("What is the password for the above email address? ")

# Login using the input information
s.login(senderEmail, senderPassword)

# Read the subject to be sent to all email addresses in the Excel file
sbjFile = open("subject.txt", "r")
sbj = sbjFile.read()

# Read the message to be sent to all email addresses in the Excel file
msgFile = open("message.txt", "r")
msg = msgFile.read()

# Begin sending messages
for i in range(len(emails)):
    # Edit the message with information from the Excel file
    msgWithFullName = msg.replace("fullName", "%s %s" % (firstNames[i], lastNames[i]))
    msgFull = msgWithFullName.replace("name", firstNames[i])

    # Edit the subject with information from the Excel file
    sbjWithFullName = sbj.replace("fullName", "%s %s" % (firstNames[i], lastNames[i]))
    sbjFull = sbjWithFullName.replace("name", firstNames[i])

    # Send the email
    s.sendmail(senderEmail, emails[i], "Subject: %s\n%s" % (sbj, msgFull))
    print("Sent email to %s %s at %s." % (firstNames[i], lastNames[i], emails[i]))

# Terminate connection once email sending has completed and close files
s.quit()
msgFile.close()
sbjFile.close()
