# dann wollen wir mal anfangen

# Coffe shop by NetworkChuck
# Robot Barista


print("Hello, welcome to Kings`s coffee!")


name = input("What ist your name?\n")

#Weil man den Ben`s einfach nicht trauen kann! Tabea kam dazu!
if name == "Lena" or name == "Tabea" or name == "Loki":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "yes" and good_deeds < 4:
         print("Get the hell out of here!")
         exit()
    else:
     print("Hello " + name + ", thank you so much for coming in today!\n")
      
else:
    print("Hello " + name + ", thank you so much for coming in today!\n")


#Coffee menu
menu = "Black Coffee, Espresso, Latte, Cappuchino"

print(name + ", what would you like from our menu today? Here is what we are serving.\n\n" + menu)

order = input()

menge = input("How many " + order + " would you like?\n")

if order == "Black Coffee":
    price = 2
elif order == "Espresso":
    price = 3
elif order == "Latte":
    price = 4
elif order == "Cappuchino":
    price = 4.5

total = price * int(menge)


print("Sounds good " + name + ", we`ll have your " + menge + " " + order + " ready for you in a moment." + "Your total is: " + str(total) + "Euro")

