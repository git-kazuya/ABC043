simple = list(input())

s: str = ""

for i in simple:
    if i == "B":
        s = s[:-1]
    else:
        s += i

print(s)
