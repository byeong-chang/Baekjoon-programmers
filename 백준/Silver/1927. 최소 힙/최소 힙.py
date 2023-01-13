import sys
N = int(sys.stdin.readline())
heap_lst = [0]
def del_heap():
    min_val = heap_lst[1]
    temp = heap_lst.pop()
    if len(heap_lst) == 1: 
        return min_val
    heap_lst[1] = temp
    parent = 1
    child = 2
    while child < len(heap_lst):
        if child < len(heap_lst)-1 and heap_lst[child] > heap_lst[child+1] : #
            child += 1
        if temp <= heap_lst[child]:
            break
        heap_lst[parent] = heap_lst[child]
        parent = child
        child *=2
    heap_lst[parent] = temp
    return min_val

def insert_heap(n):
    heap_lst.append(n)
    count = len(heap_lst)-1
    while count >1:
        count_temp = count//2
        if heap_lst[count_temp] > heap_lst[count]:
            temp = heap_lst[count_temp]
            heap_lst[count_temp] = heap_lst[count]
            heap_lst[count] = temp
            count = count_temp
        else: break

for i in range(N):
    value = int(sys.stdin.readline())
    if value == 0:
        if len(heap_lst) <=1:
            print(0)
        else:
            print(del_heap())
    else:
        insert_heap(value)