#String Cheatsheet
first_name = "Abe"
last_name = "Simpson"
#first_name = "Julie"
#last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name

new_account = account_generator(first_name, last_name)

#print(new_account)
#------------------------------------------------------------------

def password_generator(first_name, last_name):
    temp_password= first_name[-3:] + last_name[-3:]
    return temp_password

temp_password = password_generator(first_name,last_name)

#print(temp_password)

#--------------------------------------------------------------
#same len()
def get_length(name):
  count = 0
  for i in name:
    count += 1
  return count

#-------------------------------------------------------------

def letter_check(word, letter):
  for i in word:
    if i == letter:
      return True
  return False

#--------------------------------------------------------

def contains(big_string, little_string):
  if little_string in big_string:
      return True
  return False
  
#print(contains("watermelon", "melon"))

def common_letters(string_one, string_two):
  common = []
  for i in string_one:
      if i in string_two and not i in common:
          common.append(i)
  return common       
  
#print(common_letters("banana", "cream"))


def username_generator(first_name, last_name):
    global user_name
    user_name = first_name[:3] + last_name[:4]
    return user_name
    
print(username_generator(first_name,last_name))

#user_name = username_generator(first_name, last_name)

def password_generator(user_name):
    global password
    password = ""
    for i in range(0,len(user_name)):
        password += user_name[i-1]
    return password

print(password_generator(user_name))

print(password)
    
    
    