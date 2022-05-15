'''
heapq : heap + queue
heap: max value is the root
heapq is a priority queue
Normal queue: FIFO ---------------------------
enqueue  1
enqueue  1,2
enqueue  1,2,10
enqueue  1,2,10,3
enqueue  1,2,10,3,-6
dequeue 2,10,3,-6
dequeue 10,3,-6
dequeue 3,-6
Priority queue: --------------------------
enqueue  1
enqueue  1,2
enqueue  1,2,10
enqueue  1,2,3,10
enqueue  -6,1,2,3,10
dequeue 1,2,3,10        -6
dequeue 2,3,10          1
dequeue 3,10            2
priority queue is implemented using heap
'''

from random import randrange
from heapq import heappush
from binarytree import build


# step 1) create a empty list
l = []

for _ in range(10):

    n = randrange(100) # [0,100)
    print(f"heappush {n} to list l")
    heappush(l, n) # heappush will make sure, list l is always a valid heap
    
    heap = build(l)
    print(heap)
    print(l)
    print("-" * 100)
