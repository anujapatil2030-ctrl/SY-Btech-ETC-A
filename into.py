#three ways to write string 

"""
imaportant
string is immutable(i.e we cannot change existing string)
"""

a='Anuja'    #Single Qoated string
b="Anuja"    #double qouated string
c='''Anuja''' #triple Qoated string

#---------------------------------------------
#String slicing  (we can get part of a string)
#---------------------------------------------
name = "Anuja"

"""
    "A  n  u  j  a
     0  1  2  3  4
    -5 -4 -3 -2 -1
"""
a=len(name)    #gives the length of the string

nameshort =   name[0:3]  #starts from 0 index all the wat till 3 ( excluding 3)

"""
   syntax for slicing
      variable = variable(string that we have to slice) [index of string to start from : index of string befor which we have to stop]
"""

character1=name[1]       #prints only 1 character
print(nameshort)
print(character1)

#if we press alt at any line , with the help of arrow we can move the line up or down