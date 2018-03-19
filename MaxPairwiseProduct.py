# uses python3
def max_pairwise(n,a):
    #n = int(input())
    #a = [int(x) for x in input().split()]
    assert(len(a) == n)

    index1 = 0
    for i in range(1,n):
        if a[i]>a[index1]:
            index1=i

    if index1==0:
        index2 = 1
    else:
        index2=0

    for j in range(0,n):
        if index1!= j and a[j]>a[index2]:
            index2=j

    return(a[index1]*a[index2])

def max_pairwiseslow(n,a):
    #n=int(input("Please enter the length for array : " ))
    #a=[int(x) for x in input("Please keep entering the number : ").split()]
    assert(len(a)==n)
    product=0
    for i in range(0,n):

        for j in range(i+1,n):

            if a[i]*a[j]>product:
                product=a[i]*a[j]

    return product



print(max_pairwiseslow())