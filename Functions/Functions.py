#Functions CheatSheet

#------------------------------------------------------------------------
current_budget = 3500.75
shirt_expense = 9


def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below:
def deduct_expense(budget, expense):
  return budget - expense 

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)
#---------------------------------------------------------------------
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)

#---------------------------------------------------------------------
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome("Michi")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(16.75)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin )
  print("And you are traveling to " + destination )
  print("You will be traveling by " + mode_of_transport )
  print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("Soltau", "Hannover", estimate)