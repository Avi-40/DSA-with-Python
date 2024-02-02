def parti(arr,s,e):
    pivot = arr[s]
    i = s
    j = e
    while(i<j):
        while arr[i]<=pivot and i<=e-1:
            i+=1
        while arr[j]>pivot and j>=s+1:
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[s],arr[j] = arr[j],arr[s]
    return j

def qs(arr,s,e):
    if s<e:
        pivot=parti(arr,s,e)
        qs(arr,s,pivot-1)
        qs(arr,pivot+1,e)
    

def quickSort(arr):
    qs(arr,0,len(arr)-1)
    return arr
