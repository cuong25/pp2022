from re import sub
course=[]
student=[]
nc=0
ns=0
name0=str(0)
stumark={}
def numcourse():
    ns=input("Number of students in a class:")
def numcourse():
    nc=input("Number of courses:")
def Courseinfo():
        print("Enter 0 for course name if you want to stop inputting\n")
        while(1):
          name=input("Course name:")
     
          if name != name0: 
             id=input("Course id:")
             linec = f"{name}-{id}"
             course.append(linec)
          else :
             break   
def Studentinfo():
        print("Enter 0 for student name if you want to stop input\n")
        while(1):
          names=input("Student name:")
          if names != name0:
             id=input("Student id:")
             dOB=input("Stuent DOB:") 
             lines = f"{names}-{id}-{dOB}"
             student.append(lines)
          else :
             break                 
def Courselist():
    print("Course list:")
    for i in range(len(course)):
        print(course[i])
def Studentlist():
    print("Student list:")
    for i in range(len(student)):
        print(student[i])    
def Studentmark():
    s = input("Subject:")                                       
    mark=[]
    stumark[s]=mark
    for i in range(len(student)):
        m=input(f"{student[i]}'s mark in {s} is:")   
        mark.append(m)   
def ListStudentmark():
    s = input("Subject:")
    if s in stumark:
     print(f"Student {s} mark:")
     for i in range(len(student)):
        print(f"{student[i]}-mark:{stumark[s][i]}")    
    else:
        print("Subject not found,please use Studentmark() to add new course")
Courseinfo()
Studentinfo()
Courselist()
Studentlist()
Studentmark()
ListStudentmark()