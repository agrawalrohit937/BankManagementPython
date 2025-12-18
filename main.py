import json
import random
import string
from pathlib import Path

class Bank:

    database = 'data.json'
    data = []
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists ")
    except Exception as err:
        print(f"An exception occurred as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def Createaccount(self):
        info = {
            "name" : input("Tell your name :- "),
            "age" : int(input("Tell your age :- ")),
            "email" : input("Tell your Mail :- "),
            "pin" : int(input("Tell your 4 number PIN :- ")),
            "accountNo." : Bank.__accountgenerate(),
            "balance" : 0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry YOu cannot create your account")
        else:
            print("Account has been craeted successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number")

            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input("Please tell your account number :: ")
        pin = int(input("Please tell your PIN :: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        if userdata == False:
            print("Sorry No Data Found")
        else:
            amount = int(input("How much You want to deposit "))
            if amount > 10000 or amount < 0:
                print("Sorry the amount is too much you can deposit below 10000 and above 0")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully")

    def withdrawmoney(self):
        accnumber = input("Please tell your account number :: ")
        pin = int(input("Please tell your PIN :: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        if userdata == False:
            print("Sorry No Data Found")
        else:
            amount = int(input("How much You want to Withdraw "))
            if userdata[0]['balance'] < amount:
                print("Sorry You dont have that much money")
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrew successfully")

    def showdetails(self):
        accnumber = input("Please tell your account number :: ")
        pin = int(input("Please tell your PIN :: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        print("Your Information are ------- \n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accnumber = input("Please tell your account number :: ")
        pin = int(input("Please tell your PIN :: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("No such User found")
        else:
            print("You cannot change the age, Account Number, balance")
            print("fill the details for chnage or leave it empty if no change")

            newdata = {
                "name" : input("Please tell name or press Enter : "),
                "email" : input("Please tell your email or press Enter to skip"),
                "pin" : input("enter new pin or press Enter")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']

            newdata['age'] = userdata[0]['age']
            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
            Bank.__update()
            print("Details updated successfully")

    def delete(self):
        accnumber = input("Please tell your account number :: ")
        pin = int(input("Please tell your PIN :: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no such data exists")
        else:
            check = input("Press y if you actually want to delete the account or press n : ")

            if check == 'n' or check == 'N':
                print("ByPasses")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted Successfully ")
                Bank.__update()     # to dummy to json file

user = Bank()


print("Press 1 for creating an account ")
print("Press 2 for Depositing the money in the bank ")
print("Press 3 for withdrawing the money ")
print("Press 4 for details")
print("Press 5 for updating the details ")
print("Press 6 for deleting your account ")

check = int(input("Tell your response :- "))

if check == 1:
    user.Createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.delete()