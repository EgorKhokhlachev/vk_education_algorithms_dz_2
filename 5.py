arr = list(map(int,input().split(" ")))

target = int(input())

i = 0
j = len(arr) - 1
f = 0

while i < j:
    if (arr[i] + arr[j]) < target:
        i += 1
        continue
    if(arr[i] + arr[j]) > target:
        j -= 1
        continue
    if (arr[i] + arr[j] == target):
        print(i,j)
        f = 1
        break
if (f == 0):
    print("false")