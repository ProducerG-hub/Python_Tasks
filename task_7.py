# A program to create a function that will be used to check whether the number is prime or not by returning true / false
# Remember that Prime number is any number greater than 1, that is divisible by 1 or itself without reminder

def is_prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if (num%i==0):
            return False
        
    return True

print("================ PRIME NUMBER CHECKER ===================")
number = int(input("Enter a number to be checked: "))

print(is_prime(number))