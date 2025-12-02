import sys

class ATM:
    def __init__(self, initial_balance=5000, pin=1234):
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []

    def check_pin(self):
        try:
            user_pin = int(input("Enter your 4-digit PIN: "))
            if user_pin == self.pin:
                return True
            else:
                print("❌ Incorrect PIN.")
                return False
        except ValueError:
            print("❌ Invalid input. Please enter numbers only.")
            return False

    def display_menu(self):
        print("\n" + "="*30)
        print(" WELCOME TO STUDENT BANK ATM")
        print("="*30)
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Mini Statement")
        print("5. Exit")
        print("="*30)

    def run(self):
        if not self.check_pin():
            return

        while True:
            self.display_menu()
            choice = input("Select an option (1-5): ")

            if choice == '1':
                print(f"\n💰 Current Balance: ₹{self.balance}")
            
            elif choice == '2':
                amount = float(input("\nEnter amount to deposit: "))
                if amount > 0:
                    self.balance += amount
                    self.transaction_history.append(f"Deposited: +₹{amount}")
                    print(f"✅ ₹{amount} Deposited Successfully!")
                else:
                    print("❌ Invalid amount.")

            elif choice == '3':
                amount = float(input("\nEnter amount to withdraw: "))
                if 0 < amount <= self.balance:
                    self.balance -= amount
                    self.transaction_history.append(f"Withdrew: -₹{amount}")
                    print(f"✅ Please collect your cash: ₹{amount}")
                else:
                    print("❌ Insufficient funds or invalid amount.")

            elif choice == '4':
                print("\n--- Mini Statement ---")
                for record in self.transaction_history[-5:]: # Show last 5
                    print(record)
                if not self.transaction_history:
                    print("No transactions yet.")

            elif choice == '5':
                print("\n👋 Thank you for using Student Bank ATM. Goodbye!")
                sys.exit()
            
            else:
                print("❌ Invalid choice. Try again.")

# Run the system
if __name__ == "__main__":
    my_atm = ATM()
    my_atm.run()