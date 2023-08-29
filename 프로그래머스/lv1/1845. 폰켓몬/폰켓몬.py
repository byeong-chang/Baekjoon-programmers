def solution(nums):
    # dict 자료형으로 받아서 key의 개수를 세면 될듯함.(최대값은 N/2로 제한)
    poketmon = dict()
    for num in nums:
        poketmon[num] = True
    
    answer = len(poketmon.keys())
    N = len(nums)//2
    
    if answer > N:
        return N
    else : return answer