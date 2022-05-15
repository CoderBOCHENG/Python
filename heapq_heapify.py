from random import randrange
from heapq import heapify
from binarytree import build


l = [randrange(100) for _ in range(10)]
print(l)

# make list l a valid min heap
heapify(l)

# step 2) create heap from l
heap = build(l)
print(heap)
print(l)
