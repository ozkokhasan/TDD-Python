
class Checkout(object):
    class Discount(object):
        def __init__(self, numberofitems, price):
            self.numberofitems = numberofitems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        if item not in self.prices:
            raise Exception("Bad Item")
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculate_total(self):
        total = 0
        for item, count in self.items.items():
            total += self._calculate_item_total(item, count)
        return total

    def _calculate_item_total(self, item, count):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.numberofitems:
                total += self._calculate_discount_total(item, count, discount)
            else:
                total += self.prices[item] * count
        else:
            total += self.prices[item] * count
        return total

    def _calculate_discount_total(self, item, count, discount):
        total = 0
        numberofdiscounts = count / discount.numberofitems
        total += numberofdiscounts * discount.price
        remaining = count % discount.numberofitems
        total += remaining * self.prices[item]
        return total

    def add_discount(self, item, numberofitems, price):
        discount = self.Discount(numberofitems, price)
        self.discounts[item] = discount
