class Student:

    def __init__(self,fullname):
        self.name=fullname
        print("adding student name")

obj1=Student("afham")
print(obj1.name)

obj2=Student("ali")
print(obj2.name)