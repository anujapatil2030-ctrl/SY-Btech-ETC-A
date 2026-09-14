name = "Anuja"
print(name[-4 : -1])    # not in practical programming only for interview
print(name[1 : 4])      #positive index corresponding to the negative index


#Advance slicing technique
print(name[:4])   # is same as print(name[0:4])
print(name[1:])   # is same as print(name[1:5])


#slicing with skip value
"""
  syntax
     variable = varible[start_index : end_index : jump_value]
"""

print(name[0:5:2])    # output = Aua