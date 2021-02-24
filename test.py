import sys
var1= "Hello"
var2= "enter Age only under 50"
var3= "you are eligible for driving"
var4= "you are not eligible for driving"
var5= "Sorry"
name= input("Enter the Driver name:- ")
age= int(input("Enter the age:- "))
if age >= 50:
    print (var1+" " + name.capitalize() +" " + var2)
elif age >= 18:
    print (var1 +" "+ name.capitalize() +" "+ var3)
else: 
    print (var5+ " "+ name.capitalize() +" "+ var4)

