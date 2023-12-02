def sum_distance(first, second):
    result = 0
    if first < second:
        while first <= second:
            result += first
            first += 1
        return result
    if second < first:
        while second <= first:
            result += second
            second += 1
    return result


x = sum_distance(11, 11)
print(x)
