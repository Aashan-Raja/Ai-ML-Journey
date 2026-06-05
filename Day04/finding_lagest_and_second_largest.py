list = [99, 50 , 101 , 10 , 85, 100  , 3]
largest = list[0]
sec_largest = list[0]
for i in list:
    if i > largest:
        largest = i
    elif i > sec_largest:
        sec_largest = i
     
print(f"Largest Number is : {largest} , Second largest Number is: {sec_largest}")

