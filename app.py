from order_books.buy_orders import BuyOrders
from order_books.sell_orders import SellOrders
from api import app, db
from api import models
buy_orders = BuyOrders([5, 3, 8, 23, 9])

sell_orders = SellOrders([1, 10, 50, 23, 43, 27, 2, 4, 8, 2, 4, 6, 3, 2, 3])

def match(sells, buys):
    while sells.get_top() != None and buys.get_top() != None and sells.get_top() <= buys.get_top():
        print(f"SOLD\nseller was at {sells.pop()}\nbuyer was at {buys.pop()}\n\n")

match(sell_orders, buy_orders)
