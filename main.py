class OnlineShop:
    shop_name = "Tech Martket"

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    @classmethod
    def change_shop_name(cls, new_name):
        cls.shop_name = new_name

    @staticmethod
    def is_valid_price(price):
        if price > 0:
            return True


sh = OnlineShop("smel", 12000, 10)
print(sh.total_price())
