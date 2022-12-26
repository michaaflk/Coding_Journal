#Ep4

print("Hello, welcome to Kings`s coffee!")

name = input("What ist your name?\n")

print("Hello " + name +  ", thank you so much for coming in today!\n")

menu = "Black Coffee, Espressp, Latte, Cappuchino"

print(name + ", what would you like from our menu today? Here is what we are serving.\n\n" + menu)

order = input()

price = 8

menge = input("How many coffees would you like?\n")

total = price * int(menge)

print("Thank you. Your total is: " + str(total) + "Euro\n")

print("Sounds good " + name + ", we`ll have your " + menge + " " + order + " ready for you in a moment.")