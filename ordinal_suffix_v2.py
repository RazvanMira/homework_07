number = int(input("Introduce a number: "))
str_number = str(number)
if number % 10 == 1:
    if number == 11:
        print("11th")
    else:
        print(str_number + "st")
elif number % 10 == 2:
    if number == 12:
        print("12th")
    else:
        print(str_number + "nd")
elif number % 10 == 3:
    if number == 13:
        print("13th")
    else:
        print(str_number + "rd")
else:
    print(str_number + "th")