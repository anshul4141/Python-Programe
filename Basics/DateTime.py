import datetime

x = datetime.datetime.now()
print("current date and time:", x)
print("month:", x.strftime("%B"))
print("day:", x.strftime("%A"))
print("year:", x.strftime("%Y"))
print("local date:", x.strftime("%D"))

print("------------------")

dob = datetime.datetime(2002, 1, 25)
print("dob:", dob)
print("day of dob:", dob.strftime("%A"))
print("month of dob:", dob.strftime("%B"))
print("year of dob:", dob.strftime("%Y"))
print("local date of dob:", dob.strftime("%D"))