#Assginment-4

print("Question-1")

def towerofhanoi(n , source, destination, temporary):   #defining the function
    step_number=1
    if n==1:
        print ("Move disk 1 from",source,"to",destination)
        return
    towerofhanoi(n-1, source, temporary, destination)
    print ("Move disk",n,"from",source,"to",destination)
    towerofhanoi(n-1, temporary, destination, source)

no_of_disk=int(input("Enter number of disks you want: "))    #Taking Input for the number of disks in the Tower
print("\nSteps to move all disks from Source Tower to Destination Tower :\n")

towerofhanoi(no_of_disk,"Source Tower","Destination","Temporary") #Calling the function

#------------------------------------------------------------------------------------------------------------------------

print("Question-2")

n = int(input("Enter the number of rows to be printed : ")) #taking input for th number of lines to be

print("\nUsing Recursion: ") #first using recursion
def pascal(n, T=n):
    if n == 0:
        return
    pascal(n - 1, T)
    print('  ' * (T - n), end='')     #for spaces
    num1 = 1
    for i in range(1, n + 1):   
        print(num1, end='   ')        #for binomail coefficients
        num1 = num1 * (n - i) // i
    print()
pascal(n)

print("\nUsing Iteration: ")   #now using iteration
for j in range(1,n+1):
    print('  '*(n - j),end='')   #for spaces
    t = 1
    for i in range(1,j+1):
        print(t,end='   ')
        t = t*(j - i)//i        #for binomail coefficients
    print()
print("")

#------------------------------------------------------------------------------------------------------------------------

print("Question-3")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

while b == 0:             #divison by zero is not allowed so nulling out this case
    b = int(input("ERROR!!! Can not divide by zero. Enter a different number: "))

Q, R = divmod(a, b)
m = [Q, R]

def division():
    Q, R = divmod(a, b)
    print(f"Questiont:{Q}\nRemainder:{R}")


division()
 
print('3-a')                     #question 3 part a
t=callable(division)
if (t):
    print("The function is callable")
else:
    print("The function is not callable")
    
print('3-b')                    #question 3 part b
if all(divmod(a, b)):
    print('All the values are non zero')
else:
    print('All the values are not non zero')

print('3-c')                    #question 3 part c
m.extend([4, 5, 6])
print("After adding 4,5,6 : ", m)
f=filter(lambda n: n > 4, m)
print("Values greater than 4 are : ",list(f))

print('3-d')                    #question 3 part d
set1= set(m)
print(set1)

print('3-e')                    #question 3 part e
set2= frozenset(set1)
print("Immutable set: ",set2)

print('3-f')                    #question 3 part f
m = max(set2)
print("Maximum value in the set:",m)
print("The hash value of",m,"is:",hash(str(m)))

#------------------------------------------------------------------------------------------------------------------------

print("Question-4")

class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object destroyed")
        
student1 = Student("Harsh Seth", 21105103)  #creating object
print("Object created")

print(f"The name of the student is {student1.name} and SID is {student1.sid}.")    #printing the values

del student1        #deleting object

#------------------------------------------------------------------------------------------------------------------------

print("Question 5")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __del__(self):
        print(f"Employee {self.name}'s record deleted")


E1= Employee("Mehak", 40000)
E2= Employee("Ashok", 50000)
E3= Employee("Viren", 60000)

print("Part A")             #Question 5 part-a
E1.salary = 70000
print(f"The updated salary of the employee {E1.name} is {E2.salary}")

print("Part B")             #Question 5 part-b
del E3

#------------------------------------------------------------------------------------------------------------------------

print("Question-6")

G_word=input("Enter George's word: ")
B_word=input("Enter Barbie's word: ")

def anagrams(t):
    if t=="":
        return[t]
    ans=[]
    for i in anagrams(t[1:]):
        for j in range(len(i)+1):
            ans.append(i[:j] + t[0] + i[j:])
    return ans
Anagrams=anagrams(G_word)

f=False
for i in Anagrams:
    if i==B_word and f==False:
        print("Friendship is True!!")
        f=True
if f==False:
    print("Friendship is Fake!!")

#------------------------------------------------------------------------------------------------------------------------

