""" collection on all models used in DS.py include
User => a parent class for Employee,Customer
Manager => this class is same as Employee class and
its parent class in Employee
Employee => parent class for Manager
"""
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

    def add_account(self, account_number: int):
        '''get account_number and return nothing'''
        self.accounts.append(account_number)
        self.history['add_account'][datetime.now(  # add to history
        )] = f'add account with number => {account_number}'


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

    def show_balance(self):
        ''' return integer (balance)'''
        self.history['show_balance'][
            datetime.now()] = f'balance => {self.balance}'  # add to history
        return self.balance

    def withdraw(self, amount: int, types='withdraw_mode',
                 account_number_o=None):
        '''
        withdraw (amount=integer,types= choose withdraw_mode for withdraw money
        else choose fund_transfer_mode,
        account_number_o=another account_number for fund_transfer_mode )
        '''
        if amount > self.balance:
            return 1  # There is not enough money in your account
        elif amount <= 0:
            return 7  # number is smalller or equal to 0
        self.balance -= amount
        time = datetime.now()
        if types == 'withdraw_mode':
            # add to history
            self.history['withdraw'][time] = f'withdraw => {amount} '
        elif types == 'fund_transfer_mode':
            self.history['fund_transfer'][  # add to history
                time] = f'send => {amount} to => {account_number_o}'

    def deposit(self, amount: int, types='deposit_mode',
                account_number_o=None):
        '''
        deposit(amount=integer,types=choose deposit_mode for deposit
        else choose fund_transfer_mode,
        account_number_o=another account_number for fund_transfer_mode)
        '''
        self.balance += amount
        if amount <= 0:
            return 7  # number is smaller or equal to 0
        time = datetime.now()
        if types == 'deposit_mode':
            # add to history
            self.history['deposit'][time] = f'deposit => {amount} '
        elif types == 'fund_transfer_mode':
            self.history['fund_transfer'][
                time] = f'get => {amount} from => {account_number_o}'

    def fund_transfer(self, amount: int, account_number_o, types):
        '''
        fund_transfer(amount=integer,
        account_number_o=sender or receiver account number ,
        types=choose withdraw if you send money else choose deposit))
        '''
        if types == 'withdraw':
            self.withdraw(**locals())
        elif types == 'deposit':
            self.deposit(**locals())


@dataclass
class Branch:
    '''
    Branch(address=string,name=string)
    '''
    address: str
    name: str
    manager: str = ''
    employees: list[int] = field(default_factory=list)
