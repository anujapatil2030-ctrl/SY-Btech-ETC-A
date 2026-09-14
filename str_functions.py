# len()
"""
  this returns the length of the string
  i.e it gives us the number of characters in the string  
"""
name = "Anuja"
print(len(name))           # output = 5

# varible.endswith(<"Sub_String">)
"""
   chech if the string ends with the sub string
   if yes: it returns True
   else  : it returns False
"""
print(name.endswith("ja"))

# varible.startswith(<"Sub_String">)
"""
   chech if the string starts with the sub string
   if yes: it returns True
   else  : it returns False
"""
print(name.endswith("An"))

# variable.capitalize()
"""
    makes the 1st character of the string capital
    ex."anuja" -> Anuja
       "Anuja" -> Anuja
       " anuja" -> anuja
"""
name=" anuja"
name="anuja"
print(name.capitalize())

# variable.title()
"""
  makes first letter of each word capital
"""
Title = "anuja sanjay patil  "
print(Title.title())

# variable.count(<"character">)
"""
  counts the total number of occurance of any character
"""
print(Title.count("a"))

# variable.find(word)
"""
    returns the index of 1st occurance of the word in the string
"""
print(Title.find("sanjay"))

# variable.replace(old word,new word)
"""
    replaces old word with new word in the new string ,the first string remains as it is (no changes in it)
"""
n = Title.replace("anuja","snehal")
print(n)

# variable.center(width.fillchar)
print(n.center(len(n),"#"))