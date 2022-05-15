from binarytree import heap

# create a random max-heap
heap1 = heap()
print("Max heap with height=3")
print(heap1)

heap2 = heap(height=2)
print("Max heap with height=2")
print(heap2)

heap3 = heap(height=2, is_max=False, is_perfect=True)
print("Min heap with height=2 and it is perfect")
print(heap3)
