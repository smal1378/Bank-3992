from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    '''
    parent class for manager, employee and customer
    '''
    first_name: str
    last_name: str
    username: str
    password: str
    ID: str
    address: str


@dataclass
class Manager(User):
    '''
    Manager(first_name:string ,last_name:string,username:string,password:string,
    ID:string,address:string,salary:integer)
    it inherits from user class
    '''

    salary: int


@dataclass
class Employee(User):
    '''
    Employee(first_name:string ,last_name:string,username:string,password:string,
    ID:string,address:string,salary:integer)
    it inherits from user class
    '''
    salary: int


@dataclass
class Customer(User):
    '''
    Employee(first_name:string ,last_name:string,username:string,password:string,
    ID:string,address:string)
    it inherits from user class
    '''
    accounts: []
    history = {'show_balance': {}, 'add_acount': {},
               'withdraw': {}}

    def show_balance(self, account_number: int):
        if account_number in accounts:
            self.history['show_balance'][datetime.now(
            )] = f'get balance from account number {account_number}'
            return accounts  # return account number to use in core
        else:
            return 2  # there is no such account number

    def add_account(self, account_number: int):
        self.accounts.append(account_number)
        self.history['add_account'][datetime.now(
        )] = f'add account with number {account_number}'


@dataclass
class Account:
    '''
    Account(balance=integer,owner,account_number)
    '''
    balance: int
    owner: str
    history = {'withdraw': {}, 'deposit': {}, 'fund_transfer': {}}
    account_number: int

    def withdraw(self, amount: int):
        if amount > balance:
            return 1  # There is not enough money in your account
        else:
            self.balance -= amount
            self.history['deposit'][datetime.now()] = f'deposit {amount} '

    def deposit(self, amount: int):
        self.balance += amount
        self.history['withdraw'][datetime.now()] = f'withdraw {amount} '

    def fund_transfer(self, amount: int, account_number_o, types):
        '''
        fund_transfer(amount=integer,account_number_o=account number of other side,types=(withdraw,deposit))
        '''
        if types == 'withdraw':
            if amount > balance:
                return 1  # There is not enough money in your account
            else:
                self.balance -= amount
                self.history['fund_transfer'][datetime.now(
                )] = f'send {amount} to {account_number_o}'
        elif types == 'deposit':
            self.balance += amount
            self.history['fund_transfer'][datetime.now(
            )] = f'get {amount} from {account_number_o}'
