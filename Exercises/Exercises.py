# # 4. List (ordered, mutable, allows duplicates)
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]


# # 3. Boolean
# is_student = True

# # 2. String
# name = "Alice"


# # 1. Numbers
# float_num = 7.89
# int_num = 10
# complex_num = 3 + 4j

# # 5. Tuple (ordered, immutable, allows duplicates)
# coordinates = (10.0, 20.0)
# # 6. Set (unordered, mutable, no duplicates)
# unique_numbers = {1, 2, 3, 4, 5}
# # 7. Dictionary (unordered, mutable, key-value pairs)
# person = {"name": "Bob", "age": 30, "city": "New York"}

# import math

# point1 = (int(input("Enter x1: ")), int(input("Enter y1: ")))
# point2 = (int(input("Enter x2: ")), int(input("Enter y2: ")))

# distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
# print("Straight line distance:", distance)

# length = math.trunc(distance)
# print("Truncated distance:", length)

# print (input("Press any keyto exit..."))
# print("Goodbye!")


# name = input("Enter your name: ")
# last_name = input("Enter your last name: ")
# country = input("Enter your country: ")
# age = int(input("Enter your age: "))

# print("Hello " + name + " " + last_name + ", you are " + str(age) + " years old and you live in " + country + ".") 

# print(website[slice])

# import math
# radius = float(input("Enter the radius of the circle: "))

# area_of_circle = math.pi * radius ** 2

# print ("The area of the circle with radius", radius, "is:", area_of_circle)

# age = int(25) 
# height = float(185.5)
# complex_number = complex(2, 3)

# Area of triangle
# base = int(input("Enter the base of the triangle: "))
# height = int(input("Enter the height of the triangle: "))
# area = 0.5 * base * height
# print("The area of the triangle is:", area)


#Perimeter of triangle
# side_a = int(input("Enter side a of the triangle: "))
# side_b = int(input("Enter side b of the triangle: "))
# side_c = int(input("Enter side c of the triangle: "))
# perimeter = side_a + side_b + side_c
# print("The perimeter of the triangle is:", perimeter)


# #Area and Perimeter of rectangle
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area = length * width
# perimeter = 2 * (length + width)
# print("The area of the rectangle is:", area)
# print("The perimeter of the rectangle is:", perimeter)

# Radius of circle
# radius = float(input("Enter the radius of the circle: "))
# pi = 3.14159
# area = pi * radius ** 2
# circumference = 2 * pi * radius
# print("The area of the circle is:", area)
# print("The circumference of the circle is:", circumference)

# Slope 
# import math
# slope1 = 2
# b = -2 
# x_intercept = -b / slope1

# print("Slope (m1):", slope1)
# print("Y-Intercept (b):", b)
# print("X-Intercept:", x_intercept)

# # Euclidean distance between two points
# x1, y1 = 2, 2
# x2, y2 = 6, 10
# slope2 = (y2 - y1) / (x2 - x1)
# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# print("Slope (m2):", slope2)
# print("Euclidean Distance:", distance) 

# # Compare the slopes
# if slope1 > slope2:
#     print("Slope1 is greater than Slope2")
# elif slope1 < slope2:
#     print("Slope1 is less than Slope2")
# else:
#     print("Slope1 is equal to Slope2")  


# Calculate the value of y
# x = int(input("Enter the value of x: ")) 
# y = x**2 + 6*x + 9
# if x == -3:
#     print("The value of y is: 0")
# else: print("Wrong value of y:", y)

# Length of 'python' and 'dragon'
# str1 = "python"
# str2 = "dragon"
# len_str1 = len(str1)
# len_str2 = len(str2)
# print("Length of 'python':", len_str1)
# print("Length of 'dragon':", len_str2)
# are_equal = len_str1 == len_str2
# print("Are the lengths equal?", are_equal)

# Check if 'on' is in both 'python' and 'dragon'
# print('on' in str1 and 'on' in str2)

# Check if 'jargon' is in the sentence
# sentence = "I hope this course is not full of jargon."
# print('jargon' in sentence)

# No "no" in dragon and python
# print('on' not in "dragon" and 'on' not in "python")

# find the length of the text and convert the length to float and then to string
# text = "Python is a popular programming language."
# length = len(text)
# length_float = float(length)
# length_str = str(length_float)
# print ("Lenght:", length)
# print ("As float:", length_float)
# print("Length as string:", length_str)

# Even 
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(4))  # True
# print(is_even(7))  # False

