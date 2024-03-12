import datetime as dt
user_day = input("Enter the day of your birth: ")
user_month = input("Enter the month of your birth: ")
user_year = input("Enter the year of your birth: ")
try:
    user_dob = dt.datetime.strptime(
        f"{user_day}/{user_month}/{user_year}", "%d/%m/%Y").date()
except ValueError:
    print("Wrong input")
else:
    today = dt.date.today()
    age = today.year - user_dob.year - ((today.month, today.day) < (user_dob.month, user_dob.day))

    print(age)