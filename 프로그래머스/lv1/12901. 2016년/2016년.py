from datetime import datetime
def solution(a, b):
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    answer = ''
    my_date = datetime(2016,a,b)
    date_gap =  (my_date - datetime(2016,1,1)).days
    day = date_gap%7
    return days[day]