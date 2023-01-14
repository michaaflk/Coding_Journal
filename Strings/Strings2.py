#Next Artikle in CodeCademy

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(",")

author_last_names = []
for i in author_names:
    author_last_names.append(i.split()[-1])
  
print(author_last_names)

#-----------------------------------------------------------------------

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for i in love_maybe_lines:
  love_maybe_lines_stripped.append(i.strip())
  
love_maybe_full = "\n".join(love_maybe_lines_stripped)

print(love_maybe_full)

#-----------------------------------------------------------

def poem_title_card(title, poet):
  return "The poem \"{}\" is written by {}.".format(title,poet)

poem_title_card("I Hear America Singing", "Walt Whitman")

#-------------------------------------------------------------

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

poem_description(publishing_date, author, title, original_work)

my_beard_description = poem_description(publishing_date, author, title, original_work)


#Over this lesson you’ve learned:

#.upper(), .title(), and .lower() adjust the casing of your string.
#.split() takes a string and creates a list of substrings.
#.join() takes a list of strings and creates a string.
#.strip() cleans off whitespace, or other noise from the beginning and end of a string.
#.replace() replaces all instances of a character/string in a string with another character/string.
#.find() searches a string for a character/string and returns the index value that character/string is found at.
#.format() allows you to interpolate a string with variables.

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(",")

highlighted_poems_stripped = []
for i in highlighted_poems_list:
  highlighted_poems_stripped.append(i.strip())

highlighted_poems_details = []
for n in highlighted_poems_stripped:
  highlighted_poems_details.append(n.split(":"))

titles = []
poets = []
dates = []
for p in highlighted_poems_details:
    titles.append(p[0])
    poets.append(p[1])
    dates.append(p[2])
    
for f in range(0, len(highlighted_poems_details)):
    print("The poem {} was published by {} in {}.".format(titles[f], poets[f], dates[f]))
