print("nerdy pie")

#this is a comment nerd you dont need to worry about the compiler
#variables 
name ="red bean paste"
num=13
print(name)
print(num)

#update variable/redefine a variable
num=4
print(num)
#operators(+-*/)
x=2
y=21
print(x+y)
# string concatenation
word="panda"
word2="express"
space=" "
print(word + space + word2 + " is a restaurant")
# assign multiple variables 
x, y, z = 1, 2, "three"
print(x, y, z) 
# data types
#string 
text="this is a string"
#integer
wholenum=19
#float
decimalnum=98.6
#list/arrays
mylist=[1,2,4,"string somthing", [11,22,33],19.333]
#boolean 
output=True
# dictionary/object
carobject={
    "make": "Toyota",
    "model": "Camry",
    "year": 2020,
    "color": {
        "contrast": "black",
        "main": "white",
        "accent": "red"},
        "list": [1, 2, 3, 4, 5]
}
print(carobject.get('color').get('main'))
print(carobject['color']['main'])
print(carobject['list'][0])
#indexing
myarray=[20,15,30,14.66,87]
floatnum=myarray[3]
print(floatnum)
makewhole=int(floatnum)
print(makewhole)
#assinment operators
a=2
b=5
a+=b 
# this means a=a+b
print(a)
# lets create our first function
#the basic syntax for a function for python is:
def myfunction():
    print("this is a function")

#create a scenario. lets make a function that converts celsius to fahrenheit!
def converter(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit

temp=input("what is the temperature in celsius? ")
convtemp=int(temp)
tempinfahrenheit=converter(convtemp)
print(tempinfahrenheit)
#conditionals
a=12
b=18
if a > b:
    print("a is greater than b")
elif a < b:
    print("b is greater than a")
else:
    print("a is equal to b")

#challenge - create a condidtional that would work for a game of rock paper scissors
#challenge2 - create 2 variables that would collect an input: user choice and opponent choice
#challenge3 - update the conditional to run a rps game on the choices/imputs
#bonus challenge - learn about the built-in random madule to enhance your game 
choice=("rock", "paper", "sissors")
rock = "rock"
paper = "paper"
sissors = "sissors"
user_choice= input("what is your choice? (rock, paper, sissors) ")  
oponent_choice=choice(["rock", "paper", "sissors"])
if user_choice == oponent_choice:
    print("its a tie!") 
elif user_choice == rock and oponent_choice == sissors:
    print("you win!")
elif user_choice == rock and oponent_choice == paper:
    print("you lose!")
elif user_choice == paper and oponent_choice == rock:
    print("you win!")
elif user_choice == paper and oponent_choice == sissors:
    print("you lose!")
elif user_choice == sissors and oponent_choice == paper:
    print("you win!")
elif user_choice == sissors and oponent_choice == rock:
    print("you lose!")


