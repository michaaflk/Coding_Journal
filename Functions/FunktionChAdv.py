#Math Funktion Advanced by CodeCademy


def first_three_multiples(num):
    print(num)
    print(num * 2)
    print(num * 3)
    return num *3

# Uncomment these function calls to test your first_three_multiples function:
#first_three_multiples(10)
# should print 10, 20, 30, and return 30
#first_three_multiples(0)
# should print 0, 0, 0, and return 0
#--------------------------------------------

def tip(total,percentage):
    return (total * percentage) / 100

#print(tip(10, 25))
# should print 2.5
#print(tip(0, 100))
# should print 0.0
#---------------------------------------------

def introduction(first_name, last_name):
    return last_name + ", " + first_name + " " + last_name

#print(introduction("James", "Bond"))
# should print Bond, James Bond
#print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou
#-----------------------------------------------------------

def dog_years(name, age):
    return name + ", you are " + str(age*7) + " years old in dog years"

#print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
#print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

def lots_of_math(a, b, c, d):
    plus = a + b
    minus = c - d
    multi = plus * minus
    print(plus)
    print(minus)
    print(multi)
    return multi % a

print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0