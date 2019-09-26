import time
from sympy import nextprime

n = 10000
while True:
    n = nextprime(n)
    print(n)
    time.sleep(1)
