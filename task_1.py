# A program to allow a user to enter his/her name and their age and displaying them on the screen
#using f-string method

name = input("What is your name? ")
age= int(input("Enter your age: "))

print(f"""
    Hello {name}, you are {age} years old
""")