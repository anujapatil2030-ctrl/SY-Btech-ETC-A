# accept marks of six students ,sort them and print
"""
marks = []

i=0
while i<6 :
   f1=input("Enter the marks")
   marks.append(f1)
   i=i+1
print("list: ",marks)
marks.sort()
print("list: ",marks)   here it is string hence it sorts based on only starting number
if it is 11 3 65 111 222 445
--> 11 111 222 3 444 65
"""

marks = []
i=0
while i<6 :
   f1=int(input("Enter the marks"))
   marks.append(f1)
   i=i+1
print("list: ",marks)
marks.sort()
print("list: ",marks)

# ctr+f2 --> we can change same variable/string(here marks) in code 