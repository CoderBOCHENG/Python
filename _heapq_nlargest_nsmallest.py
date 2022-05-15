from random import randrange
from heapq import nlargest, nsmallest


l = [randrange(100) for _ in range(10)]
print(l)

subList1 = nlargest(2, l)
print(subList1)

subList2 = nsmallest(2, l)
print(subList2)
