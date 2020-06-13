# author: Allyson Vasquez
# version: June.13.2020
# NOTES: Sending Email through SMTP Server

import smtplib

# create smtp obj with domain name + port num
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

print(smtpObj.ehlo())  # say hello to server

# start TLS encryption
print(smtpObj.starttls())

print('enter email')
user_email = input()
print('enter password')
user_pass = input()
print('enter recipient email')
recip_email = input()

smtpObj.login(user_email, user_pass)

smtpObj.sendmail(user_email, recip_email, 'Subject: Test.\nHello Email! From, Allyson <3')

smtpObj.quit()