import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "testerforudemy@gmail.com"
MY_PASSWORD = "bggdztaqxeuioasa"

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()

        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Hey, Happy Birthday!!\n\n{contents}")

# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
