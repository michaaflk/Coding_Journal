user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({'theLooper': 138475, 'strinQueen': 85739})
print(user_ids)
#-----------------------------------------------------

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {k:v for k, v in zipped_drinks}

print(drinks_to_caffeine)
#--------------------------------------------------------------

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {k:v for k,v in zip(songs,playcounts)}
plays["Purple Haze"] = 1
plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
#-----------------------------------------------------------------

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"],
                   "fire": ["Aries", "Leo", "Sagittarius"],
                   "earth": ["Taurus", "Virgo", "Capricorn"],
                   "air":["Gemini", "Libra", "Aquarius"],}

zodiac_elements["energy"] = "Not a Zodiac element"

key_to_check = "energy"

if key_to_check in zodiac_elements:
  print(zodiac_elements["energy"])
  
#--------------------------------------------------
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level["matcha"] = 30

try:
  print(caffeine_level["matcha"])
except KeyError:
  print("Unknown Caffeine Level")
#-------------------------------------------------------------------------

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112,
            "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)
#-----------------------------------------------------------------------------  
available_items = {"health potion": 10, "cake of the cure": 5,
                   "green elixir": 20, "strength sandwich": 25,
                   "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)


print(available_items)
print(health_points)
#----------------------------------------------------------------------------------
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112,
            "lyleLoop": 102931, "keysmithKeith": 129384}

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22,
                 "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)
#----------------------------------------------------------------------------------

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15,
                 "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0
for list in num_exercises.values():
  total_exercises += list

print(total_exercises)
#------------------------------------------------------------------------
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58,
                           "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for key, value in pct_women_in_occupation.items():
  print("Women make up " + str(value) + " percent of " + key + "s")

#------------------------------------------------------------------------
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress",
         4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot",
         8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice",
         12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil",
         16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement",
         21:	"The World", 22: "The Fool"}

spread = {}
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for key, value in spread.items():
  print("Your " + key + " is the " + value + " card.")
  #-------------------------------------------------------------------------------------------------