print("QUESTION 1")
str="Python is a case sensitive language"

length=len(str) #finding the length of the input string

rev_str=str[ : :-1] # reversing the string

slice_str=str[10: ] #string slicing

replace_str=str.replace("a case sensitive","object oriented") #replacing 

find_str=str.find('a') #searching for 'a'

replace_str2=str.replace(" ","") #removing white spaces if any

print("Length of the string : ",length)

print("The reversed string : ",rev_str)

print("The silced string : ",slice_str)

print("The replaced string : ",replace_str)

print("Index of substring 'a' : ",find_str)

print("After removing whitespaces : ",replace_str2)


#--------------------------------------------------------------------------


print("QUESTION 2")
name=input("Enter your name : ") #taking input for name

sid=int(input("Enter your SID : ")) #taking input for sid

dept=input("Enter your departments's name : ") #taking input for department

cgpa=float(input("Enter you CGPA : ")) #taking input for cgpa

print("Hey,",name,"Here! \nMy SID is",sid,"\nI am from",dept,"department and my cgpa is",cgpa)


#--------------------------------------------------------------------------


print("QUESTION 3")

a=56;
b=10;

print("a & b is:",a&b) #using and bitwise operator

print("a | b is:",a|b) #using or bitwise operator

print("a ^ b is:",a^b) #using xor bitwise operator

print("left shift a with 2 bits gives :",a<<2) #using shift bitwise operator

print("left shift b with 2 bits gives :",b<<2) #using shift bitwise operator

print("right shift a with 2 bits gives :",a>>2) #using shift bitwise operator

print("right shift b with 4 bits gives :",b>>4) #using shift bitwise operator

#--------------------------------------------------------------------------


print("QUESTION 4")
num1=int(input("Enter number 1 : "))
num2=int(input("Enter number 2 : "))
num3=int(input("Enter number 3 : "))
if(num1>num2 and num1>num3):
         print("The largest number entered is : ",num1)
         
elif (num2>num1 and num2>num3):
         print("The largest number entered is : ",num2)
else:
    print("The largest number entered is : ",num3)

#--------------------------------------------------------------------------


print("QUESTION 5")
str=input("Enter your string : ") #taking input for the string
i=str.find("name") #searching for 'name'

if(i==-1):  #find returns -1 when the given string / substring is not found
    print("No")

else:       
    print("Yes")


#--------------------------------------------------------------------------


print("QUESTION 6")
side_1=int(input("Enter first side : ")) #taking input for first side

side_2=int(input("Enter second side : ")) #taking input for second side

side_3=int(input("Enter third side : ")) #taking input for third side

#the condition for 3 numbers to form a triangle or not
if ( side_1 < (side_2 + side_3) and side_2 < (side_1 + side_3) and side_3 < (side_2 + side_1)):
    print("Yes")

else:
    print("No")
    




   
    
         





         








