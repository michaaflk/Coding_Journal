#Loop Chalelenge by CodeCademy

#Define the function to accept one input parameter called nums
#Initialize a counter to 0
#Loop through every number in nums
#Within the loop, if any of the numbers are divisible by 10, increment our counter
#Return the final counter value

def divisible_by_ten(num):
    count = 0
    for i in num:
        if (i % 10 == 0):
            count += 1
    return count
        
#Uncomment the line below when your function is done
#print(divisible_by_ten([20, 25, 30, 35, 40]))
#-------------------------------------------------------------

#Define the function to accept a list of strings
# as a single parameter called names
#Create a new list of strings
#Loop through each name in names
#Within the loop, concatenate 'Hello, ' and
# the current name together and append this new string
# to the new list of strings
#Afterwards, return the new list of strings

def add_greetings(names):
    greet = 'Hello, '
    name = []
    for n in names:
        name.append(greet + n)
    return name
    
#Uncomment the line below when your function is done
#print(add_greetings(["Owen", "Max", "Sophie"]))
#----------------------------------------------------------

#Define our function to accept a single input parameter
# lst which is a list of numbers
#Loop through every number in the list if there are
# still numbers in the list and if we haven’t hit an odd number yet
#Within the loop, if the first number in the list is even,
# then remove the first number of the list
#Once we hit an odd number or we run out of numbers,
# return the modified 

def delete_starting_evens(lst):
    while (len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1:]
    return lst
        
#Uncomment the lines below when your function is done
#print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
#print(delete_starting_evens([4, 8, 10]))
#--------------------------------------------------------

#Define the function header to accept one input which
# will be our list of numbers
#Create a new list which will hold our values to return
#Iterate through every odd index until the end of the list
#Within the loop, get the element at the current odd
# index and append it to our new list
#Return the list of elements which we got from the odd indices.

def odd_indices(lst):
    new_list =[]
    for i in range(1, len(lst), 2):
        new_list.append(lst[i])
    return new_list
    
#Uncomment the line below when your function is done
#print(odd_indices([4, 3, 7, 10, 11, -2]))
#--------------------------------------------------------------

#Define the function to accept two lists of numbers,
# bases and powers
#Create a new list that will contain our answers
#Create a loop that iterates through every base in bases
#Within that loop, create another loop that iterates
# through every power in power
#Within that nested loop, append the result of the current
# base raised to the current power.
#After all iterations of both loops are complete,
# return the list of answers

def exponents(base, power):
    result = []
    for i in base:
        for n in power:
         result.append(i ** n)
    return result             
    
#print(exponents([2, 3, 4], [1, 2, 3]))
