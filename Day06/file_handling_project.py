from pathlib import Path
import os
def Reading_existing_files():
    path = Path("")
    items = path.rglob("*")
    for index , item in enumerate(items, start=1):
        print(f"{index} : {item}")

def createfile():
    try:
        name = input("Enter a File name you want to create :")
        p = Path(name)
        if not p.exists():
            with open(p , "w") as fs:
                data = input("Enter Content You want to write in your file : ")
                fs.write(data)
            
            print("FILE CREATED SUCCESSFULLY")
        else:
            print("File already Exists")
    except Exception as err:
        print(f"An error occured as {err} ")   
def readfile():
    try:
        name = input("Enter a file name you want to read :")
        p = Path(name)
        if p.exists():
            with open(p, "r") as fs:
                content = fs.read()
                print(content)
            
            print("FILE READED SUCCESSFULLY")
        else:
            print("File Not Exists")
    except Exception as err:
        print(f"An error occured as {err} ") 
def updatefile():
    try:
        name = input("Enter a file name that you want to update :")
        p = Path(name)
        if p.exists():
            print("Press 1 for Changing file name :")    
            print("Press 2 for overwrite the content in file :")  
            print("Press 3 for update content into file without overwriting :") 
            
        res = int(input("Enter you response :"))
        if res == 1 :
            name2 = input("Enter new name : ")
            p2 = Path(name2)
            p = p.rename(p2)
            print(f"New File name is : {p}")
        elif res == 2:
            with open(p , "w") as fs:
                data = input("Enter text that you want to overwrite in file :")
                fs.write(data)
            print("Content overwriten Successfully")
        elif res == 3:
            with open(p ,"a") as fs:
                data = input("Enter text that you want to append in file :")
                fs.write("" + data)
            print("Data appended Successfully")
        else:
            print("Invalid Choice!")
    except Exception as err:
        print(f"An error occured as {err} ") 

def deletefile():
    try:
        name = input("Enter a file name that you want to delete :")
        p = Path(name)
        if p.exists():
            os.remove(p)
            print("FILE REMOVED SUCCESSFULLY")
        else:
            print("File does not Exists")
    except Exception as err:
        print(f"An error occured as {err} ")
while True:
    print("Press 1 for Creating a File ")
    print("Press 2 for Reading a File ")
    print("Press 3 for Updating a File ")
    print("Press 4 for Deletion a File ")
    choice = int(input("Enter Your Response :"))
    if choice == 1:
        Reading_existing_files()
        createfile()
    if choice ==2:
        Reading_existing_files()
        readfile()
    if choice == 3:
        Reading_existing_files()
        updatefile()
    if choice == 4:
        Reading_existing_files()
        deletefile()
