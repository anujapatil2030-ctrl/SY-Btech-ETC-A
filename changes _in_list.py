friends = ["Apple","Orange",5,345.06,False,"Akash","Rohan"]
print(friends)

# variable.append("string") -> adds string at the end of list in same list not new list is created
friends.append("Anuja")
print(friends)

#variable.sort()
n=[45,67,1,8,278,3,9]
n.sort()
print(n)

#variable.reverse()
n=[45,67,1,8,278,3,9]
n.reverse()
print(n)


#variable.insert(index,object)
n=[45,67,1,8,278,3,9]
n.insert(3,999)
print(n)


#variable.pop()  -> removes perticular value and returns its value
n=[45,67,1,8,278,3,9]
print(n.pop(3))      #returns the index of value to be removed
print(n)

#variable.remove(value)  -> removes perticular value 
n=[45,67,1,8,278,3,9]
n.remove(45)
print(n)