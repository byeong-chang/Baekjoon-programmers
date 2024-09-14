import sys

def input():
    return sys.stdin.readline().rstrip()
vowel = ["a","e","i","o","u"]

while True:
    text = input()
    if text =="end":
        break

    # 모음이 하나도 없음
    flag = True
    for v in vowel:
        if v in text:
            flag = False
    if flag:
        print(f"<{text}> is not acceptable.")
    else:
        temp = ""
        for i in range(len(text)-2):
            if text[i] in vowel and text[i + 1] in vowel and text[i+2] in vowel:
                print(f"<{text}> is not acceptable.")
                break
            elif text[i] not in vowel and text[i + 1] not in vowel and text[i+2] not in vowel:
                print(f"<{text}> is not acceptable.")
                break
        else:
            for i in range(len(text)-1):
                if text[i] == text[i+1] and text[i] not in ["o", "e"]:
                    print(f"<{text}> is not acceptable.")
                    break
            else:
                print(f"<{text}> is acceptable.")


            
        

