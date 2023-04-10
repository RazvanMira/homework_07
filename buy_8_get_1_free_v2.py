number_of_coffees = int(input("How many coffees did the customer buy?\n"))
price_per_coffee = int(input("The price per coffee is: "))
total_cost = 0
total_cost = (number_of_coffees * price_per_coffee) - (number_of_coffees // 9 * price_per_coffee)
print("The total cost for", number_of_coffees, "coffees is", total_cost)