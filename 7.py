arr = list(map(int,input().split(" ")))

i = 0
j = 1
Len = len(arr)

l = 1

while i < Len:
    if arr[i] == arr[j]:
        while (j < Len) and (arr[i] == arr[j]):
            j += 1
            l += 1
        for k in range(i + l,len(arr)):
            arr[k - l + 1] = arr[k]
        i += 1
        j = i + 1
        Len = Len - (l - 1)
        l = 1
    else:
        i += 1
        j += 1

for i in range(Len):
    print(arr[i], end=" ")      
        
