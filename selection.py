from itertools import product
import time
import getpass

#psw = str(input('write you psw: '))
psw = getpass.getpass('write your psw: ')
t1 = time.time()
ln = len(psw)

symbols = "0123456789"

comb = product(symbols, repeat=ln)
result = [''.join(comb) for comb in comb]

mat = format(len(result), ',').replace(',', ' ')
for line in result:
    line=line.strip()
    if psw == line:
        t2= time.time()
        print(f'All possible combination {mat}')
        print(f'The {n} character password was selected in {round(t2-t1, 5)} seconds')
        break
print(f'Error, compare your psw "{psw}" and available symbols "{symbols}"')

"""
write you psw: 01234567
All possible combination 100 000 000
The 8 character password was selected in 8.56052 seconds
"""
