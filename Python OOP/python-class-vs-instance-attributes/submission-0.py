class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_account: int = 0
    total_balance: int = 0
    
    def __init__(self, balance: int) -> None:
        self.__balance = balance
        BankAccount.total_account += 1
        BankAccount.total_balance += balance
    
    @property
    def balance(self) -> int:
        return self.__balance

# TODO: Create two accounts
# TODO: Print the information using the mentioned format
alice_bank_acc = BankAccount(1000)
bob_bank_acc = BankAccount(2000)
print(f"Alice's balance: ${alice_bank_acc.balance}")
print(f"Bob's balance: ${bob_bank_acc.balance}")
print(f"Total Accounts: {BankAccount.total_account}")
print(f"Total Balance: ${BankAccount.total_balance}")