python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index = 0

while index < length:
  print("I am learning about " + python_topics[index])
  index += 1



  dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("they have the dog I want!")
    break


sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
  print(location)
  for i in location:
    scoops_sold += i
print(scoops_sold)



grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [num + 10 for num in grades]

print(scaled_grades)




heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [i for i in heights if i > 161]
print(can_ride_coaster)




single_digits = range(10)
squares = []

for i in single_digits:
  print(i)
  squares.append(i**2)
  
print(squares)

cubes = [num**3 for num in single_digits]
print(cubes)
