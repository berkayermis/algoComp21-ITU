from itertools import combinations
test_str = input()
test_str = test_str.replace(" ","")

print(test_str)

def main(test_str):
    currentLong = ""
    for x, y in combinations(range(len(test_str) + 1), r = 2):
        a = test_str[x:y]
        if a == a[::-1] and len(a) > len(currentLong):
            currentLong = a

    return len(currentLong)

print(main(test_str))