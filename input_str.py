# Problem 1:
# input your name
name = input("Enter your name:")

# f string
print(f"Hi, {name}")             # name variable name

print("hi "+name+ " how are you?")   #concatination

# Problem 2:
# input the date
letter =''' Dear <|Name|>,
you are selecte....!
<|Date|> '''

print(letter.replace("<|Name|>","Anuja").replace("<|Date|>","28 sep 2026"))  #chaining
"""
first it replace name in new string,and in that new string again it replaces date
"""

# Problem 3: to detect douple space
name = "Anuja  Sanjay Patil"
print(name.find("  "))  # return -1 if subtring not found ,else it returns starting indext of substring

# Problem 4:
# replace double space by single space
print(name.replace("  "," ")) 
print(name)  # string is immutable which means we cannot change string by opereating any functions on it


# Problem 5:
n = "Dear Anuja,\n\tYou are selected...!\n\tThank you!"
print(n)