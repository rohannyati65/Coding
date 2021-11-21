# Evaluate Expression (Coding Ninjas)
n = int(input())
x = 0
for i in range(n):
    a = int(input())
    a = str(a)
    y = int(a[:-1])
    z = int(a[-1])
    x = x + y ** z
print(x)
