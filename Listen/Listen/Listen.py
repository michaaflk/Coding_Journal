
#Listen erstellen und bearbeiten



camping_list = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]

camp_site = ["Crytal Lake", 404, False, 95.5, 10]

#camping_list.append("toilet papper")
#camping_list.append("bidet")

camping_list.extend(["toilet paper", "bidet"])

#camping_list = camping_list + ["toilet paper", "bidet"]

#camping_list.insert(0, "bidet")
#camping_list.insert(-1, "toilet paper")

#camping_list.remove("tent")
#camping_list.remove("sleeping bags")

print("Removed: " + camping_list.pop(0)) #tent removed
print("Removed: " + camping_list.pop(0)) #sleeping bags removed




print(camping_list)

#Updated List cheatsheet
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
first = inventory[1]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)
inventory.insert(10, "19th Century Bed Frame")
inventory = sorted(inventory)

print(inventory)







