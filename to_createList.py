# list is container used  to store set  values of any data type
friends = ["Apple","Orange",5,345.06,False,"Akash","Rohan"]
print(friends[0])

friends[0] = "grapes"
print(friends[0])   #unlike strings List are mutable

# index of list
"""
   "Apple", "Orange",  5,  345.06,  False,  "Akash",  "Rohan"
     0         1       2      3        4       5         6
     -7       -6       -5     -4       -3      -2        -1
"""


# slicing of list
print(friends[1:4])