'''
import json
filename = "example.json"
entry ={
    "name": "abc",
    "accont number": "xxxxxxxx001",
    "Balance": "100000000$"
  }
with open(filename,"r") as file:
    data = json.load(file)
data.append(entry)
with open(filename,"w") as file:
    json.dump(data,file)
'''
import json
from Acc import Account_details

filename = "example.json"
print("Welcome to KR Bank ", "How can I Help You?", "Account Details", "Create Account", "Deposite", "Withdraw",
      sep="\n")
inp = input()
with open(filename, "r") as f:
    data = json.load(f)
if inp == "Account Details":
    name = input("Enter your name:")
    for i in range(len(data)):
        if data[i]["name"] == name:
            user = Account_details(data, i)

elif inp == "Create Account":
    print("For the purpose of Account Creation 200$ will be deducted from your account.")
    name = input("Enter Your name:")
    amount = int(input('Enter the amount you want to Deposite '))
    new_user = {"name":name, "account number":f"xxxxxxx{len(data)+1}","Balance":f"{amount-200}"}
    data.append(new_user)
    with open(filename, "w") as file:
        json.dump(data, file)
    print("Successfully Account created!")

elif inp =="Deposite":
    name =input("Enter your name")
    amount = int(input("Enter the amount you want to Deposite"))
    for i in range(len(data)):
        if data[i]["name"] == name:
            new_bal = int(data[i]["Balance"])+amount
            data[i]["Balance"]=new_bal
            with open(filename, "w") as file:
                json.dump(data, file)
            print("Successfully amount Deposited to your bank account")

elif inp =="Withdraw":
    name =input("Enter your name:")
    amount = int(input("Enter the amount you want to Withdraw:"))
    for i in range(len(data)):
        if data[i]["name"] == name:
            new_bal = int(data[i]["Balance"])-amount
            data[i]["Balance"]=new_bal
            with open(filename, "w") as file:
                json.dump(data, file)
            print("Successfully amount Withdrawen from your bank account.")




