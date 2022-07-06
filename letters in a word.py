word = input().upper()
wordDict = {}
for i in word:
    if i in wordDict:
        wordDict[i] += 1
    else:
        wordDict.update({i:1})
for keys, values in wordDict.items():
    print(keys+":",values)