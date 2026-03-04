# В задаче на платформк сказано использовать указатели, а не стеки деки очереди. Я написал не как на семе, а как через указатели

str_1 = input()
str_2 = input()

i = 0
j = 0

while (i < len(str_1)) and (j < len(str_2)):
    if str_1[i] == str_2[j]:
        i += 1
        j += 1
        continue
    if str_1[i] != str_2[j]:
        j += 1

if (j == len(str_2)) and (i < len(str_1)):
    print("false")
else:
    print("true")