arr = list(map(int,input().split(" ")))

i = 0
j = 1
Len = len(arr)

l = 1

while i < Len:
    if arr[i] == arr[j]:
        while arr[i] == arr[j]:
            j += 1
            l += 1
        
