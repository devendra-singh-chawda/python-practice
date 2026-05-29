class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def display(self):

        print("Name:", self.name)
        print("Marks:", self.marks)

student1 = Student("Devendra", 92)

student1.display()