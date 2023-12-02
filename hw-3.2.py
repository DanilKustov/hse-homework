def trim_and_repeat(my_string, offset=0, repetitions=1):
    result = my_string[offset:]
    return result * repetitions


x = trim_and_repeat("Super-puper-string")
print(x)
