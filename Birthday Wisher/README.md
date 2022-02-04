# Guide to using this program

To use this program you'll need to make some changes in the code

## Main.py changes

- Find the smtp name for your email provider. For gmail it's "smtp.gmail.mail". Once you find out change the value at line 39. (If it's gmail then no need to change)
- Then change MY_EMAIL and PASSWORD variable to your email address and password one line 36 and 37 respectively
- Then make changes to `to_addrs` variable and set it to the address you want to send the mail to in line 42.

## birthdays.csv changes

- add name, email, birthyear, birthmonth and birthday of people in this csv file in the format `name,email,year,month,day`
