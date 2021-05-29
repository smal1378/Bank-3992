""" collection on all models used in DS.py include
User => a parent class for Employee,Customer
Manager => this class is same as Employee class and
its parent class in Employee
Employee => parent class for Manager
"""
from dataclasses import dataclass, field
from datetime import datetime
from time import sleep


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


@dataclass
class Employee(User):
    '''
    Employee(first_name:string ,last_name:string,username:string,
    password:string,ID:string,address:string,salary:integer)
    '''
    salary: int


class Manager(Employee):
    '''
    Manager(first_name:string ,last_name:string,username:string,
    password:string,ID:string,address:string,salary:integer)
    '''


@dataclass
class Customer(User):
    '''
    Customer(first_name:string ,last_name:string,username:string,
    password:string,ID:string,address:string)
    '''
    accounts: list[int] = field(default_factory=list)
    history = {'add_account': {}}

    def add_to_history(self, types, **kwargs):
        """
        add_to_history(types=(add_account))
        add_account => (add_account,account_number=integer)
        """
        sleep(.00001)
        time = datetime.now()
        if types == 'add_account':
            self.history[types][time] = \
                f'add account with number => {kwargs["account_number"]}'

    def add_account(self, account_number: int):
        '''get account_number and return nothing'''
        self.accounts.append(account_number)
        self.add_to_history('add_account', account_number=account_number)


@dataclass
class Account:
    '''
    Account(balance=integer,owner=string,account_number=integer)
    '''
    balance: int
    owner: str
    account_number: int
    history = {'withdraw': {}, 'deposit': {},
               'fund_transfer': {}, 'show_balance': {}}

    def add_to_history(self, types, **kwargs):
        """
        add_to_history(types=(withdraw,deposit,fund_transfer_withdraw,fund_transfer_deposit,balance))
        withdraw => (withdraw,amount=integer)
        deposit => (deposit,amount=integer)
        transfer_deposit => (fund_transfer_deposit,amount=integer,
        account_num=account number of sender or receiver)
        transfer_withdraw => (fund_transfer_withdraw,amount=integer,
        account_num= account number of sender or receiver)
        balance => (balance)
        """
        sleep(.00001)
        time = datetime.now()
        if types == 'withdraw':
            self.history[types][time] = f'withdraw => {kwargs["amount"]} '
        elif types == 'deposit':
            self.history[types][time] = f'deposit => {kwargs["amount"]} '
        elif types == 'transfer_withdraw':
            self.history['fund_transfer'][time] = \
                f'send => {kwargs["amount"]} to => {kwargs["account_num"]}'
        elif types == 'transfer_deposit':
            self.history['fund_transfer'][time] = \
                f'get => {kwargs["amount"]} from => {kwargs["account_num"]}'
        elif types == 'balance':
            self.history['show_balance'][time] = f'balance => {self.balance}'

    def show_balance(self):
        ''' return integer (balance)'''
        self.add_to_history('balance')
        return self.balance

    def withdraw(self, amount: int, history=True):
        '''
        withdraw (amount=integer)
        '''
        if amount > self.balance:
            return 1  # There is not enough money in your account
        elif amount <= 0:
            return 7  # number is smalller or equal to 0
        self.balance -= amount
        if history == True:
            self.add_to_history('withdraw', amount=amount)

    def deposit(self, amount: int, history=True):
        '''
        deposit(amount=integer)
        '''
        self.balance += amount
        if amount <= 0:
            return 7  # number is smaller or equal to 0
        if history == True:
            self.add_to_history('deposit', amount=amount)

    def fund_transfer(self, amount: int, account_num: int, types):
        '''
        fund_transfer(amount=integer,
        account_num=sender or receiver account number ,
        types=choose transfer_withdraw if you send money else choose transfer_deposit))
        '''
        var = vars()
        var.pop('self')
        if types == 'transfer_withdraw':
            result = self.withdraw(amount=amount, history=False)
            if result:
                return result
            self.add_to_history(**var)
        elif types == 'transfer_deposit':
            result = self.deposit(amount=amount, history=False)
            if result:
                return result
            self.add_to_history(**var)


@ dataclass
class Branch:
    '''
    Branch(address=string,name=string)
    '''
    address: str
    name: str
    manager: str = ''
    employees: list[int] = field(default_factory=list)
