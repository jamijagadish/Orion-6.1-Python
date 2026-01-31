# for i in range(1,5): #i=1, i=2, i=3, i=4
#   for j in range(i): #range(4) j=0,1,2,3
#    print(j,end=' ' )
#   print()

#range(1) j=0
#range(2) j=0,1
#range(3) j=0,1,2
#range(4) j=0,1,2,3

#range(endPoint)
#range(startPoint,endPoint)
#range(startPoint,endPoint,step)

# for i in range(5,10):
#     for j in range(1):
#         print(j, end=' ')
#     print()


# Write a function to calculate factorial of a number.
# def calculatefact(num):
#   fact=1
# #   num=int(input("enter the number"))
#   for i in range(1,num+1):
#     fact=fact*i
#     i+=1 #unneccesry
#   print(fact)
# calculatefact(5)

# Check whether a number is divisible by 3 and 5 or not

# num = int(input("Enter a number ")) #19

# if num % 3==0 and num % 5 ==0:
#     print("Divisible by both 3 and 5")
# else:
#     if(num % 3==0):
#         print("Divisible by 3 but not by 5")
#     elif(num % 5==0):
#         print("Divisible by 5 but not by 3")
#     else:
#         print("Not divisible by both 3 and 5")

# num=int(input("enter a number"))
# if num % 3==0 and num % 5 ==0:
#     print("Divisible by both 3 and 5")
# elif(num%5==0):
#    print("the number is divisible by 5 ")
# elif(num%3==0):
#   print(" divisible by 3")  
# else:
#   print("not divisible by 3&5")


# Reverse a number using while loop

# num = int(input("Enter a number ")) #123
# rev = 0

# while(num>0):# 123, 12, 1
#     rem = num % 10 #3,2,1
#     rev = rev * 10 + rem #0+3= 3, 3*10= 30+2=32, 32*10=320+1=321
#     num = num // 10 #12, 1
# print(rev)

s = "The Supreme Court on Monday (January 12, 2026) stayed a Madhya Pradesh High Court order directing the reinstatement of a judicial officer who had been dismissed from service over allegations of serious misconduct on board a train, including urinating while in an inebriated state in the presence of a woman co-passenger."
#Count how many times a occurs in s
# print(s.count('a'))

#Replace a with A
# print(s.replace('a', 'A'))

#Split the string into words
# print(s.split())

#Check if the string is starts with x
# print(s.startswith('x'))

#Check if a string contains both letters and numbers
# print(s.isalnum())

# Functions
# def functionName():
#     # statements

def addition():
    print(10+20)
    print(10+20)
    print(10+20)
    print(10+20)
# addition()

# Function without parameters
def add():
    return 10+20
# sum = add()
# print(sum)
# print(add())

# Function with parameters
def sum(a,b):
    print("a=",a)
    print("b=",b)
    return a+b

# print(sum(10,30))
# print("------------")
# print(sum(100,200))
# print(sum(b=100,a=200))
# print(sum(10)) #error

# Function with default parameters
def multi(a=1, b=1):
    print("a=", a)
    print("b=", b)
    return a*b

# print(multi(10, 20))
# print("------------")
# print(multi(100, 200))
# print("------------")
# print(multi(b=100, a=200))
# print("------------")
# print(multi(10))