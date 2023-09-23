def solution(todo_list, finished):
    answer = [todo_list[i] for i in range(len(finished)) if not finished[i] ]
    return answer