# Check if floor division of 7 by 3 is equal to int conversion of 2.7
# result = (7 // 3) == int(2.7)
# print(result)  # True

# Check if type of '10' is equal to type of 10
# result = type('10') == type(10)
# print(result)  # False

# result = int(float('9.8')) == 10
# print(result)  

# Calculate weekly earnings, monthly earnings, and annual earnings
# hours = float(input("Enter hours worked in a week: "))
# rate_per_hour = float(input("Enter rate per hour: "))
# weekly_earnings = hours * rate_per_hour
# monthly_earnings = weekly_earnings * 4
# annual_earnings = monthly_earnings * 12
# print("Weekly earnings:", weekly_earnings)
# print("Monthly earnings:", monthly_earnings)
# print("Annual earnings:", annual_earnings)

# Calculate number of seconds lived
# years = int(input("Enter number of years you have lived: "))
# days = years * 365
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60
# print("You have lived for", seconds, "seconds.")


# for i in range (1, 6):
#     print(i, 1, i, i**2, i**3) 

#Concatenate list elements into a string
# days = ['Thirty', 'Days', 'Of', 'Python']
# result = ' '.join(days)
# print(result)

# coding = ['Coding', 'For', 'All']  
# result = ' '.join(coding)
# print(result)

# coding = "Coding For All" 
# print(coding.lower())  

# items = ["apple", "banana", "cherry", "mango", "orange"] 
# print(len(items))

# first_item = items[0]
# middle_item = items[len(items) // 2]
# last_item = items[-1]

# print("First item:", first_item)
# print("Middle item:", middle_item)
# print("Last item:", last_item)

# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']  
# print(len(it_companies))
# first_company = it_companies[0]
# middle_company = it_companies[len(it_companies) // 2]
# last_company = it_companies[-1]
# print("First company:", first_company)
# print("Middle company:", middle_company)    
# print("Last company:", last_company)

# # Remove 'Amazon' from the list
# it_companies.remove('Amazon')
# print(it_companies)

# # Change 'Google' to 'Alphabet'
# it_companies[1] = 'Alphabet'
# print(it_companies)
# # Add 'Twitter' to the end of the list
# it_companies.append('Twitter')
# print(it_companies)

# # Insert 'LinkedIn' in the middle of the list
# middle_index = len(it_companies) // 2
# it_companies.insert(middle_index, 'LinkedIn') 
# print(it_companies)

# # Change 'LinkedIn' to uppercase
# it_companies[3] = it_companies[3].upper()
# print(it_companies)

# # Join the list into a string separated by spaces
# result = " ".join(it_companies)
# print(result)

# # Check if 'IBM' is in the list
# if 'IBM' in it_companies:
#     print("IBM is found in the list.")

# # Sort the list
# it_companies.sort()
# print(it_companies)

# # Reverse the list
# it_companies.reverse()
# print(it_companies)

# # Slice the first 3 companies
# first_three = it_companies[:3]
# print("First three companies:", first_three)

# # Slice the last 3 companies
# last_three = it_companies[-3:]
# print("Last three companies:", last_three)

# # Slice the middle company
# middle_company = it_companies[len(it_companies) // 2:len(it_companies) // 2 + 1]
# print("Middle company:", middle_company)

# # Remove the first company
# it_companies.pop(0)
# print(it_companies)

# # Remove the middle company
# middle_index = len(it_companies) // 2   
# it_companies.pop(middle_index)
# print(it_companies)

# # Remove the last company
# it_companies.pop(-1)
# print(it_companies)

# # Clear the list
# it_companies.clear()
# print(it_companies)

# Joining lists
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node', 'Express', 'MongoDB']
# full_stack = front_end + back_end
# insert elements at specific positions
# full_stack.insert(5,'Python')
# full_stack.insert(6,'SQL')
# print(full_stack)

# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ages.sort()
# min_age = ages[0]
# max_age = ages[-1]
# print("Ages:", ages)
# print("Min age:", min_age)
# print("Max age:", max_age)
# median_age = (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2 if len(ages) % 2 == 0 else ages[len(ages) // 2]
# print("Median age:", median_age)
# average_age = sum(ages) / len(ages)
# print("Average age:", average_age)
# range_of_ages = max_age - min_age
# print("Range of ages:", range_of_ages)
# # Compare min and max age with average age
# print("Min age is close to average age:", abs(min_age - average_age) < abs(max_age - average_age))  


# Read countries from a file and perform operations
# with open ("Exercises/countries.py") as file:
#     countries = file.read().splitlines()

# middle_index = len(countries) // 2
# middle_item = countries[middle_index]

