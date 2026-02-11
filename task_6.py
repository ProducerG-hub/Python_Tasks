# A program to create the dictionary which carries a name of student as key and marks as the value (name:marks)
# Then being able of looping the values on dictionary and print the name of student and the grade (name->grade)

students = {
    "David":85,
    "Stephen":67,
    "Gwamaka":55,
    "Mlue":23
}

def grade(name,marks):
        if marks<0 or marks>100:
            return f"{name}-> Invalid Marks Range"
        elif marks>=80:
            return f"{name}-> A"
        elif marks>=60:
            return f"{name}-> B"
        elif marks>=50:
            return f"{name}-> C"
        elif marks>=40:
            return f"{name}-> D"
        else:
            return f"{name}-> F"

for name,marks in students.items():
    print(grade(name,marks))