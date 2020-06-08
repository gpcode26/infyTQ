# OOPR-Assign-9

courses = {
    1001: 25575,
    1002: 15500
}

class Student:

    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None
        self.__course_id = None
        self.__fees = None


    def validate_marks(self):
        if self.__marks in range(0, 101):
            return True
        return False


    def validate_age(self):
        if self.__age > 20:
            return True
        return False

    def check_qualification(self):
        if self.validate_age() and self.validate_marks() and self.__marks >= 65:
            return True
        return False

    def choose_course(self, course_id):
        if course_id in courses.keys():
            self.__course_id = course_id
            if self.__marks > 85:
                self.__fees = courses[course_id]*0.75
            else:
                self.__fees = courses[course_id]
            return True
        return False


    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id


    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


    def get_course_id(self):
        return self.__course_id

    def get_fees(self):
        return self.__fees


maddy=Student()
maddy.set_student_id(1004)
maddy.set_age(21)
maddy.set_marks(65)
if(maddy.check_qualification()):
    print("Student has qualified")
    if(maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")

