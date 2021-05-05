def isWord(word):
    return len(word) > 0


lens = input()
string = input()
inputs = string.split(" ")
words = []
memory = []
result = 0
for item in inputs:
    word = item.strip(".-?!',").lower()
    if isWord(word):
        words.append(word)
if len(words) == 0:
    print(0)
    print(0)
else:
    for word in words:
        if word not in memory:
            if len(memory) >= int(lens):
                memory.pop(0)
            memory.append(word)
            result = result + 1
    # print(words)
    print(len(words))
    print(result)
