from datetime import datetime
from uuid import uuid4
from prettytable import PrettyTable
import itertools
x = PrettyTable()


class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.slip_no = uuid4()
        self.product_bought = []
        self.prices = []
        self.trans_time = datetime.now()
        self.discount = 5/100
        self.product_list = {'apple': 120, 'bread': 700, 'soda': 150, 'beer': 300, 'banana': 580}

    def add_product(self, product, num=1):
        if product in self.product_list:
            if num > 1:
                while num > 0:
                    self.product_bought.append(product)
                    self.prices.append(self.product_list[product])
                    num -= 1

            else:
                self.product_bought.append(product)
                self.prices.append(self.product_list[product])

        else:
            self.product_bought.append(f'{product} is not available.')
            self.prices.append(0)
            # Done not to mess-up the indices

    def remove_product(self,product, num=1):
        if product in self.product_bought:
            # Validates that product to be removed exists
            if num > 1:
                for i in range(num):
                    self.prices.pop(self.product_bought.index(product))
                    self.product_bought.remove(product)
                    num -= 1
            elif num == 1:
                self.prices.pop(self.product_bought.index(product))
                self.product_bought.remove(product)
        else:
            print(f'{product} not in your cart.')

    def clear_cart(self):
        self.product_bought.clear()
        self.prices.clear()
        return

    def view_cart(self):
        print(f'You currently have {self.product_bought} in your cart.')

    def checkout(self):
        if self.product_bought:
            for i in self.product_bought:
                if i not in self.product_list:
                    # To remove unavailable items from checkout
                    self.prices.pop(self.product_bought.index(i))
                    self.product_bought.remove(i)
            if self.balance >= sum(self.prices):
                # Generate a receipt if you have enough money to purchase items
                x.field_names = ['Goods', 'Prices']
                x.max_table_width = 500
                for i,j in itertools.zip_longest(self.product_bought,self.prices):
                    x.add_row([i,j])
                x.add_row(['Total',sum(self.prices)])

                x.title = f'Slip ID : {str(uuid4())[0:6]}          {datetime.now()}'
                print(x)

            else:
                # If you don't have any items in your cart
                print(f'You do not have enough funds to purchase all the items.')
        else:
            print(f'{self.name}, you have\'nt purchased anything today. Thanks for coming.')




u = Customer('dubem',10000)
u.add_product('bread',5)
u.add_product('soda',5)
u.add_product('bread',5)
u.remove_product('bread',2)
u.remove_product('soda',5)
u.add_product('beer')
# u.add_product('beer')
u.remove_product('beer')
u.add_product('okpa')
u.view_cart()
# u.clear_cart()
u.checkout()
