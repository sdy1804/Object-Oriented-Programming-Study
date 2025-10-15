from datetime import date

class BankAccount:
    def __init__(self, username, password, balance, interest_rate, generated_date):
        self.__username = username
        self.__password = password
        self._balance = balance
        self.interest_rate = interest_rate
        self.generated_date = generated_date
    
    def withdraw(self, money):
        self._balance -= money
        print(f"system: {money}만원이 인출되었습니다.")
    
    def deposit(self, money):
        self._balance += money
        print(f"system: {money}만원이 입금되었습니다.")
    
    def report(self):
        print(f"잔액: {self._balance}만원")

class SavingAccount(BankAccount):
    def __init__(self, username, password, balance, interest_rate, generated_date, monthly_input, expiration_date):
        super().__init__(username, password, balance, interest_rate, generated_date)
        self.monthly_input = monthly_input
        self.expiration_date = expiration_date

class TimeDepositAccount(BankAccount):
    def __init__(self, username, password, balance, interest_rate, generated_date, input_amount, expiration_date):
        super().__init__(username, password, balance, interest_rate, generated_date)
        self.input_amount = input_amount
        self.expiration_date = expiration_date
        self.able_to_withdraw = False
        self.today = str(date.today())
    
    def __check_expire_date(self): # private method
        if (self.today != self.expiration_date):
            print("system: 적금 만기일에 도달하지 못했습니다.")
            self.able_to_withdraw = False
        else:
            print("system: 적금 만기일에 도달했습니다.")
            self.able_to_withdraw = True
    
    def withdraw(self):
        self.__check_expire_date()
        if self.able_to_withdraw == True:
            print("system: 모든 적금액이 인출되었습니다.")
            self._balance = 0
        else:
            print("system: 적금 만기일에 도달하지 못해 인출할 수 없습니다.")
    
    def deposit(self):
        self.__check_expire_date()
        if self.able_to_withdraw == False:
            self._balance += self.input_amount
            print(f"system: {self.input_amount}만원이 저축되었습니다.")

class OverdraftAccount(BankAccount):
    def __init__(self, username, password, balance, interest_rate, generated_date, max_amount, interest_rate_excess):
        super().__init__(username, password, balance, interest_rate, generated_date)
        self.max_amount = max_amount
        self.multiply_for_excess = interest_rate_excess
        self.able_to_borrow = True
    
    def check_max_limit(self):
        if self._balance <= self.max_amount:
            print("system: 한도에 도달하였습니다.")
            self.able_to_borrow = False
    
    def withdraw(self, money):
        if self.able_to_borrow == True:
            self._balance -= money
            print(f"system: {money}만원이 인출되었습니다.")

mike = SavingAccount("Mike", 123, 1000, 0.1, "2025-09-05", 100, "2026-09-05")
mike.withdraw(500)
mike.report()
print(" ")

kate = TimeDepositAccount("Kate", 456, 0, 0.1, "2025-09-05", 100, "2026-09-05")
kate.withdraw()
kate.deposit()
kate.report()
print(" ")

tim = OverdraftAccount("Tim", 789, 0, 0.1, "2025-09-05", -1000, 0.1)
tim.check_max_limit()
tim.withdraw(1000)
tim.report()
tim.check_max_limit()
tim.report()
tim.deposit(2000)
tim.check_max_limit()
tim.report()