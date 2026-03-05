from collections import deque

s = input()

d = deque(s)

f = 1

while len(d) > 1:
    if d.pop() != d.popleft():
        f = 0

if f == 0:
    print("false")
else:
    print("true")