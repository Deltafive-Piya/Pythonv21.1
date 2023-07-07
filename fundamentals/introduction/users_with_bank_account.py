class BankAccount:
    accounts = []
    def __init__(self, balance=0, interest_rate=0.001):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.accounts.append(self)

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"Deposited: ${deposit_amount}")

    def withdrawal(self, withdrawl_amount):
        if self.balance >= withdrawl_amount and withdrawl_amount <5001: 
            self.balance -= withdrawl_amount
            print(f"Withdrew: ${withdrawl_amount}")
        else:
            print(f"${withdrawl_amount}? You aint that hot, Shot!")

    def display_account_info(self):
        print(f"Checking Balance: ${self.balance}")

    def yield_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest 
        print(f"Thank you for banking with Barbie! Interest added: ${interest}") 

# Add the User Class with __Init__----------------------------------------------------------------------------------------------------------------------
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    def display_user_info(self):                #Displays User Balance----------------------------------------------------------------------------------
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        self.account.display_account_info()

    def make_deposit(self, deposit_amount):     #Make a deposit VIA USER--------------------------------------------------------------------------------
        self.account.deposit(deposit_amount)
    
    def make_withdrawl(self, withdrawl_amount):  #Make a withdrawl VIA USER-----------------------------------------------------------------------------
        if self.account.balance >= withdrawl_amount and withdrawl_amount <5001:
            self.account.withdrawal(withdrawl_amount)

user1 = User("Piya", "piya@code.com")
user1.display_user_info()
user1.make_deposit(10020)
user1.make_withdrawl(8000)
user1.make_withdrawl(20)
user1.display_user_info()





# Sempai Bonus-Empty
# Sensei Bonus-Empty