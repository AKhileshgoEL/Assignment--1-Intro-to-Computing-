#Ques_1

print('#Ques_1')

#given information

my_string= "Python is a case sensitive language"

#a

print (len (my_string))

#b

print (my_string[::-1])

#C

print (my_string[10:-9])

#d

print (my_string. replace("a case sensitive", "object oriented"))

#e

print (my_string.index("a"))

#f

print (my_string. replace(" ",""))

#Question 2:- printing about yourself
Name='Akhilesh Goel'
SID=21104057
department='Electrical Engineering'
CGPA=9.9
print("Hey,%s Here!\nMy SID is %d\nI am from %s department and my CGPA is %s"%(Name,SID,department,CGPA))

#Question 3
#a
a=56
b=10
print (a&b)
#b
print (a|b)
#C
print (a^b)
#d
print(a<<2)
print (b<<2)
#e
print (a>>2)
print (b>>4)

#ques4
x=int(input('enter first no:'))
y=int(input('enter second no:'))
z=int(input('enter third no:'))
largest=x
for i in[x,y,z]:
    if largest<i:
        largest=i
print("largest no is: ",largest)

#ques5

#Taking input statement
a=str(input("Write your sentence or word and I will tell you whether it contains 'name' or not:- \n"))
#Using (if,else) conditionals
if 'name' in a:
    print("Yes")
else:
    print("No")

print("\n")

#ques6_To check if a triangle can be formed by given three lengths

a=int(input('side a:'))

b=int(input('side b:'))

c=int(input('side c:'))


if (a+b>c) and (b+c>a) and (c+a>b):
    print ("yes")
else:
    print("no")