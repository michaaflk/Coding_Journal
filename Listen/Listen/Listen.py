
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







