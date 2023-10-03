"""
    Min Heap = starts from smaller parent node to bigger children nodes
    Max Heap = starts from bigger parent node to smaller children nodes

    The child node on the left of its parent takes this equation:
    2i + 1, so it means that if index (i) of it parent is == 0, so 2 x 0 + 1 = index[1]
    so the next array's number to be placed should go at the index 1

    The child node on the right of its parent takes this equation:
    2i + 2, so it means that if index (i) of it parent is == 1, so 2 x 0 + 2 = index[2]
    so the next array's number to be placed should go at the index 2

    Remember that each of the children will become the parents of their directly linked
    nodes and the refence node's index must be from this new parent node

    example:

    if you have a node at the index[0] with a parent number 3, then the left child with
    the number 10 at index[1] and the right child with the number 4 at the index[3], the
    number 10 at the index[1] will become the parent for its 2 nodes (left and right) children 
    
"""

import heapq


heap = [1,2,65,78,98,3,6,7,99]

heapq.heapify(heap)  # Do NOT accept being added up to a variable to be printed out
print(heap)

x = heapq.nsmallest(3, heap)
print(x)

x = heap[0] # To know the smallest number/heap is used just heap[0]
print(x)

y = heapq.nlargest(3, heap)
print(y)

y = heapq.nlargest(1, heap) # To know the largest number/heap is used just 1
print(y)

heapq.heappush(heap, -9)
print(heap)

heapq.heappop(heap) # Removes node at index[0]
print(heap)

heapq.heappushpop(heap, 12) # Removes node at index[0] and add up 12 in right sequence
print(heap)

print(heap[0])

# Outputs:

# [1, 2, 3, 7, 98, 65, 6, 78, 99]
# [1, 2, 3]
# 1
# [99, 98, 78]
# [99]
# [-9, 1, 3, 7, 2, 65, 6, 78, 99, 98]
# [1, 2, 3, 7, 98, 65, 6, 78, 99]
# [2, 7, 3, 12, 98, 65, 6, 78, 99]
# 2

