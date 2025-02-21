# =>Write a program to check if a given number is positive, negative, or zero.
# num=int(input("enter a number"))
# if num>0:
#     print("positive")
# elif num==0:
#     print("zero")
# else:
#     print("negative")


# =>Determine if a number is odd or even.
# num=int(input("enter a number"))
# if num%2==0:
#     print("even")
# elif num==0:
#       print("number is zero")
# else:
#     print("odd")


# =>Check if a person is eligible to vote (age >= 18).
# age = int(input("Enter your age"))
# if age>= 18 :
#     print("you are eligible")  
# else:
#     print("not eligible")

# print("you are eligible") if age >=18 else print("not eligible")


# =>Write a program to find the greatest of two numbers.
# num1 = float(input("Enter a number for num1"))
# num2 = float(input("Enter a number for num2"))
# # print('num1 is greatest') if num1 > num2 else print('both are equal') if num1 == num2 else print ('num2 is greater')
# if num1>num2:
#     print("num1 is bigger")
# elif num1<num2:
#     print("num2 is bigger")
# else:
#     print("both are equal")


# =>Print "Pass" if a student scores more than 40 marks; otherwise, print "Fail."
# marks = int(input("marks obtaine"))
# # print("pass") if marks > 40 else print("fail") 
# if marks>40:
#     print("passed")
# else:
#     print("fail")



# =>Write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday, etc.).
# day = int(input("Enter a number for day "))
# if day==1 :
#     print('Monday')
# elif day==2 :
#     print('Tuesday')
# elif day==3 :
#     print('Wednesday')
# elif day==4 :
#     print('Thursday')
# elif day==5 :
#     print('Friday')
# elif day==6 :
#     print('Saturday')
# elif day==7 :
#     print('Sunday')
# else:
#     print('enter a valid day')




# =>Implement a simple calculator to perform addition, subtraction, multiplication, and division.
# numb1 = float(input("Enter a number "))
# numb2 = float(input("Enter a number "))
# operation = input("Enter an operation ").lower()

# if operation=='add' or operation=='+' :
#     print('addition is ',numb1+numb2)
# elif operation=='sub' or operation=='-':
#     print('subtraction is ',numb1-numb2)
# elif operation=='mul' or operation =='*':
#     print('multiplication is ',numb1*numb2)
# elif operation=='div' or operation == '/':
#     if numb2 == 0:
#         print("division by zero is not possible")
#     else:
#         print('division is ',numb1/numb2)
# else:
#     print('invalid input')



# =>Write a program to display the name of a month based on the month number (1 for January, 2 for February, etc.).
# month = int(input("Enter a month number "))
# if month==1 :
#     print('January')
# elif month==2 :
#     print('February')
# elif month==3 :
#     print('March')
# elif month==4 :
#     print('April')
# elif month==5 :
#     print('May')
# elif month==6 :
#     print('June')
# elif month==7 :
#     print('July')
# elif month==8 :
#     print('August')
# elif month==9 :
#     print('September')
# elif month==10 :
#     print('October')
# elif month==11 :
#     print('November')
# elif month==12 :
#     print('December')
# else:
#     print('invalid month')


# =>Write a program to find the greatest of three numbers. 
# num1 = float(input("Enter num1 "))
# num2 = float(input("Enter num2 "))
# num3 = float(input("Enter num3 "))

# if num1>=num2 and num1>num3:
#     print(num1, "is bigger")
# elif num2>=num3 and num2>num1:
#     print(num2,"is bigger")
# elif num3>=num1 and num3>num2:
#     print(num3, "is bigger")
# else:
#     print("all are equal")


# =>Check if a year is a leap year
# year = int(input("Enter a year "))
# if year % 4==0 and  year%400==0:
#     print (year,"is a leap year")
# else:
#     print(year,"is not a leap year")


# =>Write a program to classify a character entered by the user as a vowel, consonant, or neither.
# alphabet=input("Enter a single Character ").lower()
# if len(alphabet)!=1:
#     print("Invalid")
# else:
#     if alphabet in['a','e','i','o','u']:
#         print("Vowels")
#     elif alphabet.isalpha():
#         print("consonant")
#     else:
#         print("Special characters")



# =>Calculate the grade of a student based on the marks they score: 1. 90-100 : Grade A 2. 80-89 : Grade B 3. 70-79 : Grade C 4. <70 : Fail.
# marks = float(input("Enter your marks "))

# if marks>=90 and marks<=100:
#     print("A grade")
# elif marks>=80 and marks<=89:
#     print("B grade")
# elif marks>=70 and marks<=79:
#     print("C grade")
# elif marks>=0 and marks<=70:
#     print("Failed")
# else:
#     print("please enter marks between 0-100 only")



# =>Write a program to check if three sides length form a valid triangle.

# side1 = float(input("Enter the first side "))
# side2 = float(input("Enter the second side "))
# side3 = float(input("Enter the third side "))

# if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
#     print("The given sides form a valid triangle.")
# else:
#     print("The given sides do not form a valid triangle.")