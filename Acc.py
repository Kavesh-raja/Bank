class Account_details:
    def __init__(self,data,index):
        self.name = data[index]["name"]
        self.acc_num = data[index]["account number"]
        self.balance = data[index]["Balance"]

        print(f"Account holder:{self.name}\nAccount number:{self.acc_num}\nAccount Balance:{self.balance}$")