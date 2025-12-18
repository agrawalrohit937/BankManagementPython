import streamlit as st
from aimain import Bank

st.set_page_config(page_title="Bank Management System", layout="centered")
bank = Bank()

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "View Account Details",
        "Update Details",
        "Delete Account"
    ]
)

# ---------------- CREATE ACCOUNT ----------------
if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create Account"):
        success, result = bank.create_account(name, age, email, int(pin))
        if success:
            st.success("Account Created Successfully")
            st.write("Account Number:", result["accountNo."])
        else:
            st.error(result)

# ---------------- DEPOSIT ----------------
elif menu == "Deposit Money":
    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        success, msg = bank.deposit(acc, int(pin), amount)
        if success:
            st.success(f"New Balance: ₹{msg}")
        else:
            st.error(msg)

# ---------------- WITHDRAW ----------------
elif menu == "Withdraw Money":
    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        success, msg = bank.withdraw(acc, int(pin), amount)
        if success:
            st.success(f"New Balance: ₹{msg}")
        else:
            st.error(msg)

# ---------------- VIEW DETAILS ----------------
elif menu == "View Account Details":
    st.subheader("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("View"):
        success, user = bank.get_details(acc, int(pin))
        if success:
            st.json(user)
        else:
            st.error(user)

# ---------------- UPDATE DETAILS ----------------
elif menu == "Update Details":
    st.subheader("Update Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)", type="password")

    if st.button("Update"):
        success, msg = bank.update_details(
            acc,
            int(pin),
            name if name else None,
            email if email else None,
            int(new_pin) if new_pin else None
        )
        if success:
            st.success(msg)
        else:
            st.error(msg)

# ---------------- DELETE ----------------
elif menu == "Delete Account":
    st.subheader("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        success, msg = bank.delete_account(acc, int(pin))
        if success:
            st.success(msg)
        else:
            st.error(msg)
