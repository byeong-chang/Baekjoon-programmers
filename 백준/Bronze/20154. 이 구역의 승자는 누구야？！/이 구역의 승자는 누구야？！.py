import sys

N = sys.stdin.readline().rstrip()

letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
values = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
dictionary = dict(zip(letters, values))
lst = []
for t in N:
    lst.append(dictionary[t])

if sum(lst) % 2 == 1: print("I'm a winner!")
else: print("You're the winner?")