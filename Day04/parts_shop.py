parts = {
    "silencer" : 4500,
    "carburator" : 3200,
    "indicator" : 2000,
    "lights" : 1200
}
print(f"Available Parts and their Prices {parts}")
customer_choice = input("Enter a Part Name You Want to Purchase: ")
quantity =  int(input("Enter Quantity :"))
bill = 0
# found = False
# for i in parts:
#     if customer_choice == i and quantity > 0:
#         bill = parts[customer_choice] * quantity
#         print(f"Your Bill is : {bill}")
#         found = True
#         break
# if(found == False):
#     print("Parts Not Available or Invalid Quantity")

if customer_choice in parts:
         if quantity > 0:
            bill = parts[customer_choice] * quantity
            print(f"Your Bill is : {bill}")
            print("Thank You For Shopping")
         else:
            print("Part Not Available or invalid quantity")




