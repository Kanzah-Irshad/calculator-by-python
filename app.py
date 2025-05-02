# -------------------------------------- A calculator using conditions ----------------------------------------
#----------------------------------------------TASK 1----------------------------------------------------------
# Create a calculator using conditions, You will take two numbers as input from the user, then ask the user for their choice. Depending on user's choice, you have to perform the operation and print the result.
num1 = float(input("ENTER THE FIRST NUMBER:"))
num2 = float(input("ENTER THE SECOND NUMBER:"))

print ("\nChoose an operation:")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")

choice = input("ENTER THE NUMBER OF YOUR CHOICE:")

if choice == '1':
    result = num1 + num2
    print (f"THE RESULT OF ADDITION IS:{result}")
elif choice == '2':
    result = num1 - num2
    print (f"THE RESULT OF SUBTRACTION IS:{result}")
elif choice == '3':
    result = num1 * num2
    print (f"THE RESULT OF MULTIPLICATION IS:{result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else :
        print("Error: A number cannot be divided by 0")
else :
    print("Invalid choise: Please select a valid option (1/2/3/4).")        