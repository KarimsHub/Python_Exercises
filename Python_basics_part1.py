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

#19. Write a Python program to get a new string from a given string where "Is" has been added to the front. 
#If the given string already begins with "Is" then return the string unchanged

#def change_string(string):
#    if string[:2] == 'Is':
#        return string
#    else:
#        return 'Is ' + string
#
#print(change_string('example string'))

#20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

#def string_copies(n, string):
#    lagerstring = ''
#    for i in string:
#        lagerstring += i
#    return lagerstring * n
#
#print(string_copies(2, 'hello'))

#21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

#def even_odd():
#    user_input = int(input('Please insert a number: '))
#    if user_input % 2 == 0:
#        return('The given number is even')
#    else:
#        return('The given number is odd')
#
#print(even_odd())


