def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Select option from below\n" , "1.add\n", "2.subtract\n","3.multiply\n","4.divide" )
choice = input("Enter your choice: ")
if choice in ('1','2','3','4'):
    num1=float(input('Enter ur number1: '))
    num2=float(input("Enter ur number2: "))
    if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
else:
        print("Invalid Input")
