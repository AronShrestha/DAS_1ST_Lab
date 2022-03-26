def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i =  j-1
        while i >= 0 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        
        A[i+1] = key
    
    return A



def Merge_sort(A,p,r):
    if p <r :
        q = (p+r)//2
        Merge_sort(A,p,q)
        Merge_sort(A,q+1,r)
        Merge(A,p,q,r)
    return A
def Merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L=[]
    R=[]
    for i in range(1,n1+1):
        L.append(A[p+i-1])
    for j in range(1,n2+1):
        R.append(A[q+j])
    i = 0
    j = 0
    k=p
    while i < n1 and j < n2:
        if L[i]<=R[j]:
            A[k]=L[i]
            i=i+1
        else:
            A[k] = R[j]
            j=j+1
        k+=1
    if i>=n1:
        while j < n2:
            A[k] = R[j]
            j+=1
            k+=1
    else:
        while i < n1:
            A[k]=L[i]
            i+=1
            k+=1
    return A
    
    
# print(Merge([8,9,2,6],0,1,3))