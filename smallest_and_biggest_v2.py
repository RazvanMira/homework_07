min_ = 9999
max_ = 0

while True:
    user_input = input("Please type input a number: ")
    if user_input == "":
        break
    user_number = int(user_input)
    
    if user_number < min_:
        min_ = user_number
    
    if user_number > max_:
        max_ = user_number

print("Min:", min_)
print("Max:", max_)