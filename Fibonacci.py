#uses python3
import sys

n=int(input())
fb =[0,1]
for x in range(2,n+1):
    fb.append((fb[x-1]+fb[x-2])%10)
print(fb[n])