# print("Middle country:", middle_item)

# countries_count = len(countries)

# print("Total number of countries:", countries_count)

# mid = (len(countries)) // 2
# first_half = countries[:mid]
# second_half = countries[mid:]
# print("First half:\n" + "\n".join(first_half))
# print("Second Half:\n" + "\n".join(second_half))

# countries_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# first, second, third, *scandic = countries_list

# print("First three countries in the list:", first, second, third)
# print("Scandic countries:\n" + "\n".join(scandic))

# Creating and manipulating tuples
# tuple1 = ('Henrik, Anna', 'John', 'Peter')
# tuple2 = ('Maria', 'Sofia', 'Laura')
# siblings = tuple1 + tuple2
# family_members = siblings + ('Mother', 'Father')
# print(siblings)
# print(len(siblings))
# print(family_members)
# unpacking tuples
# *siblings_only, father, mother = family_members
# print(siblings)
# print(father)
# print(mother)

# Tuple operations
# fruits = ('apple', 'banana', 'cherry', 'date', 'elderberry')
# vegetables = ('carrot', 'broccoli', 'spinach', 'potato', 'cabbage')
# animal_products = ('milk', 'cheese', 'yogurt', 'butter', 'eggs')
# food_stuff_tp = fruits + vegetables + animal_products
# print(food_stuff_tp)
# food_stuff_it = food_stuff_tp

# # Find the middle item
# mid = len(food_stuff_it) // 2
# middle_item = food_stuff_tp[mid]
# print("Middle item:", middle_item)

# # Slice the first three items
# first_three = food_stuff_it[:3]
# print("First three items:", first_three)

# # Slice the last three items
# last_three = food_stuff_it[-3:]
# print("Last three items:", last_three)
# del food_stuff_tp 

# nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
# if 'Estonia' in nordic_countries:
#     print("Estonia is a Nordic country.")
# else:
#     print("Estonia is not a Nordic country.")

# if 'Iceland' in nordic_countries:
#     print("Iceland is a Nordic country.")   
# else:
#     print("Iceland is not a Nordic country.")


# SETS
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# age = [22, 19, 24, 25, 26, 24, 25, 24]

# it_companies.add('Twitter')
# print(len(it_companies))

# it_companies.update(['LinkedIn', 'Snapchat', 'Pinterest'])
# print(it_companies)

# it_companies.remove('Oracle')
# print(it_companies)

# A_union_B = A.union(B)
# print("A union B:", A_union_B)

# A_intersection_B = A.intersection(B)
# print("A intersection B:", A_intersection_B)

# A_subset_B = A.issubset(B)
# print("Is A a subset of B?", A_subset_B)

# A_disjoint_B = A.isdisjoint(B)
# print("Are A and B disjoint?", A_disjoint_B)
# A_sym_diff_B = A.symmetric_difference(B)
# print("A symmetric difference B:", A_sym_diff_B)
# del A
# del B

# age_set = set(age)
# print("Age set:", age_set)
# print("Length of age list:", len(age))
# print("Length of age set:", len(age_set))


# sentence = "I am a teacher and I love to inspire and teach people"
# clean_sentence = sentence.lower().replace(".", "")

# # Split into words
# words = clean_sentence.split()

# # Get unique words using a set
# unique_words = set(words)

# print("Unique words:", unique_words)
# print("Number of unique words:", len(unique_words))

# dictionary operations
# dog = {
#     "name": "Buddy",
#     "age": 5,
#     "breed": "Golden Retriever",
#     "color": "Golden",
#     "is_vaccinated": True,
#     "favorite_foods": ["chicken", "beef", "carrots"]
# }

# student = {
#     "first_name": "Alice",
#     "last_name": "Johnson",
#     "gender": "Female",
#     "age": 22,
#     "marital_status": "Single",
#     "skills": ["Python", "Data Analysis", "Machine Learning"],
#     "country": "USA",
#     "city": "New York",
#     "address": {
#         "street": "123 Main St",
#         "zip_code": "10001"
#     }
# }

# print(len(student))
# # print the value of skills and check the data type
# print("Data type of skills:", type(student["skills"]))

# # Modify the skills by adding 'SQL' and 'Data Visualization'
# student["skills"].extend(["SQL", "Data Visualization"])
# print("Updated skills:", student["skills"])

# # Get the dictionary keys as a list
# student_keys = list(student.keys())
# print("Student dictionary keys:", student_keys)

# # Get the dictionary values as a list
# student_values = list(student.values())
# print("Student dictionary values:", student_values)

