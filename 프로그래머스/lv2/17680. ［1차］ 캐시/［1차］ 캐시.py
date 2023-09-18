def solution(cacheSize, cities):
    answer = 0
    cache = [0 for _ in range(cacheSize)]
    cities = [city.lower() for city in cities]
    if cacheSize <= 0:
        return len(cities)*5
    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer+=1
        else:
            cache.pop(0)
            cache.append(city)
            answer+=5
        
    return answer