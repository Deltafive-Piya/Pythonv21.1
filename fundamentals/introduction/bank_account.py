# creating a class.
# implement default arguments in parameters for attributes that can be assigned on instantiation.
# use basic programmatic logic to implement the functionality of a bank account
# handle edge-cases, such as insufficient funds, with the appropriate control structure (if-else, code flow, or early exit)
# demonstrate proficiency in creating and update attributes of an object instance, from within the class using self .
# thoroughly test the functionality of their class by creating instances and calling methods with different test data and scenarios.

#Instance of the Bank account Class should contain a numeric balance value.
    # if deposit was made, the bank account should reflect the deposit, else have value "0" in account.
    # The account should also have an interest rate which adds value to the account; 1% interest rate should be notated as 0.01
#The Bank Account Class should have the following methods:
    #deposit (self,amount)- increase the balance by a given value
    #withdrawl(self,amount)- decreases the balance by a given value
    #display_account_info(self)-If the balance has 100, print "Checking Balance: $100" within the console




class BankAccount:
    accounts = []                                       # NINJA CHALLENGE- I needed to make the accounts list, so that i can pull all accounts in a batch

    def __init__(self, balance=0, interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.accounts.append(self)               #NINJA CHALLENGE- Adds self to accounts[]

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"Deposited: ${deposit_amount}")

    def withdrawal(self, withdrawl_amount):
        #NO SCAMS AT MY BANK and you aint even that hot, Shot.
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
        # Courtesy display of insterest accumulated. 
        print(f"Interest added: ${interest}") 


# USER ENGAGEMENT TEST----------------------------------------------------------------------------------------------------------------------
print('test_checking_account log')
test_checking_account = BankAccount(50)  # (Calling it "test_checking_account")Fork the Bankaccount Class, use default values if the () is empty
test_checking_account.display_account_info() #Display the default value
test_checking_account.withdrawal(100) # Withdrawl ATTEMPT -should fail
test_checking_account.deposit(200)    # Deposit 200
test_checking_account.withdrawal(100) # Withdrawl ATTEMPT -should pass
test_checking_account.deposit(20000)    # Deposit 200
test_checking_account.display_account_info() #Display the default value
test_checking_account.withdrawal(10000) # Withdrawl ATTEMPT -should fail
test_checking_account.withdrawal(5000) # Withdrawl ATTEMPT -should pass

test_checking_account.yield_interest() # An interest cycle simulation
test_checking_account.display_account_info() #Display the default value
print('\n')


# Checking 1 creation
print('Checking 1 log')
checking1 = BankAccount()
# CHAINING- 3 deposits & 1 withdrawl & yield & display
checking1.deposit(10); checking1.deposit(100); checking1.deposit(1000); checking1.withdrawal(1); checking1.yield_interest(); checking1.display_account_info()
print('\n')

#Checking 2 creation
print('Checking 2 log')
checking2 = BankAccount()
checking2.deposit(2); checking2.deposit(20); checking2.withdrawal(2); checking2.withdrawal(3); checking2.withdrawal(4); checking2.withdrawal(5);checking2.yield_interest(); checking2.display_account_info()
print('\n')

#SUDO- Use CLASS_METHOD to print ALL BankAccount() instances
print('ALL ACCOUNT LOG')
def print_all_accounts():
        for account in BankAccount.accounts:
            account.display_account_info()
print_all_accounts()                        #WELLLL.DO IT THEN.
