#yourway sandWITCH

availableToppings = ["Onion", "Paprika", "Tomato", "Chicken", "Alpinos", "Teriyaki Sauce"]
print("Available Toppings List : ")
for i in range(len(availableToppings)) : print(i+1, availableToppings[i], sep=' : ')
selectedToppings = [availableToppings[int(x)-1] for x in input("Select any 3 Toppings using comma separator: ")
    .split(',')]
print("Toppings selected are :")
for i in selectedToppings: print(i)
#pizzaCost = 5
#menge = int(input("How many Pizzas ? "))
print("Your total is {} euros!".format(5*int(input("How many Pizzas? "))))


"""
greeting = print("Hello,this is MyWay Sandwiches.\nWe offer sandwiches with the following toppings:\n    - onions, lettuce, tomoto, olives, peppers, tomotoes.")
print(type(greeting) = print("Please choose three of the above. \nEnter your choice in one row, separated by comma:")
choice_1 = input()
"""choice = (x for x in input().split(","))
print(choice)"""
thx = print("Thank you")
num_sand_gues = print("How many sandwiches would you like?")
num_quest_answ = int(input())
total = 5 * num_quest_answ
print(f"You bill is {total}.\nThanks for visiting\nHave a nice day!")
"""