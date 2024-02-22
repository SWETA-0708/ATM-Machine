class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def display_balance(self):
        print(f"Your current balance is ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Your new balance is ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Cannot complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Your new balance is ${self.balance}")

def main():
    print("Welcome to the ATM!")

    initial_balance = float(input("Enter your initial balance: "))
    atm = ATM(initial_balance)

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            atm.display_balance()
        elif choice == '2':
            deposit_amount = float(input("Enter the amount to deposit: "))
            atm.deposit(deposit_amount)
        elif choice == '3':
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            atm.withdraw(withdraw_amount)
        elif choice == '4':
            print("Thank you for using the ATM. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
