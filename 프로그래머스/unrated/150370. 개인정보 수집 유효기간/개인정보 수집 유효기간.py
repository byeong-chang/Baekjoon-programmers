import datetime
from dateutil.relativedelta import relativedelta
def solution(today, terms, privacies):
    a = list(map(int,today.split('.')))
    today = datetime.datetime(a[0],a[1],a[2])
    
    dic = {term[0] : int(term[2:]) for term in terms}
    
    answer = []
    for i,val in enumerate(privacies):
        d,t = val[:-2] ,val[-1]
        d = list(map(int,d.split('.')))
        d = datetime.datetime(d[0],d[1],d[2])
        d = d + relativedelta(months=dic[t]) - datetime.timedelta(days=1)
        if today > d : answer.append(i+1)
    return answer