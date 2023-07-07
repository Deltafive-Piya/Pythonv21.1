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
    def __init__(self, balance=0, interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"Deposited: ${deposit_amount}")

    def withdrawal(self, withdrawl_amount):
        if self.balance >= withdrawl_amount and withdrawl_amount <5000: #NO SCAMS AT MY BANK
            self.balance -= withdrawl_amount
            print(f"Withdrew: ${withdrawl_amount}")
        else:
            print("You broke, bye!")

    def display_account_info(self):
        print(f"Checking Balance: ${self.balance}")

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: ${self.interest}") # Courtesy display of insterest accumulated. 


checking1 = BankAccount()  # (Calling it "checking1")Fork the Bankaccount Class, use default values if the () is empty
checking1.display_account_info() #Display the default value
