semester_result = {}
while True:
        semester_result["Name"] = input("Enter Subject Name (Or type 'Exit' to finish) :")
        semester_result["Marks"] = int(input(f"Enter Marks of :  {semester_result["Name"]}  (Out of 100) :"))
        for i in semester_result:
            sheet =semester_result[i]
        print(sheet)
        
    