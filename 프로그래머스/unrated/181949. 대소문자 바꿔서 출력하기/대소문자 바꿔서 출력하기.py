string = input()
temp = ''
for i in string:
    if i.islower():
        temp+= i.upper()
    else: temp += i.lower()
print(temp)
