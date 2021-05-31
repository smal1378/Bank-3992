""" collection on all models used in DS.py include
User => a parent class for Employee,Customer
Manager => this class is same as Employee class and
its parent class in Employee
Employee => parent class for Manager
"""
from time import sleep
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class User:
    '''
    parent class for Manager, Employee and Customer
    '''
    first_name: str
    last_name: str
    username: str
    password: str
    ID: str
    address: str


@dataclass(repr=False)
class Employee(User):
    '''
    Employee(first_name:string ,last_name:string,username:string,
    password:string,ID:string,address:string,salary:integer,branch='')
    '''
    salary: int
    branch: str = ''


class Manager(Employee):
    '''
    Manager(first_name=string ,last_name:string,username=string,
    password=string,ID=string,address=string,salary=integer,branch='')
    '''


@dataclass
class Customer(User):
    '''
    Customer(first_name=string ,last_name=string,username=string,
    password=string,ID=string,address=string)
    '''
    accounts: list[int] = field(default_factory=list)
    __history = {'add_account': {}}

    def __add_to_history(self, types, **kwargs):
        """
        __add_to_history(types=(add_account),**kwargs)
        add_account => (types=add_account,account_num=integer)
        """
        history_types = {
            'add_account':
            f'add account with number =>{kwargs.get("account_num")}'}
        sleep(0.00001)
        text = history_types.get(types)
        time = datetime.now()
        if text:
            self.__history[types][time] = text

    def add_account(self, account_num: int):
        self.accounts.append(account_num)
        self.__add_to_history('add_account', account_num=account_num)

    def get_history(self, types=None):
        """yield all history if types is None else yield specific history"""
        history = self.__history.get(types)
        if history:
            for i in history.items():
                yield i
        else:
            for i in self. __history.values():
                for j in i.items():
                    yield j


@ dataclass
class Account:
    '''
    Account(balance=integer,owner=string,account_number=integer)
    '''
    balance: int
    owner: str
    account_number: int
    __history = {'withdraw': {}, 'deposit': {},
                 'fund_transfer': {}, 'balance': {}}

    def __add_to_history(self, types: str, **kwargs):
        """
        __add_to_history(types=(withdraw,deposit,fund_transfer_withdraw,fund_transfer_deposit,balance))
        withdraw => (withdraw,amount=integer)
        deposit => (deposit,amount=integer)
        transfer_deposit => (fund_transfer_deposit,amount=integer,
        account_num=account number of sender or receiver)
        transfer_withdraw => (fund_transfer_withdraw,amount=integer,
        account_num= account number of sender or receiver)
        balance => (balance)
        """
        history_types = {'withdraw': f'withdraw => {kwargs.get("amount")} ',
                         'deposit': f'deposit => {kwargs.get("amount")} ',
                         'transfer_withdraw':
                         f'send = > {kwargs.get("amount")} to \
                          => {kwargs.get("account_num")}',
                         'transfer_deposit':
                         f'get => {kwargs.get("amount")} from \
                          => {kwargs.get("account_num")}',
                         'balance': f'balance => {self.balance}'}
        sleep(0.00001)
        time = datetime.now()
        text = history_types.get(types)
        if text:
            self.__history[types][time] = text

    def show_balance(self) -> int:
        self.__add_to_history('balance')
        return self.balance

    def withdraw(self, amount: int, history=True):
        '''
        withdraw(amount=integer,history=if True add to history)
        return 1 if amount bigger than balance
        return 7 if amount is bigger or equal to 0
        '''
        if amount > self.balance:
            return 1  # There is not enough money in your account
        elif amount <= 0:
            return 7  # number is smalller or equal to 0
        self.balance -= amount
        if history:
            self.__add_to_history('withdraw', amount=amount)

    def deposit(self, amount: int, history=True):
        '''
        deposit(amount=integer,history=if True add to history)
        return 7 if amount is smaller or equal to 0
        '''
        self.balance += amount
        if amount <= 0:
            return 7  # number is smaller or equal to 0
        if history:
            self.__add_to_history('deposit', amount=amount)

    def fund_transfer(self, amount: int, account_num: int, types):
        '''
        fund_transfer(amount=integer,
        account_num=sender or receiver account number ,
        types=choose transfer_withdraw if you send money
        else choose transfer_deposit))
        return 1 if amount bigger than balance
        return 7 if amount is bigger or equal to 0
        '''
        var = vars()
        var.pop('self')
        if types == 'transfer_withdraw':
            result = self.withdraw(amount=amount, history=False)
            if result:
                return result
            self.__add_to_history(**var)
        elif types == 'transfer_deposit':
            result = self.deposit(amount=amount, history=False)
            if result:
                return result
            self.__add_to_history(**var)

    def get_history(self, types=None):
        """return all history if types None else return specific history"""
        history = self.__history.get(types)
        if history:
            for i in history.items():
                yield i
        else:
            for i in self.__history.values():
                for j in i.items():
                    yield j


@ dataclass
class Branch:
    '''
    Branch(address=string,name=string)
    '''
    address: str
    name: str
    manager: str = ''
    employees: list[int] = field(default_factory=list)


@dataclass
class Admin:
    username: str
    password: str
