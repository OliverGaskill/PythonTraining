#first_name = "Oliver"
#last_name = "Gaskill"
#full_name = first_name +" "+ last_name
#print("Hello "+full_name)


#age = 24
#age = age + 1
#print("Your age is : "+str(age))
#print(type(age))

#height = 183.5
#print("Your height is: "+str(height) +"cm")
#print(type(height))

#Human = True
#print("Are you a human: "+str(Human))
#print(type(Human))

#name = "Oliver"
#age = 24

#name, age,  = "Oliver", 24
#print(name)
#print(age)

#Spongebob = 30
#Patrick = 30
#Sandy = 30
#Squidward = 30

#Spongebob = Patrick = Sandy = Squidward = 30
#print(Spongebob)
#print(Patrick)
#print(Sandy)
#print(Squidward)

#name = "Oliver"
#print(len(name))
#print(name.find("e"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count())
#print(name.replace("l","a"))
#print(name*3)

#Type casting = convert data type of a value to another data type
#x = 1 #int
#y = 2.0 #float
#z = "3" #str

#x = str(x)
#y = float(y)
#z = float(z)

#print("x is "+x)
#print("y is "+str(y))
#print(z*3)

#User Input
#name = input("What is your name?:")
#age = int(input("How old are you?: "))
#height = float(input("How tall are you?: "))

#print("Hello "+name)
#print("You are "+str(age)+" years old")
#print("You are "+str(height)+"cm tall")

#import math
#from ftplib import parse227

#pi = 3.14
#x = 1
#y = 2
#z = 3

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(420))
#print(max(x,y,z))
#print(min(z,x,y))


#Slicing = Create a substring by extracting elements from another string
# Indexing[]        slice()
#   [start:stop:step]
#name = "Oliver Gaskill"

#first_name = name[0:6]
#last_name  = name[7:14]
#weird_name = name[2:8:2]
#reversed_name = name[::-1]

#print(reversed_name)
#print(first_name)
#print(last_name)
#print(weird_name)

# Slice()
#website = "https://google.com"
#website2 = "https://wikipedia.com"

#slice = slice(8,-4)
#print(website[slice])
#print(website2[slice])


# if statement = a block of code that will execute if it's condition is true
#age = int(input("How old are u?: "))

#if age == 100:
#    print("u are old")
#elif age >= 18:
#    print("You are an adult!")

#elif age < 0:
#   print("You haven't born yet")
#else:
#    print("You are a child!")


# Logical operators (and,or,not) = used to check if two or more conditional statements is true

#temp = int(input("What is the temp outside right now?:"))

#if not (temp >= 0 and temp <= 30):
#    print("the temp is bad")
#elif not (temp < 0 or temp > 30):
#    print("the temperature is good today")


# While loop = a statement that will execute it's block of code, as long as it's condition remains true

#name = ""

#while len(name) == 0:
#    name = input("Name?")

#print("Hello "+name)


# For loop = a statement that will execute it's block of code
#            a limited amount of times

#           while loop = unlimited
#           for loop = limited

#for i in range(10):
#    print(i+1)

#for i in range(50,100+1,2):
#    print(i)

#for i in "Oliver Gaskill":
#    print(i)


#import time

#for seconds in range(10,0,-1):
#    print(seconds)
#    time.sleep(1)
#print("Happy Year!")


# Nested loops = the "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"

#rows = int(input("How many rows?:"))
#columns = int(input("How manu columns:"))
#symbol = input("Enter symbol for use:")

#for i in range(rows):
#    for j in range(columns):
#        print(symbol, end="")
#    print()


# Loop control statements = change a loops execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iterations of the loop
# pass =        does nothing, acts as a placeholder


#while True:
#    name = input("Name:")
#    if name != "":
#        break

#phone_number = "123-456-789"

#for i in phone_number:
#    if i == "-":
#        continue
#    print(i,end="")


#for i in range(1,21):
#    if i == 13:
#        pass
#   else:
#        print(i)


# list = used to store multiple items in a single variable


#food = ["pizza","hamburger","kebab","meatballs"]

#food[0] = "sushi"

#food.append("ice cream")
#food.remove("hamburger")
#food.pop()
#food.insert(0,"cake")
#food.sort()
#food.clear()

#print(food[0])

#for x in food:
#    print(x)


# 2D = Lists = a list of lists

#drinks = ["coffe","soda","tea"]
#dinner = ["pizza","burger", "hotdog"]
#dessert = ["cake","ice cream"]

#food = [drinks,dinner,dessert]

#print(food[2][1])

# tuple = collection which is ordered and unchangeable, used to group together related data

#student = ("Oliver",24,"male")

#print(student.count("Oliver"))
#print(student.index("male"))

#for x in student:
#    print(x)

#if "Oliver" in student:
#    print("Oliver is here!")


# set = collection which unordered, unindexed. No duplicate values

#utensils = {"fork","spoon","knife"}
#dishes = {"bowl","plate","cup","knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)

#dinner_table = utensils.union(dishes)

#for x in dinner_table:
#    print(x)

#print(dishes.difference(utensils))

#print(utensils.intersection(dishes))


# dictionary = A changeable, unordered collection of unique key:value pairs, Fast because the use hashing, allow us to access a value quickly

#capitals = {'USA':'Washington DC',
#            'India':'New Dehli',
#            'China':'Beijing',
 #           'Russia':'Moscow'}

#capitals.update({'Germany':'Berlin'})
#capitals.update({'USA':'Las Vegas'})
#capitals.pop('China')
#capitals.clear()

#(capitals['Russia'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

#for key in capitals.items():
#    print(key)


1:47:20
