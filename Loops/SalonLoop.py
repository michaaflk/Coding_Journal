#CodeCademy Loop project

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

avg_text = "Average Haircut Price: "
rev_text = "Total Revenue: "

total_price = 0

#Reducing the Price by 5
new_prices = [new -5 for new in prices]
print(new_prices)
#Loop for total Price.
for price in new_prices:
    total_price += price
#get average price and print it.
average_price = total_price / len(new_prices)
print(avg_text + str(average_price))

total_revenue = 0
#Loop for revenue-
for i in range(len(hairstyles)):
    total_revenue += new_prices[i] * last_week[i]
print(rev_text + str(total_revenue))
#Get daylie revenue
average_daily_revenue = total_revenue / 7
#List comprehension to get Haicuts under 30 bucks.
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles[i])) if new_prices[i] < 30]
print(cuts_under_30)