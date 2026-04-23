class BankAccount_eas:
    def __init__(self_eas, balance_eas):
        self_eas.__balance = balance_eas

    def deposit_eas(self_eas, amount_eas):
        self_eas.__balance += amount_eas

    def withdraw_eas(self_eas, amount_eas):
        if amount_eas <= self_eas.__balance:
            self_eas.__balance -= amount_eas
        else:
            print("Insufficient funds")

    def get_balance_eas(self_eas):
        return self_eas.__balance

account_eas = BankAccount_eas(5000)
account_eas.deposit_nbs(1000)
account_eas.withdraw_nbs(2000)
print("Balance_eas:", account_eas.get_balance_eas())