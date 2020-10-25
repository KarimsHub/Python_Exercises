#1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
#Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :
#
#Twinkle, twinkle, little star,
#	How I wonder what you are! 
#		Up above the world so high,   		
#		Like a diamond in the sky. 
#Twinkle, twinkle, little star, 
#	How I wonder what you are

#def print_string():
#    print('Twinkle, twinkle, little star,\n  How I wonder what you are! \n      Up above the world so high, \n      Like a diamond in the sky. \nTwinkle, twinkle, little star, \n  How I wonder what you are')


#2. Write a Python program to display the current date and time.
#Sample Output :
#Current date and time :
#2014-07-05 14:34:14
#import time
#
#def get_time():
#    print(time.asctime())


#3. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
#Sample Output :
#r = 1.1
#Area = 3.8013271108436504

#import numpy
#def compute_area_from_circle():
#    pi = numpy.pi
#    radius = float(input('Please insert the radius: '))
#    area = pi * radius ** 23 ,
#    print('The area of the given circle is %s!' % area)

#4. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
#def reversed_name():
#    first_last = input('Please insert your first and last name: ')
#    print(first_last[::-1]) # Omitting the two index numbers and retaining colons will keep the whole string within range. Additionally, you can indicate a negative numeric value for the stride

#5. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
#Output :
#Sample data : 3, 5, 7, 23
#List : ['3', ' 5', ' 7', ' 23']
#Tuple : ('3', ' 5', ' 7', ' 23')

#def create_list_and_tuple():
#    user_input = input('Please insert comma-sperated numbers: ').replace(',', '')
#    print(list(user_input))
#    print(tuple(user_input))

#6. Write a Python program to accept a filename from the user and print the extension of that.
#Sample filename : abc.java
#Output : java

#def only_extension():
#    new_string = ''
#    user_input = input('Please insert the filename with extension: ')
#    extension = user_input.split('.')[1] # The spit function returns a list of the words of a given string using a separator as the delimiter string.
#    print('The name of the extension is %s' % extension)

#7. Write a Python program to display the first and last colors from the following list.
#color_list = ["Red","Green","White" ,"Black"]

#def print_first_last(list):
#    #print(color_list[0])
#    #print(color_list[-1])
#    # nicer way: 
#    print('%s & %s' %(color_list[0], color_list[-1]))

#8. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
#exam_st_date = (11, 12, 2014)
#Sample Output : The examination will start from : 11 / 12 / 2014

#def print_date():
#    print('Examination starts at: %s /%s / %s' % (exam_st_date))

#9. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#Sample value of n is 5
#Expected Result : 615

#def compute_value(n):
#    one = int('%s' % n)
#    two = int('%s%s' % (n,n))
#    three = int('%s%s%s' % (n,n,n))
#    print(one + two + three)

# 10. Write a Python program to print the calendar of a given month and year.
#import calendar
#
#def display_calender():
#    yy = int(input('Please insert in a year: '))
#    mm = int(input('Please insert in a month: '))
#    print(calendar.month(yy, mm))
#
#display_calender()

#11. Write a Python program to calculate number of days between two dates.
#Sample dates : (2014, 7, 2), (2014, 7, 11)
#Expected output : 9 days
#from dateutil import parser
#from datetime import date
#
#def calculate_days():
#    date1 = parser.parse(input("Enter first date: "))
#    date2 = parser.parse(input("Enter second date: "))
#    delta = date2 - date1
#    print(delta.days)
#
#calculate_days()

#12. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

#def difference_number(n):
#    if n <= 17:
#        return 17 - n 
#    else:
#        return (n - 17) * 2
#
#print(difference_number(14))

#13. Write a Python program to test whether a number is within 100 of 1000 or 2000.

#def number_within(n):
#    if (abs((1000 - n) < 100) or abs((2000 - n) < 100)):
#        return True
#    else:
#        return False
#
#print(number_within(990))

#14. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

#def sum_three_numbers(one, two, three):
#    if one == two == three:
#        return (one + two + three) * 3
#    else:
#        return (one + two + three)
#
#print(sum_three_numbers(7, 7, 7))

#15. Write a Python program to get a new string from a given string where "Is" has been added to the front. 
#If the given string already begins with "Is" then return the string unchanged

#def change_string(string):
#    if string[:2] == 'Is':
#        return string
#    else:
#        return 'Is ' + string
#
#print(change_string('example string'))

#16. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

#def string_copies(n, string):
#    lagerstring = ''
#    for i in string:
#        lagerstring += i
#    return lagerstring * n
#
#print(string_copies(2, 'hello'))

#17. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

#def even_odd():
#    user_input = int(input('Please insert a number: '))
#    if user_input % 2 == 0:
#        return('The given number is even')
#    else:
#        return('The given number is odd')
#
#print(even_odd())

#18. Write a Python program to count the number 4 in a given list.

#def counting_number(liste):
#    count = 0
#    for i in liste:
#        if i == 4:
#            count += 1
#    return count
#
#print(counting_number([3, 7, 12, 4, 6, 4]))

#19. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. 
#Return the n copies of the whole string if the length is less than 2.

#def n_copies(n, string):
#    if len(string) < 2:
#        return n * string
#    else:
#        return n * string[:2]
#
#print(n_copies(4, 'h'))

