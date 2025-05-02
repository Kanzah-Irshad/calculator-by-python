# -------------------------------------- A calculator using conditions ----------------------------------------
#----------------------------------------------TASK 1----------------------------------------------------------
# Create a calculator using conditions, You will take two numbers as input from the user, then ask the user for their choice. Depending on user's choice, you have to perform the operation and print the result.

# take 2 numbers as  inputs from the user
num1 = float(input("ENTER THE FIRST NUMBER:")) # input() function user se input leta hai (text format me)
num2 = float(input("ENTER THE SECOND NUMBER:")) # float() isliye use kiya gaya hai taake decimal numbers bhi input kiye ja sakein

# asking user for their operation choices 
print ("\nChoose an operation:")  # User ko options dikhana (menu banake)
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")

# Take user's choice
# Jo option user enter karega (1, 2, 3 ya 4), woh choice variable me store ho jayega
choice = input("ENTER THE NUMBER OF YOUR CHOICE:")

# perform the operation based on the user's choice
if choice == '1':
    result = num1 + num2
    print (f"THE RESULT OF ADDITION IS:{result}")
# agar user ne '1' choose kiya to addition hoga

elif choice == '2':
    result = num1 - num2
    print (f"THE RESULT OF SUBTRACTION IS:{result}")
# agar user ne '2' choose kiya to subtraction hoga

elif choice == '3':
    result = num1 * num2
    print (f"THE RESULT OF MULTIPLICATION IS:{result}")
# agar '3' choose kiya to multiplication hoga

elif choice == '4':
    if num2 != 0: # ye not equal to check krne k leye lagaya k num2 0 na ho warna error aayega cz division by zero is not possible
        result = num1 / num2
        print(f"The result of division is: {result}")
# agar '4' choose kiya, toh division hoga
    else :
        print("Error: A number cannot be divided by 0")
    # agar user ne num2 0 dya to ye error show hoga
else :
    print("Invalid choise: Please select a valid option (1/2/3/4).")   
# agar user ne koi ghalat input diya to ye error msg show karega
