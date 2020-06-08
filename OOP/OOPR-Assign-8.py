# OOPR-Assign-8

class Student:

    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None
        

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
