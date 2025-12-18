import json
import random
import string
from pathlib import Path

class Bank:
    DATABASE = "data.json"

    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        if Path(self.DATABASE).exists():
            with open(self.DATABASE, "r") as f:
                return json.load(f)
        return []

    def save_data(self):
        with open(self.DATABASE, "w") as f:
            json.dump(self.data, f, indent=4)

    def generate_account_number(self):
        chars = (
            random.choices(string.ascii_letters, k=3) +
            random.choices(string.digits, k=3) +
            random.choices("!@#$%^&*", k=1)
        )
        random.shuffle(chars)
        return "".join(chars)

    def find_user(self, acc_no, pin):
        for user in self.data:
            if user["accountNo."] == acc_no and user["pin"] == pin:
                return user
        return None

    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "Age must be 18+ and PIN must be 4 digits"

        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo.": self.generate_account_number(),
            "balance": 0
        }

        self.data.append(user)
        self.save_data()
        return True, user

    def deposit(self, acc_no, pin, amount):
        user = self.find_user(acc_no, pin)
        if not user:
            return False, "Invalid credentials"

        if amount <= 0 or amount > 10000:
            return False, "Deposit must be between 1 and 10000"

        user["balance"] += amount
        self.save_data()
        return True, user["balance"]

    def withdraw(self, acc_no, pin, amount):
        user = self.find_user(acc_no, pin)
        if not user:
            return False, "Invalid credentials"

        if amount <= 0:
            return False, "Invalid amount"

        if user["balance"] < amount:
            return False, "Insufficient balance"

        user["balance"] -= amount
        self.save_data()
        return True, user["balance"]

    def get_details(self, acc_no, pin):
        user = self.find_user(acc_no, pin)
        if not user:
            return False, "Invalid credentials"
        return True, user

    def update_details(self, acc_no, pin, name=None, email=None, new_pin=None):
        user = self.find_user(acc_no, pin)
        if not user:
            return False, "Invalid credentials"

        if name:
            user["name"] = name
        if email:
            user["email"] = email
        if new_pin and len(str(new_pin)) == 4:
            user["pin"] = new_pin

        self.save_data()
        return True, "Details updated"

    def delete_account(self, acc_no, pin):
        user = self.find_user(acc_no, pin)
        if not user:
            return False, "Invalid credentials"

        self.data.remove(user)
        self.save_data()
        return True, "Account deleted"
