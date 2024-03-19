# -*- coding: utf-8 -*-
# 修正前のコード
"""
price1 = 100
price2 = 200

def total():
    tax = 1.1
    return price1 + price2

print (total() * tax)
"""

# 修正後のコード
price1 = 100
price2 = 200

def total():
    tax = 1.1
    return (price1 + price2) * tax

print (total())
