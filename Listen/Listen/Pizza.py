#Len´s Pizza Slice

#toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
#price = [2, 6, 1, 3, 2, 7, 2]
#num_two_dollar_slices = price.count(2)
#num_pizzas = len(toppings)

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"],
                    [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

#sorting toppings by price
toppings = sorted(pizza_and_prices)
#storing the cheapest pizza in a value
cheapest_pizza = toppings[0]
#storing the priciest pizza in a value
priciest_pizza = toppings[-1]
#removing the priciest pizza from the list
toppings.pop(-1)
#adding a new topping
toppings.insert(4, [2.5, "peppers"])
#slicing the list in to the three cheapest pizza toppings
three_cheapest = toppings[:3]

print(three_cheapest)