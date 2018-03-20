#uses python3


import sys

#input= sys.stdin.read()
n,m = 10,10 #[int(x) for x in input.split()]
a=[0,1]

for x in range(2,20):

    a.append((a[x-1]+a[x-2])%m)
    if a[x-1] == 0 and a[x]==1:
        break
period=len(a)-2
print(period)
print(a)
b=[0,1]
for y in range(2,period+1):
    b.append(b[y-1]+b[y-2])

print (b[n%period]%m)