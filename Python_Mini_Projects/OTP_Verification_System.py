import os
import math
import random
import smtplib

digits = "0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]

msg= OTP + " is your OTP"

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
# Mail id & Password.
s.login("Enter Your mail id ", "password")
emailid = input("Enter your email: ")
s.sendmail("ashishbapat01@gmail.com",emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")