from product import *
from buyer import *
from order_iter import *


class Order:
    def __init__(self, buyer=None):
        if buyer is not None and not isinstance(buyer, Buyer):
            raise TypeError(f"'{type(buyer).__name__}' object cannot be interpreted as a buyer")

        self.buyer = buyer
        self.products = []

    def add_product(self, value):
        if not isinstance(value, Product):
            raise TypeError(f"'{type(value).__name__}' object cannot be interpreted as a product")
        self.products.append(value)

    def sum_order(self):
        res = 0
        for i in self.products:
            res += i.price
        return res

    def __str__(self):
        str_products = '\n'.join(map(str, self.products))
        prd = []
        for i in self.products:
            prd.append(i.name)
        prd = ', '.join(prd)
        return f'{self.buyer}\nOrder: {prd}\nSum order -{order_1.sum_order()}'

    def __getitem__(self, index):
        if index < len(self.products):
            return self.products[index]

    def __len__(self):
        return len(self.products)

    def __iter__(self):
        return OrderIterator(self.products)


order_1 = Order(buyer_2)
order_1.add_product(prod_1)
order_1.add_product(prod_1)
order_1.add_product(prod_2)
