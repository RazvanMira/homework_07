print("The programme ends when you press Enter.")
numbers_list = []
more_numbers = True
while more_numbers:
    number = input("Introduce a number: ")
    if number == "":
        more_numbers = False
    else: 
        number = int(number)
        numbers_list.append(number)
print(numbers_list)
print(max(numbers_list))
print(min(numbers_list))