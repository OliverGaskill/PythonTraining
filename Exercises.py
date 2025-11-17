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



