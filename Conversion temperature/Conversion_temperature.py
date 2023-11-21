def con_temp(number, conversion):
    if conversion == "CtoF":
        return (number*1.8)+32
    elif conversion == "FtoC":
        return (number-32)*(5/9)

def convert_age(age):
    days = age*365
    hours = days * 24
    return days, hours

print(con_temp(32, "CtoF"))
print(con_temp(100,"FtoC"))

days, hours = convert_age(16.8)
print(days)
print(hours)