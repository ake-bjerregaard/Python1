
n = int(input())

for x in range(0,n):
    print(x*x)


print(*[num**2 for num in range(n)], sep='\n')

