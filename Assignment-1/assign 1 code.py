'''ASSIGNMENT 1
QUESTION 1'''
print("QUESTION 1")
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
avg=(num1+num2+num3)/3
print("The average is:",avg)

#-------------------------------------------------------


print("QUESTION 2")
gross=int(input("Enter Gross Income:"))
dep=int(input("Enter no of dependants"))
taxable_income=gross-10000-(3000*dep)
tax=taxable_income*0.2
print("The net tax is:",tax)

#-------------------------------------------------------

print("QUESTION 3")
print("Student [SID, Name, Gender, Course Name, CGPA]")
student=[1005,"Jerry","M","ECE",9.3]
print("Student=",student)

#-------------------------------------------------------


print("QUESTION 4")
print("Marks of 5 Students")
Marks=[44,65,22,60,13]
print("Marks before sorting",Marks)
Marks.sort()
print("SORTED LIST",Marks)


#-------------------------------------------------------


print("QUESTION 5")
color=["RED","GREEN","WHITE","BLACK","PINK","YELLOW"]
color.pop(3)
print(color)
color[3:5]=["PURPLE"]
print(color)





