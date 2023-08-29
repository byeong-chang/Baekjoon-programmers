def solution(phone_book):
    N = len(phone_book)
    sorted_phone_book = sorted(phone_book)
    for i in range(N-1):
        temp_len = len(sorted_phone_book[i])
        if sorted_phone_book[i] in sorted_phone_book[i+1][0:temp_len]:
            return False
    return True
