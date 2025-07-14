# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

from collections import OrderedDict

n = int(input())

items = OrderedDict()

for _ in range(n):
    *item_name, price = input().split()
    item_name = ' '.join(item_name)
    price = int(price)

    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price

for name, total_price in items.items():
    print(name, total_price)
