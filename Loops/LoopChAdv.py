#CodeCademy Loop Chalelenge Advanced

def larger_sum(lst1,lst2):
    sum1 = 0
    sum2 = 0
    for i in lst1:
        sum1 += i
    for i in lst2:
        sum2 += i
    if sum1 >= sum2:
        return lst1
    else:
        return lst2

#Uncomment the line below when your function is done
#print(larger_sum([1, 9, 5], [2, 3, 7]))
#-------------------------------------------------------

def over_nine_thousand(lst):
    sum = 0
    for i in lst:
        sum += i
        if sum > 9000:
            break
    return sum
    
#Uncomment the line below when your function is done
#print(over_nine_thousand([8000, 900, 120, 5000]))
#----------------------------------------------------------

def max_num(nums):
    maximum = nums[0]
    for i in nums:
        if i > maximum:
            maximum = i
    return maximum
    
#print(max_num([50, -10, 0, 75, 20]))
#-------------------------------------------------------------

def same_values(lst1, lst2):
    index = []
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            index.append(i)
    return index
            
#print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
#--------------------------------------------------------------

def reversed_list(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] != lst2[len(lst2) - 1 - i]:
            return False
    return True
    
    
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
            
        