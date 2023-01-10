#CodeCademy List Challenge Optional

def append_size(lst):
    lst.append(len(lst))
    return lst
    
#Uncomment the line below when your function is done
#print(append_size([23, 42, 108]))
#----------------------------------------------------

#Define the function to accept one parameter for our list of numbers
#Add the last and second to last elements from our list together
#Append the calculated value to the end of our list.
#Repeat steps 2 and 3 two more times
#Return the modified list

def append_sum(lst):
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    return lst
    
#Uncomment the line below when your function is done
#print(append_sum([1, 1, 2]))
#-----------------------------------------------------

#Define the function to accept two parameters for our two lists of numbers
#Check if the length of the first list is greater than or equal to the length of the second list
#If true, then return the last element from the first list.
#Otherwise, return the last element from the second list

def larger_list(lst1, lst2):
    if len(lst1) > len(lst2):
        return lst1[-1]
    if len(lst1) < len(lst2):
        return lst2[-1]
    return lst1[-1]
        
#Uncomment the line below when your function is done
#print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
#------------------------------------------------------

#Define the function to accept three parameters, a list of numbers,
# a number to look for, and a number for the number of instances
# #Count the number of occurrences of item (the second parameter)
# in lst (the first parameter)
# #If the number of occurrences is greater than n
# (the third parameter), return True. Otherwise, return False

def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    return False
    
#Uncomment the line below when your function is done
#print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
#-------------------------------------------------------

#Define the function to accept two parameters, one for each list.
#Combine the two lists together
#Sort the result
#Return the sorted and combined list

def combine_sort(lst1, lst2):
    return sorted(lst1 + lst2)
    
#Uncomment the line below when your function is done
#print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))