from datetime import date

class Bank:
    def __init__(self):
        self.__list_accounts = []    
    
    def register_bank_account(self, username, password, balance, interest_rate, generated_date, input_amount=None, duration=None, max_under=None):
        cur_account = None 
        self.__username = username
        self.__password = password
        self._balance = balance
        self.interest_rate = interest_rate
        self.generated_date = generated_date

        if duration is None and max_under is None:
            cur_account = SavingAccount(self.__username, self.__password, self._balance, self.interest_rate, self.generated_date)
            print("저축 계좌가 생성되었습니다.")
        elif duration is not None and max_under is None:
            cur_account = TimeDepositAccount(self.__username, self.__password, self._balance, self.interest_rate, self.generated_date, input_amount, duration)
            print("적금 계좌가 생성되었습니다.")
        elif duration is None and max_under is not None:
            cur_account = OverdraftAccount(self.__username, self.__password, self._balance, self.interest_rate, self.generated_date, max_under)
            print("마이너스 계좌가 생성되었습니다.")

        self.__list_accounts.append(cur_account)
        return cur_account

class BankAccount:
    def __init__(self):
        self._list_transaction_accounts = []
    
    def deposit(self, money):
        self._balance += money
        trans = Transaction().trans(money)
        self._list_transaction_accounts.append(trans)
        print(f"system: {money}만원이 입금되었습니다.")
    
    def withdraw(self, money):
        self._balance -= money
        trans = Transaction().trans(money)
        self._list_transaction_accounts.append(trans)
        print(f"system: {money}만원이 인출되었습니다.")
    
    def report(self):
        print(f"잔액: {self._balance}만원")

class Transaction:
    def trans(self, money):
            if money >= 0:
                print(f"거래가 완료되었습니다.") 
            else:
                print("거래 입출금에 오류가 발생했습니다.")

class SavingAccount(BankAccount):
    def __init__(self, username, password, balance, interest_rate, generated_date):
        super().__init__()
        self.__username = username
        self.__password = password
        self._balance = balance
        self.interest_rate = interest_rate
        self.generated_date = generated_date

class TimeDepositAccount(BankAccount):
    def __init__(self, username, password, balance, interest_rate, generated_date, input_amount, duration):
        super().__init__()
        self.__username = username
        self.__password = password
        self._balance = balance
        self.interest_rate = interest_rate
        self.generated_date = generated_date
        self.input_amount = input_amount
        self.duration = duration
        # self.able_to_withdraw = False
        self.today = str(date.today())
    
    def __check_expire_date(self): # private method
        if (self.today != self.duration):
            print("system: 적금 만기일에 도달하지 못했습니다.")
            # self.able_to_withdraw = False
        else:
            print("system: 적금 만기일에 도달했습니다.")
            # self.able_to_withdraw = True
        return self.today != self.duration
    
    def withdraw(self):
        if self.__check_expire_date():
        # if self.able_to_withdraw == True:
            print("system: 모든 적금액이 인출되었습니다.")
            self._balance = 0
        else:
            print("system: 적금 만기일에 도달하지 못해 인출할 수 없습니다.")
    
    def deposit(self):
        if self.__check_expire_date():
        # if self.able_to_withdraw == False:
            self._balance += self.input_amount
            print(f"system: {self.input_amount}만원이 저축되었습니다.")

class OverdraftAccount(BankAccount):
    def __init__(self, username, password, balance, interest_rate, generated_date, max_under):
        super().__init__()
        self.__username = username
        self.__password = password
        self._balance = balance
        self.interest_rate = interest_rate
        self.generated_date = generated_date
        self.max_under = max_under
        # self.able_to_borrow = True
    
    def __check_max_limit(self):
        if self._balance <= self.max_under:
            print("system: 한도에 도달하였습니다.")
            # self.able_to_borrow = False
        else:
            print(f"system: 출금 가능합니다.")
        return self._balance > self.max_under
    
    def withdraw(self, money):
        if self.__check_max_limit():
        # if self.able_to_borrow == True:
            self._balance -= money
            print(f"system: {money}만원이 인출되었습니다.")

mike = Bank().register_bank_account("Mike", 123, 500, 0.1, "2025-09-05")
mike.deposit(100)
mike.report()
mike.withdraw(300)
mike.report()
print(" ")

kate = Bank().register_bank_account("Kate", 456, 0, 0.1, "2025-09-10", 100, 24)
kate.withdraw()
kate.deposit()
kate.report()
print(" ")

tim = Bank().register_bank_account("Tim", 789, 1000, 0.1, "2025-09-01", None, None, -2000)
# tim.check_max_limit()
tim.withdraw(1000)
tim.report()
tim.withdraw(1000)
# tim.check_max_limit()
tim.report()
tim.deposit(2000)
# tim.check_max_limit()
tim.report()