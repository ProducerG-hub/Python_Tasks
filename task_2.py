# Program to accept the user input (in string format) then checking if the input is a number or not
# If is a number the program should give the square of the number and state whether the number is Positive or negative if not Invalid value
# NB: A number must not be equal to zero
user_input = input("Enter your input: ")
try:
    num = int(user_input)
    if num != 0:
      if num<0:
         print(f"""
            The number {num} is Negative   
            Square of number is: {num*num}
            """)
      else:
         print(f"""
             The number {num} is Positive
             Square of number is: {num*num}
             """)
     
    else:
       print("Only non-zero numbers are required")
    
except ValueError:
    print("Invalid Value: Not a number")