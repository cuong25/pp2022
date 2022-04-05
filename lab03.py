import math
import curses
import re
from xml.dom.minidom import Element
import numpy as np
class Student:
    def __init__(self,id,name,dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
    def studentID(self):
        return self.__id
    def studentName(self):
        return self.__name
    def studentDob(self):
        return self.__dob

class listStudent:
    def __init__(self):
        self.__list = []
    def getList(self):
        return self.__list
    def addStudent(self,student):
        self.__list.append(student)
    def Display_Student_Information(self):
        print("The number of Students: ".format(len(self.__list)))
        for student in self.__list():
            print("Student name: ,Student ID: ,Student dob: ".format(student.getName(), student.getID, student.getdob))
class Course:
    def __init__(self,id,name):
        self.__id = id
        self.__name = name
        self.__mark = []
    def studentMark(self):
        return self.__mark
    def studentName(self):
        return self.__name
    def studentID(self):
        return self.__id
    def addMark(self, mark):
        self.studentMark().append(mark)
    def Display_Mark(self):
        if (len(self.studentMark())==0):
            print("Invalid mark.")
        else:
            print("Mark for course: {}".format(self.studentName()))
            for i in range(0, len(self.studentMark())):
               print("Student name: {}, Mark: {}".format(self.studentMark()[i].studentName(), self.studentMark()[i].studentMark()))

class Courselist:
    def __init__(self):
        self.__list = []
    def getList(self):
        return self.__list
    def addCourse(self, course):
        self.__list.append(course)
    def getCoursebyID(self, id):
        for course in self.__list:
            if course.getID() == id:
                return course
        return None
    def Display_Course_Info(self):
        print("Number of course: {}".format(len(self.__list)))
        for course in self.__list:
            print("Course ID:{}, Course: {}".format(course.studentID(), course.studentName()))
class Mark:
    def __init__(self, id, name, mark):
        self.__id = id
        self.__name = name
        self.__mark = mark
    def studentName(self):
        return self.__name
    def studentMark(self):
        return self.__mark
    def studentID(self):
        return self.__id
def Number_of_students():
    x = int (input("Number of student in class: "))
    return x
def Number_of_courses():
    Course_number = int(input("Number of course: "))
    return Course_number
def Student_info(Number_Student, student):
    for i in range(Number_Student):
        Student_ID = input("ID: ")
        Student_name = input("Name: ")
        Student_dob = input("Dob: ")
        student.getList().append(Student(Student_ID, Student_name, Student_dob))
def Course_information(CourseNumber, course):
    for i in range(CourseNumber):
        Course_ID = input("Course id: ")
        Course_name = input("Course name: ")
        course.getList().append(Course(Course_ID,Course_name))
def Course_mark(course, student):
    while True:
        id = input("Course id(0 to exit): ")
        if id == "0":
            break
        course = course.getCourseID(id)
        if course == None:
            print("Invalid Course!")
        else:
            for i in range(len(student.getList())):
                mark = input("Student mark {} : ".format(student.getList()[i].studentName()))
                course.addMark(Mark(student.getList()[i].studentID(),student.getList()[i].studentName(), mark))
def ShowCourseMark(course):
    while True:
        id = input("Course ID to show mark(0 to exit): ")
        if id == "0":
            break
        course = course.getCourseByID(id)
        if course == None:
            print("Invalid course")
        else:
            course.Display_Marks()
class GPA:
    def in_GPA(self, course):
        total_credit = 0
        for i in range(0, len(course)):
            total_credit = int(self.mark[i][2])
            self.GPA = int(self.marks[i][1] * self.marks[i][2])
            self.GPA = math.floor((self.GPA / total_credit) * 20) /20
    self_course = input("Select course: ") 

student = listStudent()
course = Courselist()
numberStudents = Number_of_students()
Student_info(numberStudents, student)
student.Display_Student_Information()

CourseNumber = Number_of_courses()
Course_information(CourseNumber,course)
course.Display_Course_Info()
Course_mark(course, student)
ShowCourseMark(course)

