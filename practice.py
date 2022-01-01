from random import *

total = 50
for i in range(1, 51):
    n = random.randrange(1, total)
    if(5 < n and n < 15):
        select = 'O'
    else:
        select = ' '
    print(f"[{select}]{i}번째 손님 (소요시간 : {n}분)")
