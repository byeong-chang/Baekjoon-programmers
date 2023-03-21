

def solution(s):
    answer = 0
    word_list=['zero','one','two','three','four','five','six','seven','eight','nine']
    num_list=[a for a in range(len(word_list))]
    for word, i in zip(word_list,num_list):
        s=s.replace(word,str(i))
    answer=int(s)  
    return answer