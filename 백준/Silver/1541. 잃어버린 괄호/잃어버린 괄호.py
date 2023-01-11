import sys
text = sys.stdin.readline()
length = 0
text_list = []
# str입력받아서 구분하는 parsing 부분
for i in range(len(text)):
    length +=1
    if text[i] == "+":
        text_list.append(int(text[i-length+1:i]))
        text_list.append("+")
        length = 0
    elif text[i] == "-":
        text_list.append(int(text[i-length+1:i]))
        text_list.append("-")
        length = 0
text_list.append(int(text[i-length+1:i]))

#list에 저장한 것을 뒤에서 부터 읽어들여 -만날때까지 일단 더한다.
# - 만나면 더한 값을 마이너스 처리한다.
add_until_minus = 0
temp = 0
total = 0
for i in reversed(text_list):
    if i == "+":
        add_until_minus += temp
    elif i == "-":
        add_until_minus += temp
        total -= add_until_minus
        add_until_minus = 0
    else:
        temp = i
total += add_until_minus +temp
print(total)