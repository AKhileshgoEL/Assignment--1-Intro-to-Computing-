#question 1: take average 3 numbers taken from user
#answer: Source code:

number_1=int(input("Enter number 1: "))
number_2=int(input("Enter number 2: "))
number_3=int(input("Enter number 3: "))

#average
avg=(number_1+number_2+number_3)/3
print(avg)

#question 2: compute a person's income tax
#answer: source code
#all avlues are in $S

gross_income=input("Enter gross income: ")
gross_income=float(gross_income)

standard_deduction=10000
dependence=input("Enter the no. of dependents: ")
dependence=int(dependence)
#there is a $3000 deduction for each dependents
dependent_deduction=3000

#tax rate=20%
taxable_income=gross_income-standard_deduction-(dependent_deduction*dependence)
tax=(taxable_income*20/100)
print("tax:")
print(tax)

#question 3:make a list of NAME,SID,GENDER,COURSE NAME, CGPA
#answer: source code

name=input("Enter Name:")
sid=input("Enter SID:")
gender=input("Enter Gender:")
course_name=input("Enter Course_Name:")
cgpa=float(input("cgpa"))
#our list now name as student_info
student_info=[name,sid,gender,course_name,cgpa]
print("student_info", student_info)

#question 4: make a list of marks of 5 students and show them in sorted manner
#answer: source code
student_1marks=int(input("Enter student 1 marks:"))
student_2marks=int(input("Enter student 2 marks:"))
student_3marks=int(input("Enter student 3 marks:"))
student_4marks=int(input("Enter student 4 marks:"))
student_5marks=int(input("Enter student 5 marks:"))

my_list=[student_1marks,student_2marks,student_3marks,student_4marks,student_5marks]
print("list:", my_list)
print("sorted list(decreasing order):")
my_list.sort()
print(my_list)

#question 5:
#(a) print nad then remove 4th element from the lsit and let it print the new list
#(b) remove 'Black' and 'Pink' from the list and replace it with 'Purple'

my_list=['Red','Green','Black','Pink','Yellow']
#(a) part
print('(a)')
print(my_list)
# remove 4th term in Black
my_list.remove('Black')
print(my_list)

#Q5(b)
#Making colour list of the given colors
my_list=['Red','Green', 'White', 'Black', 'Pink', 'Yellow']
#To add an element we use insert function
my_list.insert(3, "Purple")
print('The updated colour list after removing "Black" and "Pink" and replacing them with "Purple" :-', my_list[0:4] + my_list[6:], '\n')