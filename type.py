a = 31
print(type(a))   # class <int>

a="Anuja"
print(type(a))   # class <str>

a=3.12
print(type(a))   # class <float>

"""
   type is used to identify the data types of the variables
"""

# conversion of datatypes (typecasting)

a="31.23"
print(type(a))
b=float(a)   # but a should be float
print(type(b))

print(int("31"))