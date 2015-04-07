"""When manually iterating over an object, is it possible to view the current
value of your index? """
wallet = [100, 98, 87, 25, 4, 0]
iterWallet = iter(wallet)
next(iterWallet)
# 100
iterWallet.next()
# 98
next(iterWallet)
# 87


"""How is "return" different from "yield"?"""
def wallet1(spent):
    money = 100
    money -= spent
    return money
# 60

def wallet2(spent):
    money = 100
    money -= spent
    yield money
# <generator object wallet2 at 0x10e335fa0>
# Generators will not actually store the data, rather move through it to
# find the final desired value.


"""What modules are available to help with iterations?"""
from itertools import *  # I know you're not supposed to import univerally.

for item in count(3):
    print wallet
    # This is a bad idea... infinite iteration of wallet.

wallet3 = [12, 24, 48]
bills = ("Jackson", "Benjamin", "Washington")

for item in chain(wallet3, bills):
    print item
# 12
# 24
# 48
# Jackson
# Benjamin
# Washington
