import string

s = "1 2 3 | 3 6 9"
s_split = s.split('|')
first = s_split[0].split()
second = s_split[1].split()
result = ""

for i in range(len(first)):
    result += str(int(first[i]) * int(second[i]))
    if i != len(first):
        result += " "

print(result)
