#Day 1: Data Types and Variables


#Comments: Text used to explain, doesn't affect code 
#Must start with a pound sign or 3 pairs of singular or double quotation marks
#This is a comment
'''
This is also a comment
'''
#--------------------------------------------------------------------------------------------------------

#Strings (str): Text
#Must be in a pair of single or double quotation marks
print('Text')
print("Text")
#--------------------------------------------------------------------------------------------------------

#Integers (int): Positve/Negative Whole Numbers
print(1)
print(-100)
#--------------------------------------------------------------------------------------------------------

#Floats (float): Positive/Negative Decimal Numbers
print(-1.1)
print(1.0)
#--------------------------------------------------------------------------------------------------------

#Characters (char): Single letter, number, or symbol
#Must be in a pair of single or double quotes
print('a')
print('@')
#--------------------------------------------------------------------------------------------------------

#Varibles: Placeholders
#Variable names cannot contain spaces or any special characters or numbers for a first letter
'''
N/A:

1name = 'Eric'
$Age = 16
High School = "Lowell"
'''

name = 'Eric'
High_school = "Lowell"
Age = 16 

#--------------------------------------------------------------------------------------------------------

print('Hello') #print statement 
#--------------------------------------------------------------------------------------------------------

x = 5
x = 7 #x is now equal to 7, variables update to latest assignment
#--------------------------------------------------------------------------------------------------------

print(1+2) #addition, 3
print(1-2) #subtraction, -1
print(1*2) #multiplication, 2
print(1/2) #division, 0.5
print(1**2) #exponents, 1^2 
print(5%2) #modulous, shows division remainder, 1

print(1+2/3+8**2/2) #PEMDAS automatically, 33.666666666666664
print((1+2)/(3+8**2)/2) #Parenthesis prioritizes operations, 0.022388059701492536
#--------------------------------------------------------------------------------------------------------

#Concatenation: Combining strings,numbers,variables
my_name = 'Eric'
highschool  = 'Lowell'
print('Hello my name is ' + my_name + ', I am 16' + ' and I got to ' + highschool)
print('Hello my name is {}, I am 16 and I got to {} '.format(my_name,highschool))
