class Employee:
    def work(self):
        print("Employee works")


class Student:
    def study(self):
        print("Student studies")



class WorkingStudent(Employee, Student):
    # Наследование от классов Employee и Student
    pass

tom = WorkingStudent()

tom.work()
tom.study()

print(*WorkingStudent.mro(), sep='\n')