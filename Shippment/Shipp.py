#This Programm will evaluate witch shipping is the chepest for the Customer.

costg = "Ground Shipping Total:"
costd = "Drone Shipping Total:"
#Promt user for Weight
weight = float(input("Weight:"))
#Flat Charge
fc = 20
#Flat Charge Premium
fcp= "Ground shipping Premium: 125€"
#Pricing for Ground
price1 = 1.50
price2 = 3.0
price3 = 4
price4 = 4.75
#ground standard pricing
ground1 = (weight * price1) + fc
ground2 = (weight * price2) + fc
ground3 = (weight * price3) + fc
ground4 = (weight * price4) + fc
#drone pricing
drone1 = (weight * (price1 * 3))
drone2 = (weight * (price2 * 3))
drone3 = (weight * (price3 * 3))
drone4 = (weight * (price4 * 3))

#Ground Shipping
if weight <= 2:
    print(costg + str(ground1) + "€")
elif weight >2 and weight <= 6:
    print(costg + str(ground2) + "€")
elif weight >6 and weight <= 10:
     print(costg + str(ground3) + "€")
elif weight >= 10:
    print(costg + str(ground4) + "€")

print(fcp)

#Drone Shipping
if weight <= 2:
    print(costd + str(drone1) + "€")
elif weight >2 and weight <= 6:
    print(costd + str(drone2) + "€")
elif weight >6 and weight <= 10:
     print(costd + str(drone3) + "€")
elif weight >= 10:
    print(costd + str(drone4) + "€")