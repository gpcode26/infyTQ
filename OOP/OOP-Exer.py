#OOPR-Exer-3

class Employee:
    def __init__(self):
        self.name = None
        self.age = None
        self.salary = None

    def details(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        print('Name:', self.name)
        print('Age:', self.age)
        print('Salary:', self.salary)

Jack = Employee()
Jack.details("Jack", 24, 30000)
Jill = Employee()
Jill.details("Jill", 27, 40000)



#OOPR-Exer-4

class Athlete:

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def running(self):
        if self.__gender == "girl":
            print("150mtr running")
        else:
            print("200mtr running")


maria = Athlete("Maria", "girl")
maria.running()
