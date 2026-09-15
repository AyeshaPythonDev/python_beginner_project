def add(a,b):
  return a + b
def subtract(a,b):
  return a - b
def multiply(a,b):
  return a * b
def divide(a,b):
  return a/b
print("---Simple Calculator---")
print("Operations: + , - , * , /")
while True :
  try:
    num1 = float(input("Enter first number : "))
    operator = input("Enter operator ( +, -, *, /) : ")
    num2 = float(input("Enter second number : ")) 
    if operator == "+":
       result = add(num1 , num2)
       print(f"Result : {num1} + {num2} = {result}")
    elif operator == "-":
        result = subtract(num1 , num2)
         print(f"Result: {num1} - {num2} = {result}")
    elif operator == "*":
          result = multiply(num1 , num2)
          print(f"Result : {num1} * {num2} = {result}")
    elif operator == "/" :
          if num2 == 0 :
            print("Error : Cannot divide by zero ! ")
          else:
            result = divide(num1 , num2)
            print(f"Result:{num1} / {num2} = { result}")
          else : 
            print("Invalid operator ! Please use +, -, *, /")
            again = input("Do you want to calculate again? (yes/no) : ").lower()
          if again != 'yes":
           print("Calculator closed. Thank you!")
           break
  except ValueError : 
          print("Error : Please enter valid numbers only!")

    
  
