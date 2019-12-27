from helpers import *

# Part A
data = [int(x) for x in get_input(1)]

fuel = [m//3 -2 for m in data]
print(sum(fuel))

# Part B

def fuel_req(mass):
    fuel = (mass // 3) - 2
    if fuel > 0:
        return fuel + fuel_req(fuel)
    else:
        return 0

print(fuel_req(14))
print(fuel_req(1969))

fuel = [fuel_req(m) for m in data]
print(sum(fuel))
