word = "test"
center = int(len(word)/2)
if len(word) % 2 == 0:
    print(word[center-1:center+1])
else:
    print(word[center])
