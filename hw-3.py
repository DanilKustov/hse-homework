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


def trim_and_repeat(my_string, offset=0, repetitions=1):
    result = my_string[offset:]
    return result * repetitions


hw1 = sum_distance(1, 11)
print(hw1)

hw2 = trim_and_repeat("Super-puper-string")
print(hw2)

