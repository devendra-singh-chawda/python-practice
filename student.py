class Student:

    def __init__(self, name, marks):

        self.name = name

        self.marks = marks

    def display(self):

        print("\nName:", self.name)

        print("Marks:", self.marks)

    def grade(self):

        if self.marks >= 90:

            print("Grade: A")

        elif self.marks >= 75:

            print("Grade: B")

        else:

            print("Grade: C")

student1 = Student("Devendra", 90)

student2 = Student("Rahul", 85)

student1.display()

student1.grade()

student2.display()

student2.grade()
