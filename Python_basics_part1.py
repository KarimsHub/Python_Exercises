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