#20. Write a Python program to test whether a passed letter is a vowel or not.

#def check_vowel(letter):
#    vowels = 'aeiou'
#    if letter in vowels:
#        return 'This letter is a vowel'
#    else:
#        return 'This letter is not a vowel'
#
#print(check_vowel('b'))

#21. Write a Python program to check whether a specified value is contained in a group of values.
#Test Data :
#3 -> [1, 5, 8, 3] : True
#-1 -> [1, 5, 8, 3] : False

#list1 = [1, 5, 8, 3]
#list2 = [1, 5, 8, 3]
#
#def check_number_in_list(n, liste):
#    for i in liste:
#        if i == n:
#            return True
#    else:
#        return False
#
#print(check_number_in_list(-1, list2))

#22. Write a Python program to concatenate all elements in a list into a string and return it.
#new_list = ['hello', 'world', 'cool', 1]
#
#def concatenate_list(liste):
#    new_string = ''
#    for i in liste:
#        new_string += str(i)
#    return new_string
#
#print(concatenate_list(new_list))

#23. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
#Sample numbers list :

#numbers = [    
#    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#    958,743, 527
#    ]
#
#def printing_even_numbers(liste):
#    for i in liste:
#        if i % 2 == 0:
#            print(i)
#        elif i == 237:
#            break
#
#printing_even_numbers(numbers)

#24. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
#Test Data :
#color_list_1 = set(["White", "Black", "Red"])
#color_list_2 = set(["Red", "Green"])
#Expected Output :
#{'Black', 'White'}

#def comparing_lists(list1, list2):
#    return list1.difference(list2) # The difference() method returns the set difference of two sets.
#
#print(comparing_lists(color_list_1, color_list_2))

#25. Write a Python program that will accept the base and height of a triangle and compute the area.

#def area_of_triangle():
#    base = float(input('Plase insert the base: '))
#    height = float(input('Please insert the height: '))
#    area = (base * height) / 2
#    return 'The area of the triangle is %s' % area
#
#print(area_of_triangle())

#26. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

#def compute_gcd(number1, number2):
#    if number2 == 0:
#        return number1
#    else:
#        return compute_gcd(number2, number1 % number2) #using recursion
#
#print(compute_gcd(48, 18))

#27. Write a Python program to get the least common multiple (LCM) of two positive integers.

#def compute_lcm(number1, number2):
#    if number1 > number2:
#        higher = number1
#    else:
#        higher = number2
#    value = higher
#    
#    while True:
#        if higher % number1 == 0 and higher % number2 == 0:
#            return higher
#            break
#        else:
#            higher = higher + value
#
#print(compute_lcm(2, 3))

#28. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

#def sum_three_numbers_part_two(one, two, three):
#    if one == two or one == three or two == three:
#        return 0
#    else:
#        return one + two + three

#29. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

#def sum_integers(one, two):
#    result = one + two
#    if result > 15 and result <= 20:
#        return 20
#    else:
#        return result
#
#better approach:
#def sum_integers(one, two):
#    result = one + two
#    if result in range(15, 20):
#        return 20
#    else:
#        return result
#
#print(sum_integers(5, 14))  

#30. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

#def check_intvalues(one, two):
#    if one is two or one + two == 5 or abs(one - two) == 5:
#        return True
#    else:
#        return False
#
#print(check_intvalues(2, 7))

#31. Write a Python program to add two objects if both objects are an integer type.

#def add_int(one, two):
#    if not (isinstance(one, int) and isinstance(two, int)): #The isinstance() function returns True if the specified object is of the specified type, otherwise False.
#        return 'no integer value'
#    else:
#        return one + two
#
#print(add_int(5, 7))

#32. Write a Python program to display your details like name, age, address in three different lines.

#def details_differentline(name, age, adress):
#    print('%s\n%d\n%s' % (name, age, adress))
#
#details_differentline('karim', 12, 'kottwitz')

#33. Write a Python program to solve (x + y) * (x + y).
#Test Data : x = 4, y = 3
#Expected Output : (4 + 3) ^ 2) = 49

#def solve(x, y):
#    result = (x + y) * (x + y)
#    return '(%d + %d) * 2 = %d' % (x, y, result)
#
#print(solve(4, 3))

#34. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
#Test Data : amt = 10000, int = 3.5, years = 7
#Expected Output : 12722.79

#def interest_rate(money, rate, years):
#    decimal_rate = rate / 100
#    for i in range(years):
#        result = money * decimal_rate
#        money += result
#    return money
#
#print(interest_rate(10000, 3.5, 7))

#35. Write a Python program to check whether a file exists.

#def check_file():
#    import os.path
#    open('example.docx', 'r')
#    print(os.path.isfile('example.docx'))
#
#check_file()

#36. Write a Python program to get OS name, platform and release information.
#import os
#
#def get_os():
#    os_info = os.uname()
#    print(os_info)
#
#get_os()

#37. Write a Python to find local IP addresses using Python's stdlib
#import socket
#def get_local_ip():
#    hostname = socket.gethostname()
#    ipadress = socket.gethostbyname(hostname)
#    print(ipadress)
#
#get_local_ip()