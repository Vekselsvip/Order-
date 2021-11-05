class Product:
    '''
    class different product
    '''

    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size

    def __str__(self):
        return f'name-{self.name}, price-{self.price}, size-{self.size}'


prod_1 = Product('phone', 100, 'S')
prod_2 = Product('tv', 250, 'M')