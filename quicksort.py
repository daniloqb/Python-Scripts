import random
def quicksort(s,e):
    i=s
    j=e
    p=x[(s+e)/2]
    while i<j:
        while x[i]< p:
            i+=1
        while x[j]>p:
            j-=1
        if i<j:
            aux=x[i]
            x[i]=x[j]
            x[j]=aux
            print p, "->", x
        i+=1
        j-=1
    if j>s:
        quicksort(s,j)
    if i<e:
        quicksort(j+1,e)

x=range(10)
random.shuffle(x)
quicksort(0,9)


