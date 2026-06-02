choice = 0
while choice <= 5:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter Your Choice From 1 To 5:"))
    if choice == 1:
        num1 = int(input("Enter First Number:"))
        num2 = int(input("Enter Second Number:"))
        print("Addition is:", num1 + num2)
    elif choice == 2:
        num1 = int(input("Enter First Number:"))
        num2 = int(input("Enter Second Number:"))
        print("Subtraction is:", num1 - num2)
    elif choice == 3:
        num1 = int(input("Enter First Number:"))
        num2 = int(input("Enter Second Number:"))
        print("Multiplication is:", num1 * num2)
    elif choice == 4:
        num1 = int(input("Enter First Number:"))
        num2 = int(input("Enter Second Number:"))
        print("Division is:", num1 / num2)
    else:
        if choice == 5:
            print("Thank You For Using This Calculator")
            break 
        else:  
            print("Invalid Choice")
    

     
