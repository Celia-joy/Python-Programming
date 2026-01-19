print ("Hello World 🐱")
print("*" * 10)

# Declaring variables
students_count = 1000 
rating = 4.99
is_published  = True
course_name = "   python  programming  "
first = "Celia"
last = "Joy"
full = first + "" + last
full = f"{first} {last}"
total_of_full = f"{len(first) + (2 + 1)}"
total_of_full1 = f"{len(first)} + {2 + 1}"

# Putting to lowercase and uppercase a string
course_name1 = course_name.upper()
course_name2 = course_name.lower()
course_name3 = course_name.title()
print(course_name)
print(len(course_name))

# how to see where a character is
print(course_name[0])
print(course_name[1])
print(course_name[2])
print(course_name[3])
print(course_name[4])
print(course_name[5])
print(course_name[6])
print(course_name[7])
print(course_name[8])
print(course_name[9])
print(course_name[10])
print(course_name[11])
print(course_name[12])
print(course_name[13])
print(course_name[14])
print(course_name[15])
print(course_name[16])
print(course_name[17])
print(course_name[18])
print(course_name[19])
print(course_name[20])
print(course_name[21])
print(course_name[1:-7])
print("Student's count is " + str(students_count))
print(course_name1)
print(course_name2)
print(course_name3)
print(course_name.rstrip())
print(full)
print(total_of_full)
print(total_of_full1)

# Finding an index of a character or a sequence of characters in the 
print(course_name.find("gra"))

# Replacing a character by another 
print(course_name.replace("g" , "j"))

# Checking if the character or a sequence of characters are in the variable name 
print("pyt" in course_name)
print("swift" not in course_name)
print("swift" in course_name)

#Types of data types:
#primitive and complex
#primitive: numbers, strings and booleans
#complex: range, 

# types of numbers there is floats
x = 1.1
# integers
y = 2
#complex numbers there are in this form: a + bi
z = 1 + 2j

print(x)
print(y)
print(z)

# Some operations in python

print (4 + 2)
print (4 - 2)
print (4 * 2)
print (4 / 2)
print (4 // 2)
print (4 % 2)
print (4 ** 2)

a = 10
a += 3
# Is the same as a = a+3
print(a)

import math

#Rounding numbers
print( round (49.9))
print( round (49.3))

#Knowing the absolute value of a number
print(abs(-49.9))
print(abs(-49.3))

print(math.ceil(49.3))

# Type conversion
x = input(" x: ")
y = int(x) + 5
z = bool(0)
a = bool(67)
print(f" x: {x}, y: {y}" )
print(z)
print(a)

# There is not only int float bool str
# Others are self explanatorial but let's talk about
# bool
  #Falsy statement
   #0
   #"":(empty strings)
   #none
  #True statement
   #Others are true except the above  

#Comparison operators
 # <,>, ==, !=

comp1= 10 > 3
comp2= 10 < 3
comp3= 10 == 3
comp4= 10 != 3
comp5= 10 >= 3
comp6= 10 <= 3
comp7= 10 == "10"
comp8= 10 != "10"
comp9= "cat" > "elephant"
comp10= "cat" == "CAT"
print(comp1)
print(comp2)
print(comp3)
print(comp4)
print(comp5)
print(comp6)
print(comp7)
print(comp8)
print(comp9)
print(comp10)

# Conditional statements
temperature = input("temperature:")
temperature = int(temperature)
if temperature == 25:
    print("The temperature is normal")
    print("But you must try drinking water")
elif temperature > 25: 
    print("The temperature is high")
    print(" You must absolutely try drinking water")   
else: 
    print("It is cold")
    print("Put on a sweater and jogging") 

age = input(" age: ")
age = int(age)
message = "You are allowed vote" if age >= 18 else "You can't vote"
print(message)

#logical operators
# and or not
high_income = True
good_credit = True
student = False
if high_income and good_credit:
    print("eligible")
else:
    print("Not eligible")
if high_income or good_credit:
    print("eligible")
else:
    print("Not eligible")
if high_income and good_credit and not student:
    print("eligible")
else:
    print("Not eligible")
if 18 <= age <= 65: 
    print("You are an adult")
 
#Loops
#for loops
for number in range (1, 6):
    print(" For Loops", number, (number) * ".")

# 1. Get input and convert it to lowercase for reliable comparison
user_response = input("Did you succeed (yes/no)? ").lower() 

for number in range(5):
     if user_response == 'yes':
        print("good job")    
     elif user_response == 'no': 
        print("Hardworking is the key to success")    
     else:
        print("Invalid input. Please try again.")
print("Loop finished.") 

# Nested loops
for x in range(5):
    for y in range(3):
        print(f" x: {x}, y: {y} ")

#Iterable
for x in "Python":
    print(x)
for y in [1,2,3,4]:
    print(y)

#While loops
number= input("number=")
number = int(number)
while number > 0:
    print(number)
    number //=2

command= input("command=")
command= str(command)
while command.lower() != "Quit":
    print("Your wish is a command to us", command)
    break

#Exercise 
#Program that prints even number between 1 and 10


for number in range(1,10):
    if number % 2 == 0:
        print(number)
print(f"We have 4 even numbers")

#functions and arguments
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome to programming with Python")


greet("Celia", "Joy")
greet("MUGWANEZA", "Rick")
#The difference between greet() and  print("Hi there") is that print can take an input where as greet can't
#Two types of function
#Those who perform a task like print()
#Those who return a value like round()

def greeting(first_name, last_name):
    return f"Hi {first_name} {last_name}"


message = greeting("Celia", "Joy")
print(message)

def increment(number,by):
    return number + by


result = increment(2,8)
print(result)   

def multiply(*numbers):
    total = 1
    for number in numbers:
        total*= number
    return total


print(multiply(2,3,4,5))
