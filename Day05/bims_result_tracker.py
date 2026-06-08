semester_result = {}
while True:
    try:
        name = input("Enter Subject Name or (Type 'exit' to see Complete Mark Sheet)  :  ")
        if name.lower() == "exit":
            sub_count = 0
            obtained_marks = 0
            for subject , numbers in semester_result.items():
                print(subject ,  numbers)
                obtained_marks += numbers
                sub_count = sub_count + 1
            total_marks = sub_count * 100
            percentage = (obtained_marks / total_marks) * 100
            print(f"Total Obtained Marks are {obtained_marks}")
            print(f"Percentage : {percentage}")
            if percentage >= 85:
                print("Grade : 'A' ")
            elif percentage >= 76:
                print("Grade : 'B' ")
            elif percentage >= 65:
                print("Grade : 'C' ")
            elif percentage >= 50:
                print("Grade : 'D' ")
            else:
                print("Grade : 'F' ")
            break
        else:
            marks = int(input(f"Enter Obtained Marks of {name} Out of 100 :  "))
            if marks >= 0 and marks <= 100:
                semester_result[name] = marks
            else:
                print("Error! Marks Should Not be Greater then 100")
    except Exception as err:
        print(f"An error occured as {err}")
            
        