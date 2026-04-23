class BankAccount_eas:
    def __init__(self_eas, account_name_eas, balance_eas):
        self_eas.account_name_eas = account_name_eas
        self_eas.balance_eas = balance_eas
    
    def deposit_eas(self_eas, amount_eas):
        self_eas.balance_eas += amount_eas
        print("Deposit successful")
    
    def withdraw_eas(self_eas, amount_eas):
        if amount_eas <= self_eas.balance_eas:
            self_eas.balance_eas -= amount_eas
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    
    def display_balance_eas(self_eas):
        print("Balance:", self_eas.balance_eas)


account_eas = BankAccount_eas("Juan", 5000)
account_eas.deposit_eas(1000)
account_eas.withdraw_eas(2000)
account_eas.display_balance_eas()