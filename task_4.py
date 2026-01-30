#A program to print the numbers from 1-50 but considering  multiples of 3 (fizz), 
#multiple of 5 (Buzz) and multiple of both 3 and 5 (FizzBuzz)
for num in range (1,51):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)