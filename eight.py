#default arguments = A default value for certain parameters
#                    default is used when that argument is omitted 
#                    make your functions more flexible reduces no of arguments
#                    1. poositional, 2. DEFAULT 3. keyword   4. arbitrary

#def net_price(list_price, discount=0, tax=0.5):
#    return list_price * (1 - discount) * (1 + tax)

#print((net_price(50000, 0, 0.5)))
#print(net_price(50000, 0.1))``

import time

def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(0, 10)