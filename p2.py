str, num = (input().split())
charDict = {}
charList = list(str)
for i in range(len(charList)):
    if charList[i] in charDict.keys():
        charList[i] = '_'
    elif i < int(num):
        charDict[charList[i]] = 0
ans = "".join(charList)
print(ans)


