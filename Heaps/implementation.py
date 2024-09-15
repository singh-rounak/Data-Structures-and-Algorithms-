import heapq

heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)
heapq.heappush(heap, 15)

print(heap)

smallest = heapq.heappop(heap)
print(smallest)