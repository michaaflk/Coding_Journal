#Funktion Challenge by CodeCademy

def tenth_power(num):
    return num** 10

#print(tenth_power(1))
# 1 to the 10th power is 1
#print(tenth_power(0))
# 0 to the 10th power is 0
#print(tenth_power(2))
# 2 to the 10th power is 1024
#---------------------------------------

def square_root(num):
    return num ** 0.5

#print(square_root(16))
# should print 4
#print(square_root(100))
# should print 10
#------------------------------------------

def win_percentage(wins,losse):
  return wins / (wins + losse) * 100   
    
# Uncomment these function calls to test your win_percentage function:
#print(win_percentage(5, 5))
# should print 50
#print(win_percentage(10, 0))
# should print 100
#----------------------------------------

def average(num1,num2):
    return (num1 + num2) / 2

#print(average(1, 100))
# The average of 1 and 100 is 50.5
#print(average(1, -1))
# The average of 1 and -1 is 0
#---------------------------------------------

def remainder(num1, num2):
    return (num1 * 2) % (num2 / 2)
    
#print(remainder(15, 14))
# should print 2
#print(remainder(9, 6))
# should print 0