import heapq

#List of tasks:
tasks = [(2, 'clean the house'), (1, 'Do Leetcode'),(4, 'Pay Bills')]

heapq.heapify(tasks)

#Process the tasks based on priority:
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Processing task: {task} with priority: {priority}")