# # Create a list of tuples from the student dictionary
# student_items = list(student.items())
# print("Student dictionary items:", student_items)

# dog['legs'] = 4
# dog['tail'] = 'long'
# print(dog)

# del dog['color']
# print(dog)

# del student
# print(student)

# Conditional statements
# age =int(input("Enter your age: "))

# if age >= 18:
#     print("You are old enough to drive.")
# else:
#     years_left = 18 - age
#     print(f"You need {years_left} more years to drive.")

# my_age = 25
# your_age = int(input("Enter your age: "))
# if your_age > my_age:
#     age_diff = your_age - my_age
#     print(f"You are {age_diff} years older than me.")


# a = int(input("Enter number a: "))
# b = int(input("Enter number b: "))

# if a > b:
#     print("a is greater than b")
# elif a < b:
#     print("a is less than b")
# else:
#     print("a is equal to b")

# Grade calculation
# score = int(input("Enter your score (0-100): "))

# if 80 <= score <= 100:
#     print("Grade: A")
# elif 70 <= score <= 89:
#     print("Grade: B")
# elif 60 <= score <= 69:
#     print("Grade: C")
# elif 50 <= score <= 59:
#     print("Grade: D")
# elif 0 <= score <= 49:
#     print("Grade: F")
# else:
#     print("Invalid score. Please enter a score between 0 and 100.")


# Check season based on month
# month = input("Enter the month: ").strip().lower()
# if month in ['september', 'october', 'november']:
#     season = 'Autumn'
# elif month in ['december', 'january', 'february']:
#     season = 'Winter'
# elif month in ['march', 'april', 'may']:
#     season = 'Spring'
# elif month in ['june', 'july', 'august']:
#     season = 'Summer'
# else:
#     season = 'Invalid month'
# print("Season:", season)

# Fruits    
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit_input = input("Enter the name of a fruit: ").strip().lower()

# if fruit_input in fruits:
#     print("That fruit already exists in the list.")
# else:
#     fruits.append(fruit_input)
#     print("Fruit added to the list.")

# print("Updated fruit list:", fruits)

# person= {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 30,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }

# print middle skill
# middle_index = len(person['skills']) // 2
# middle_skill = person['skills'][middle_index]
# print("Middle skill:", middle_skill)

# # check if 'Python' is in skills
# if 'Python' in person['skills']:
#     print("Python is found in skills.")
# else: 
#     print("Python is not found in skills.")

# skills = person['skills']

# if set(skills) == {'JavaScript', 'React'}:
#     print("He is a front end developer.")
# elif set(['Node', 'Python', 'MongoDB']).issubset(skills):
#     print('He is a backend developer')
# elif set(['React', 'Node', 'MongoDB']).issubset(skills):
#     print('He is a fullstack developer')
# else:
#     print('unknown title')

# if person['is_married'] and person['country'] == 'Finland':
#     print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")

# for loop
# for number in range(11):
#     print(10 - number)    

# while loop
# count = 0
# while count < 11:
#     if count == 10:
#         count = count + 1
#         continue
#     print(count)
#     count = count + 1

# Print pattern
# i = 1
# while i <= 7:
#     print("#" * i)
#     i += 1

# nested loop 
# for i in range(8):
#     for j in range(8):
#         print("#", end="")
#     print("")

# multiplication table
# for i in range(11):
#   print(f"{i} x {i} = {i * i}")

# iterate through a list
# item = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for i in item:
#     print(i)

# print even numbers from 0 to 100
# for i in range(0 , 101):
#     if i % 2 == 0:
#         print(i)

# print odd numbers from 0 to 100
# for i in range(0 , 101):
#     if i % 2 != 0:
#         print(i)

# sum of all numbers 5050 
# total = 0
# for i in range(101):
#     total += i
# print("Sum of all numbers from 0 to 100 is:", total)

# sum of even numbers 2550
# even_total = 0
# for i in range(101):
#     if i % 2 == 0:
#         even_total += i
# print("Sum of all even numbers from 0 to 100 is:", even_total)

# sum of odd numbers 2500
# odd_total = 0   
# for i in range(101):
#     if i % 2 != 0:
#         odd_total += i
# print("Sum of all odd numbers from 0 to 100 is:", odd_total)

# countries with 'land' in their names
# with open("Exercises/countries.py") as file:
#   for line in file:
#       if "land" in line:
#        print(line.strip())

# reverse a list
# fruits = ['banana', 'orange', 'mango', 'lemon']
# for fruit in fruits[::-1]:
#     print(fruit)

