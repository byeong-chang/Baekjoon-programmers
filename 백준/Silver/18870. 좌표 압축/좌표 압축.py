import sys

n = int(sys.stdin.readline())
input_save = list(map(int,sys.stdin.readline().split()))
sorted_values = sorted(list(set(input_save)))
value_index = {sorted_values[i] : i for i in range(len(sorted_values))}
for i in input_save:
    print(value_index[i],end=" ")