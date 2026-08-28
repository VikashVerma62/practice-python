
#!Q1. Take marks as input and print grade.
#! 90 and above = A+
#! 75 to 89 = A
#! 60 to 74 = B
#! 40 to 59 = C
#! Below 40 = F


#? marks=int(input("Enter marks "))
#? if marks>=90:
#?     print("A+")
# elif marks>=75 and marks<=89:
#     print("A")
# elif marks>=60 and marks<=74:
#     print("B")
# elif marks>=40 and marks<=59:
#     print("C")
# else:
#     print("Fail")


#!Q2. Take a number as input and print whether it is Positive, Negative, or Zero.
# num=int(input("Enter a number"))
# if num>0:
#     print("Positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")


#!Q3. Take a number from 1 to 7 as input and print the day name.
#! 1 = Monday, 2 = Tuesday ... 7 = Sunday

# day=int(input("Enter the day from 1 to 7 "))
# if day==1:
#     print("Monday")
# elif day==2:
#     print("Tuesday")
# elif day==3:
#     print("Wensday")
# elif day==4:
#     print("Thursday")
# elif day==5:
#     print("Friday")
# elif day==6:
#     print("Saturday")
# elif day==7:
#     print("Sunday")
# else:
#     print("Invalid number ")


#!Q4. Take speed as input and print the category.
#! Below 40 = Too Slow
#! 40 to 80 = Normal
#! 81 to 100 = Fast
#! Above 100 = Over Speed


# speed=int(input("Enter the speed "))
# if speed<0:
#     print("Speed are not in negative")
# elif speed<40:
#     print("Too Slow")
# elif speed>=40 and speed<=80:
#     print("Normal")
# elif speed>=81 and speed<=100:
#     print("Fast")
# elif speed>100:
#     print("Over Speed")


#!Q5. Take a month number as input (1 to 12) and print the month name.
# month=int(input("Enter the month from 1 to 12 "))
# if month<=0:
#     print("month are not in negative or zero")
# elif month==1:
#     print("january")
# elif month==2:
#     print("February")
# elif month==3:
#     print("March")
# elif month==4:
#     print("April")
# elif month==5:
#     print("May")
# elif month==6:
#     print("June")
# elif month==7:
#     print("July")
# elif month==8:
#     print("August")
# elif month==9:
#     print("September")
# elif month==10:
#     print("Octumber")
# elif month==11:
#     print("November")
# elif month==12:
#     print("December")
# else:
#     print("please give a valid month number")



#!Q6. Calculate electricity bill based on units consumed.
#! 0 to 100 units = Rs 2 per unit
#! 101 to 300 units = Rs 4 per unit
#! Above 300 units = Rs 6 per unit
#! Take units as input and print total bill.

# unit=int(input("Enter the unit "))
# if unit>0 and unit<=100:
#     bill=unit*2
# elif unit>=101 and unit <=300:
#     bill=unit*4
# elif unit>300:
#     bill=unit*6
# print("the bill is",bill)


#!Q7. Take a person's age as input and print the category.
#! Below 13 = Child
#! 13 to 17 = Teenager
#! 18 to 60 = Adult
#! Above 60 = Senior Citizen

# age=int(input("Enter the age "))
# if age<13:
#     print("Child")
# elif age>=13 and age<=17:
#     print("Teenager")
# elif age>=18 and age<=60:
#     print("Adult")
# else:
#     print("Senior Citizen")



#Q8. Take a shop purchase amount as input and print discount and final amount.
# Above Rs 5000 = 20% discount
# Above Rs 2000 = 10% discount
# Above Rs 500 = 5% discount
# # Below Rs 500 = No discount


# amount=int(input("Enter the amount "))
# if amount>5000:
#     discount=(amount*20/100)
# elif amount>2000 and amount<5000:
#     discount=(amount*10/100)
# elif amount>500 and amount<2000:
#     discount=(amount*5/100)
# else:
#    discount=print("NO discount Below 500")
# print("Discount",discount)
# print("The final amount is ",amount-discount)



#!Q9. Take a BMI value as input and print the category.
#! Below 18.5 = Underweight
#! 18.5 to 24.9 = Normal
#! 25.0 to 29.9 = Overweight
#! 30 and above = Obese

bmi=float(input("Enter BMI"))
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("Normal")
elif bmi>=25.0 and bmi<=29.9:
    print("Overweight")
else:
    print("Obese")





