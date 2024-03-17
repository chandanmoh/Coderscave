class ExpenseManager:
    def __init__(self):
        self.balance_sheet = {}

    def add_expense(self, payer, amount, *users):
        share = amount / len(users)
        if payer not in self.balance_sheet:
            self.balance_sheet[payer] = 0
        self.balance_sheet[payer] -= amount
        for user in users:
            if user not in self.balance_sheet:
                self.balance_sheet[user] = 0
            self.balance_sheet[user] += share

    def show_balance(self):
        for person, balance in self.balance_sheet.items():
            print(f"{person}: {balance}")


if __name__ == "__main__":
    manager = ExpenseManager()

    while True:
        payer = input("Enter payer's name (or 'done' to finish): ")
        if payer.lower() == "done":
            break
        amount = float(input("Enter the expense amount: "))
        users = input("Enter names of people splitting the expense (comma-separated): ").split(",")
        manager.add_expense(payer, amount, *users)

    print("\nBalance Sheet:")
    manager.show_balance()

