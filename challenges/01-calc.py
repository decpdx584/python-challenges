# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input("Choose an operation between add, subtract, multiply, and divide ")
num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))

def calculation(operation, num1, num2):
    if(operation == "add"):
        result = num1 + num2
        return result
    elif(operation == "subtract"):
        result = num1 - num2
        return result
    elif(operation == "multiply"):
        result = num1 * num2
        return result
    elif(operation == "divide"):
        result = num1 / num2
        return result
    else:
        print("Wrong operator")

print (calculation(operation, num1, num2))