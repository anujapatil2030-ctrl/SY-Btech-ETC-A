a = input("\nEnter no 1:")
b = input("\nEnter no 2:")
print("Number 1 is ",a)
print("Number 2 is ",b)
print("\nSum is ",a+b)
"""
   here input is taken as string and not as int
   hence when we try to add both numbers which are basically 2 different strings
   it gets concatinated 
   ie when we have to concatinate strings i will write it as
   "Anuja"+"Patil"-->> AnujaPatil
   *Same hapens here instead of adding 1&2 and returning result as 3 ,it returns result as 12
"""
# to avoid this we have to use the typecasting
a = int(input("\nEnter no 1:"))
b = int(input("\nEnter no 2:"))
print("Number 1 is ",a)
print("Number 2 is ",b)
print("\nSum is ",a+b)    # here we will get the correct result

# to determine the type of inputed value
a=input("\nEnter the value of a:")
print(type(a))       # here the type will be str