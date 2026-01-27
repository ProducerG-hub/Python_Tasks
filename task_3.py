# A program to accept the input of the marks of the student, and determine the grade of the student
marks = float(input("Enter Marks of the student: "))

try:
    if marks <0 or marks>100:
     print("Invalid Range of marks")
    elif marks<40:
     print("Grade:F")
    elif marks<60:
     print("Grade:C")
    elif marks<80:
     print("Grade:B")
    elif marks<=100:
     print("Grade:A")

except ValueError:
  print("Invalid Input")
