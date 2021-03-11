# Python 3 program to find factorial of a number 
def factorial(n): 
      
    # single line to find factorial
    #recursive method
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
  
print("Program to find factorial of number")
num = int(input("Enter the number: ")); 
print("Factorial of",num,"is", 
factorial(num))
