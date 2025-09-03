class BankAccount:
    def __init__(self, username, password, balance, interest_rate, generated_date):
        self.__username = username
        self.__password = password
        self.balance = balance
        self.__interest_rate = interest_rate
        self.__generated_date = generated_date

    def deposit(self, money):
        self.balance += money
    
    def withdraw(self, money):
        self.balance -= money
    
    def report(self):
        print(f"{self.__username}의 잔액은 {self.balance}원입니다.")
    
mike = BankAccount("Mike", 123, 0, 0.1, 20250903)
kate = BankAccount("Kate", 456, 500, 0.1, 20240903)
tim = BankAccount("Tim", 789, 1000, 0.1, 20230903)

mike.deposit(500)
mike.withdraw(300)

kate.deposit(500)
kate.withdraw(300)

tim.deposit(500)
tim.withdraw(300)

for i in [mike, kate, tim]:
    i.report()