#!/usr/bin/python

# Now, that we know the importing of the .NET dll works, try out a real application

import clr
dll = clr.FindAssembly('MyMath')  # returns path to dll
assembly = clr.AddReference('MyMath')
#print(type(assembly)) # <class 'System.Reflection.RuntimeAssembly'>
#print(dir(assembly))
from MyMath import MyMathClass
from MyMath import MyMathClass as My

print("Adding two numbers using a dot net dll library")
print("Enter the first integer")
addend1 = input()
print("Enter the second integer")
addend2 = input()

print("The sum of",  addend1,  " and",  addend2, " is => ",  My.addInts(addend1, addend2))
