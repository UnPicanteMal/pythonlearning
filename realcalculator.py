#Define the equations

#Addition
def add(x, y):
    return x + y

#Substraction
def substract(x, y):
    return x - y 

#Multiplication
def multiply(x, y):
    return x * y 

#Division
def divide(x, y):
    return x / y 

print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

while True:
    #Ask user for an operation
    choice = input("Select an operation (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("What's x: "))
        num2 = float(input("What's y: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", substract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break

    else:
        print("Invalid input")