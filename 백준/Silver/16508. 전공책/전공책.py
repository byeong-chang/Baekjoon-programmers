from collections import Counter

def can_make_word(available, target):
    # available은 책 제목들에서 나온 글자들의 카운트, target은 만들고자 하는 단어의 글자들
    for char, count in target.items():
        if available.get(char, 0) < count:
            return False
    return True

def solve(target_word, books):
    # target_word: 원하는 단어, books: (가격, 제목) 형태의 전공책들
    target_count = Counter(target_word)
    n = len(books)
    
    min_cost = float('inf')
    
    # 비트마스크를 사용하여 책들을 고르는 모든 경우의 수 탐색
    for mask in range(1, 1 << n):
        total_cost = 0
        available_chars = Counter()
        
        for i in range(n):
            if (mask >> i) & 1:  # i번째 책을 선택
                price, title = books[i]
                total_cost += price
                available_chars.update(title)  # 선택한 책의 글자들을 추가
        
        # 선택된 책들로 원하는 단어를 만들 수 있는지 확인
        if can_make_word(available_chars, target_count):
            min_cost = min(min_cost, total_cost)
    
    return min_cost if min_cost != float('inf') else -1

# 입력 받기
target_word = input().strip()  # 만들고 싶은 단어
n = int(input())  # 책의 개수

books = []
for _ in range(n):
    price, title = input().split()
    price = int(price)
    books.append((price, title))

# 결과 출력
print(solve(target_word, books))
