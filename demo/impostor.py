finalRes = []

for i in range(10):
    wordlist = {}
    userInp = input()

    for j in userInp.split():
        if j in wordlist:
            wordlist[j] += 1
        else:
            wordlist[j] = 1

    for value in wordlist.values():
        if value > 2 and (i + 1) not in finalRes:
            finalRes.append(i + 1)

for z in finalRes:
    print(z, end=" ")
