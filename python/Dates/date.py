import datetime

x = datetime.datetime.now()
print(x)

# Creating Date Objects


x = datetime.datetime(2020, 5, 17)

print(x)
# The strftime() Method


x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))