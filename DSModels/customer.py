from user import User


class Customer(User):


    def __init__(self, first_name, last_name, username, password, national_code, address, access_level, balance):
        super().__init__(self, first_name, last_name, username, password, national_code, address, access_level)
        self.balance = balance

    def money_reception(self, amount): #money_reception: daryaft vajh     amout: mablagh
        if(amount > self.balance):
            return "There is not enough balance in you account!"
        else:
            self.balance -= amount

    def money_remitment(self, amount, card_number): #money_reminent: entefgal vajh     card_number: shomare card
        self.balance -= amount

    def show_cash(self): #show_cash: moshahede mojudi
        return (self.balance)

    def recent_transaction(self): #recent_transaction: tarakonesh haye akhir
        pass

