from user import User


class Customer(User):

    cash = 0

    def money_reception(self, amount): #money_reception: daryaft vajh     amout: mablagh
        self.cash -= amount

    def money_remitment(self, amount, card_number): #money_reminent: entefgal vajh     card_number: shomare card
        self.cash -= amount

    def show_cash(self): #show_cash: moshahede mojudi
        return self.cash

    def recent_transaction(self): #recent_transaction: tarakonesh haye akhir
        pass
