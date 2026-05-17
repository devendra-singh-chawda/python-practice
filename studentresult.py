
print("      Student Result System")
print(" Made by Devendra Singh Chawda")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

maths = float(input("Enter Maths marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
english = float(input("Enter English marks: "))
computer = float(input("Enter Computer marks: "))

total = maths + physics + chemistry + english + computer
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

if maths >= 35 and physics >= 35 and chemistry >= 35 and english >= 35 and computer >= 35:
    result = "Pass"
else:
    result = "Fail"

print("\n RESULT ")
print("Student Name:", name)
print("Roll Number:", roll_no)
print("Maths:", maths)
print("Physics:", physics)
print("Chemistry:", chemistry)
print("English:", english)
print("Computer:", computer)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)