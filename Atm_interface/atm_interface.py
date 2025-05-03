class ATM:
    def __init__(self, user_pin, user_balance=0):
        self.correct_pin = user_pin
        self.balance = user_balance
        self.logged_in = False

    def login(self):
        attempts = 3
        while attempts > 0:
            pin = input("Enter your 4-digit PIN: ")
            if pin == self.correct_pin:
                self.logged_in = True
                print("Login successful.\n")
                return
            else:
                attempts -= 1
                print(f"Incorrect PIN. Attempts left: {attempts}")
        print("Too many incorrect attempts. Exiting.")
        exit()

    def show_menu(self):
        while self.logged_in:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Select an option (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                self.logged_in = False
            else:
                print("Invalid choice. Please try again.")

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance:.2f}")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                self.balance += amount
                print(f"₹{amount:.2f} deposited successfully.")
            else:
                print("Enter a valid amount.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"₹{amount:.2f} withdrawn successfully.")
            else:
                print("Insufficient balance or invalid amount.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# ===== Main Program =====
if __name__ == "__main__":
    # You can change the PIN and balance for testing
    atm = ATM(user_pin="1234", user_balance=1000.0)
    atm.login()
    atm.show_menu()
