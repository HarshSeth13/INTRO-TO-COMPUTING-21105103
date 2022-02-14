print("QUESTION-1")
str1= input('Enter the string :')
str1_lower=str1.lower()
ele=str1.split()
occurences={}  # to store key value pairs of word/words and their occurences

if len(ele)>1: #for multi word string
 	for n in range (len(ele)):
 		if ele[n] in occurences:
 			occurences[ele[n]]+=1
 		else:
 			occurences[ele[n]]=1

elif len(ele)==1: #for checking occurences if a single word is entered
        single_ele=list(str1)
        for n in range(len(single_ele)):
                if single_ele[n] in occurences:
                	occurences[single_ele[n]]+=1
                else:
                	occurences[single_ele[n]]=1

else:  #If no valid input is entered
        print("Error! Invalid Input. Atleast enter a string or a character")
        
print(str(occurences)) #getting the occurences of words/word of the string entered 


#-------------------------------------------------------------------------------------

                    	
print("QUESTION-2")
mon_30=[4,6,9,11]    #all the months ending on 30
mon_31=[1,3,5,7,8,10,12] #all the months ending on 31
c=1

def leapyear(x):     #creating a function to check leap year case
    if ((x%400)==0 or ((x%100!=0) and (x%4==0))):
        return True
    else:
        return False
while 1:
    year=int(input("Please enter Year :"))   #taking inputs
    date=int(input("Please enter Date :"))   #taking inputs
    month=int(input("Please enter Month :")) #taking inputs

    if (date<1 or date>31 or month<1 or month>12 or year<1800 or year>2025):  #cancelling out all the invalid inputs
        print("Error! Invalid Inputs")
        c=0
    elif month>30 and month in mon_30:
        print("Error! Invalid Inputs")
        c=0
    elif month>31 and month in mon_31:
        print("Error! Invalid Inputs")
        c=0
    elif month==2 and date>=29:
        if leapyear(year) and date != 29:
            print("Error! Invalid Inputs")
            c=0
            continue
        elif not leapyear(year):
            print("Error! Invalid Inputs")
            c=0
            continue
    break

if(c!=0):
    if month == 2:          #checking leapyear for february
        if leapyear(year):
            days = 29
        else:
            days = 28
    elif month in mon_30:
            days = 30
    else:
            days = 31
    if date == days:            
        date = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    else:
        date += 1
    print("Next Date is: ", end='')
    print(date,month,year,sep='/')


#-------------------------------------------------------------------------------------


print("QUESTION-3")
list1=eval(input("Enter the values: "))# to take value for the list
list2=[]                               # creating an empty list to later store values in it
for num in list1:
    list2.append((num,num*num))        # using append function to add values in the empty list
print(list2)                           # finally printing out the list


#-------------------------------------------------------------------------------------


print("QUESTION-4")
grade=int(input("Enter the Grade Point:")) # taking input for the Grade Number
if( 4<=grade<=10):                         # conditions
    if (grade==10):
        print("Your Grade is 'A+' and Outstanding Performance")
    if (grade==9):
        print("Your Grade is 'A' and Excellent Performance")
    if (grade==8):
        print("Your Grade is 'B+' and Very Good Performance")
    if (grade==7):
        print("Your Grade is 'B' and Good Performance")
    if (grade==6):
        print("Your Grade is 'C+' and Average Performance")
    if (grade==5):
        print("Your Grade is 'C' and Below Average  Performance")
    if (grade==4):
        print("Your Grade is 'D' and Poor Performance")
else:
    print("Error")                       # printing error if any other value is given by the user


#-------------------------------------------------------------------------------------


print("QUESTION-5")
s="ABCDEFGHIJK"      # the string we need to print
l1=list(s)           # converting the characters into independant elements by using a list
for i in range(0,6):
    col=0
    count=0
    while col<11:
        if col<i or col>11-i-1:
            print(' ', end='')
        else:
            print(l1[count],end='')
            count+=1
        col+=1
    print('')

   
#-------------------------------------------------------------------------------------


print("QUESTION-6")
dict1={}                        #creating an empty dictionary to add inputs in it
SID=int(input("Please Enter SID of Student- "))    #taking input for SID
name=input("Please enter the name of the Student- ")    #taking input for name
dict1[SID]=name                 #adding inputs in the dictionary

while True:
    ch=input("Enter Y to continue or N to end:")   #asking if the user wants to add more data
    if ch in ['Y','y']:                        
        SID=int(input("Please Enter SID of Student- "))    #taking input for SID
        name=input("Please enter the name of the Student- ")  #taking input for name
        dict1[SID]=name          #adding inputs in the dictionary

    else:
        break



print("PART A")                  #first part of the ques(a)-----printing the dictionary
print(dict1)

print("PART B")                  #second part of the ques(b)-----sorting with respect to values
sorted_dict= sorted(dict1.values())
print(f"Dictionary sorted with respect to values is:  {sorted_dict}")
print()

print("PART C")                  #third part of the ques(c)-----sorting with respect to keys
sorted_dict2= sorted(dict1.keys())
print(f"Dictionary sorted with respect to keys is: {sorted_dict2}")
print()

print("PART D")                  #fourth part of the ques(d)----finding a desired student's name using SID
SID_find=int(input("Please enter the student's SID whose detail you need- "))
if SID_find in dict1.keys():
    print(f"The desired student's name is : {dict1[SID_find]}")
else:
    print("The entered sid is not present in the given data")
print("")


#-------------------------------------------------------------------------------------


print("QUESTION-7")
N=int(input("Please enter the number of terms you want to get = ")) #taking input for the no. of terms in the series

First = 0  #initial condition
Second = 1 #initial condition
Sum = 0    #for getting the final

if(N==0):  #printing error as the number of terms can not be zero
    print("Error")
print("The Fibonacci Series for",N,"terms is: ",end='')

for Num in range(0, N):     #creating a for loop till N terms
    print(First, end = '  ')
    Sum = Sum + First
    Next = First + Second    #as the formula for this series is Fn-1+Fn-2=Fn
    First = Second
    Second = Next

avg=Sum/N                #for getting the average
 
print("\nThe Average of this series is : ",avg)


#-------------------------------------------------------------------------------------


print("QUESTION-8")
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

Set4=Set1^Set2    #a ---- to get a new set of all the elements which are in Set1 and Set2 but not both
print("Set of all elements that are in Set1 and Set2 but not both:",Set4)
print()

Set5=Set1 ^ Set2 ^ Set3 #b --- to get a new set of all the elements that are in only one of the three sets
print("Set of all elements that are in only one of the three sets Set1, Set2 and Set3:",Set5)
print()

Set6 = (Set1|Set2|Set3) - (Set1^Set2^Set3) - (Set1&Set2&Set3) #c --- to get a new set of all elements that are exactly two of the sets 
print("Set of elements that are in exactly two of the sets Set1, Set2 and Set3:",Set6)
print()

Set7=set()
for a in (1,2,3,4,5,6,7,8,9,10): #d --- to get a new set of all integers in the range of 1 to 10 that are not in Set1
    if a not in Set1:
        Set7.add(a)
print("Set of all integers in the range 1 to 10 that are not in Set1:",Set7)
print()

Set8=set() #e --- to get a new set of all integers in the range of 1 to 10 that are not in Set1,Set2,Set3
Set8 = set(range(1,11)) - (Set1|Set2|Set3)
print("Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:",Set8)


#-------------------------------------------------------------------------------------


