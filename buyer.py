class Buyer:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f'Buyer: {self.name} {self.surname}, phone number- {self.phone}'


buyer_1 = Buyer('ivan', 'Ivanov', 12345)
buyer_2 = Buyer('Petr', 'Petrov', 54321)