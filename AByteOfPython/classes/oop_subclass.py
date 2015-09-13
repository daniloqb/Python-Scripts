__author__ = 'daniloqb'


class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        print "Initializing school member {}".format(self.name)

    def tell(self):
        print "Name: {}, Age: {}".format(self.name, self.age)


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print "Initialized Teacher {}".format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print "Salary: {}".format(self.salary)


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print "Initialized Student {}".format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print "Marks: {}".format(self.marks)


t = Teacher('Morini', 43, 11000)
s = Student('Anderson', 22, 10)

member = [t, s]

for m in member:
    m.tell()
