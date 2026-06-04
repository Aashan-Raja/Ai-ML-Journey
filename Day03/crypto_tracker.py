data = {}
while True:
    choice = input("Do you want to add  cryptocurrency? (yes/no) ")
    if choice.lower() == "yes":      
        data["Name"] = input("Enter the name of the cryptocurrency! ")
        data["Entry_Price"] = float(input("Enter the Entry price of the cryptocurrency! "))
        data["Buying_Amount"] = float(input("Enter the buying amount of the cryptocurrency! "))
        break
    elif choice.lower() == "no":
        print("Thank you for using the cryptocurrency tracker!")
        break   
for i in [data["Name"]]:
        current_live_price = float(input(f"What is the Current Live Price of { i } coin!"))
total_investment = data["Entry_Price"] * data["Buying_Amount"]
current_value = current_live_price * data["Buying_Amount"]
profit_loss = current_value - total_investment
if profit_loss > 0 :
     print(f"You are in profit of {profit_loss}usdt!")
else:
     print(f"You are in loss of {profit_loss}usdt!")