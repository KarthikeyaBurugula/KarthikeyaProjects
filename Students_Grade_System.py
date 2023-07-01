#Creating Student Grading System and implementing several modules of it in order to know all the details and scores and grades and rankinks aswell
#Tools used
#Iterables like Lits, Dictionaries for Storing the data
#Iterators like For loop for interating through lists and dictionaries.

#Module 1 Storing the Data and Printinf the Data
#Creating a dictionary for Storing data.

Student_data={}
#Taking how many students.
n=int(input("Enter the no of Students "))
#Inserting the data using for loop

for i in range(n):
    #Taking the student name input
    c=input("Enter the Student Name ")
    #Taking no of subjects input.
    no_s=int(input("Enter How many Subjects "))
    #Creating a Sub dictionary for subject data
    sub_data={}
    #Inserting data into sub_data
    for j in range(no_s):
        #Taking subject input.
        s=input("Enter the subject name ")
        #Taking Marks input.
        marks=int(input("Enter the Marks "))
        sub_data[s]=marks
    Student_data[c]=sub_data

print("The total data is ",Student_data)

#----Module-1 END-----#

#Module 2 Generating the Averages.
Average={}

for i in range(len(Student_data)):
    c=input("Enter the name of the student ")
    av=sum(Student_data[c].values())/len(Student_data[c])
    Average[c]=av

print("The Averages of Students are as follows ",Average)

print("The Fees of Masters at university of Houston Texas is 4000000")
print("The student whose average is 90 or above would receive a 20% Scholarship for Master Degree in University of Houston Texas ")
print("The student whose aggregate is 80 and above and below 90 would receive Scholarship of 10%")


#Module 3 Generating the Grades
Grades={}
for i in range(len(Average)):
    c=input("Enter the Student Name ")
    if Average[c]>90 and Average[c]<=100:
        Grades[c]='A'
    elif Average[c]>80 and Average[c]<=90:
        Grades[c]='B'
    elif Average[c]>50 and Average[c]<=70:
        Grades[c]='C'
    elif Average[c]>36 and Average[c]<=50:
        Grades[c]='D'
    elif Average[c]<35:
        Grades[c]='F'
print(Grades)

#Module 4 Deciding the topper
#Separating the keys and values as Names and respective averages.
k=list(Average.keys())
v=list(Average.values())
#First we retrive maximum values from v and find out its index
#Then we will access the same index in k
print("The Topper of the Batch is ",k[v.index(max(v))],"With ",max(v)," Aggregate")

#Module 5 Deciding the Failures

print("The Failures are ")

l=list(filter(lambda i:i<35,v))
index=[]
for i in l:
            c=v.index(i)
            index.append(c)

for i in index:
    print(k[i])

#Module 6 Deciding the Scholarships
ni=list(filter(lambda x:x>=90,v))
mi=list(filter(lambda x:x>=80 and x<=90,v))

ni_index=[]
mi_index=[]

for i in ni:
    c=v.index(i)
    ni_index.append(c)

for i in mi:
    d=v.index(i)
    mi_index.append(d)

print("The Students with 20% Scholarship are ")
for i in ni_index:
    print(k[i])

print("The Students with 10% Scholarship are ")
for i in mi_index:
    print(k[i])

