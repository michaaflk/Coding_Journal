#CodeCademy List Chalenge Advanced with functions

#Define the function to accept one parameter
# for our starting number
#Calculate the numbers between the starting
# number and 100 while incrementing by 3
#Store the numbers in a list
#Return the list

def every_three_nums(start):
    return list(range(start, 101,3))

#Uncomment the line below when your function is done
#print(every_three_nums(91))
#--------------------------------------------------------

#Define the function to accept three parameters:
# the list, the starting index, and the ending index
#Get all elements before the starting index
#Get all elements after the ending index
#Combine the two partial lists into the result
#Return the result

def remove_middle(lst, start, end):
    return lst[:start] + lst[end+1:]
    
#Uncomment the line below when your function is done
#print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
#-----------------------------------------------------------

#Define the function to accept three parameters:
#the list, the first item, and the second item
#Count the number of times item1 shows up in our list
#Count the number of times item2 shows up in our list
#Return the item that appears more frequently in lst
# — if both items show up the same number of times, return item1

def more_frequent_item(lst, item1, item2):
    if lst.count(item1) >= lst.count(item2):
        return item1
    else:
        return item2
    
#Uncomment the line below when your function is done
#print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
#-------------------------------------------------------------


#Define the function to accept two parameters,
#one for the list and another for the index of
# the value we are going to double
#Test if the index is invalid.
# If it’s invalid then return the original list
#If the index is valid then get all values up
# to the index and store it as a new list
#Append the value at the index times 2 to the new list
#Add the rest of the list from the index onto the new list
#Return the new list

def double_index(lst, index):
    if index >= len(lst):
        return lst
    new_lst= lst[0:index]
    new_lst.append(lst[index]*2)
    new_lst = new_lst + lst[index+1:]
    return new_lst
    
#print(double_index([3, 8, -10, 12], 2))
#------------------------------------------------------------

#Define the function to accept one parameter
# for our list of numbers
#Determine if the length of the list is even or odd
#If the length is even, then return the average of
# the middle two numbers
#If the length is odd, then return the middle number
   
def middle_element(lst):
    if len(lst) % 2 == 0:
        sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2)-1]
        return sum / 2
    else:
        return lst[int(len(lst)/2)] 
    
#print(middle_element([5, 2, -10, -4, 4, 5]))