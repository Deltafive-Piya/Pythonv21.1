class BankAccount:
    accounts = []
    def __init__(self, balance=0, interest_rate=0.001, withdrawl_limit=5000):
        self.balance = balance
        self.interest_rate = interest_rate
        self.withdrawl_limit = withdrawl_limit
        BankAccount.accounts.append(self)

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"Deposited: ${deposit_amount}")

    def withdrawl(self, withdrawl_amount, withdrawl_limit):
        if self.balance >= withdrawl_amount and withdrawl_amount <= withdrawl_limit: 
            self.balance -= withdrawl_amount
            print(f"Withdrew: ${withdrawl_amount}")
        else:
            print(f"Thats more than ${withdrawl_limit}! Withdrawl failure.")

    def display_account_info(self):
        print(f"Checking Balance: ${self.balance}")

    def yield_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest 
        print(f"Thank you for banking with Barbie! Interest added: ${interest}") 

# Add the User Class with __Init__----------------------------------------------------------------------------------------------------------------------
class User:
    def __init__(self, name, email, withdrawl_limit=5000):
        self.name = name
        self.email = email
        self.account = BankAccount()
        self.withdrawl_limit = withdrawl_limit

    def display_user_info(self):                #Displays User Balance----------------------------------------------------------------------------------
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        self.account.display_account_info()

    def make_deposit(self, deposit_amount):     #Make a deposit VIA USER--------------------------------------------------------------------------------
        self.account.deposit(deposit_amount)
    
    def make_withdrawl(self, withdrawl_amount):  #Make a withdrawl VIA USER-----------------------------------------------------------------------------
        if self.account.balance >= withdrawl_amount and withdrawl_amount < self.withdrawl_limit:
            self.account.withdrawl(withdrawl_amount, self.withdrawl_limit)
        else:
            print(f"${withdrawl_amount} exceeds Limit(${self.withdrawl_limit})! Withdrawl less.")


#TESTS--------------------------------------------------------------------------------------------------------------------------------------------------
user1 = User("Piya", "piya@email.com")
user1.display_user_info()
user1.make_deposit(10020)
user1.make_withdrawl(8000)                      #Should FAIL
user1.make_withdrawl(20)
user1.display_user_info()




# Sempai Bonus-Empty
# Sensei Bonus-Empty