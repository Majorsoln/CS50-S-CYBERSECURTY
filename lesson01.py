## 4-digit PIN - There are 10 possibilities for each position WHICH IS 10⁴ = 10,000

from itertools import product
from string import digits

for pin in product(digits, repeat=4):
    pin = ''.join(pin)
    print(pin)

## This demonstrates the search space of a 4-digit PIN
