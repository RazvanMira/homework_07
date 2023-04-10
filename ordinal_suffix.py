number = int(input("Introduce a number: "))
str_number = str(number)
print(str_number)
list_number = list(str_number)
print(list_number)
if list_number[-1] == str(1):
    print(str_number + "st")
elif list_number[-1] == str(2):
    print(str_number + "nd")
elif list_number[-1] == str(3):
    print(str_number + "rd")
else:
    print(str_number + "th")