def sort(arr,s,mid,e):
    temp = []
    l=s
    r=mid+1
    
    while(l<=mid and r<=e):
        if arr[l] < arr[r]:
            temp.append(arr[l])
            l+=1
        else:
            temp.append(arr[r])
            r+=1
        
    
    while(l<=mid):
        temp.append(arr[l])
        l+=1
    
    while(r<=e):
        temp.append(arr[r])
        r+=1
    
    for i in range(s,e+1):
        arr[i]=temp[i-s]
        
def merge(arr,s,e):
    if s>=e:
        return
    mid = s+(e-s)//2
    merge(arr,s,mid)
    merge(arr,mid+1,e)
    
    sort(arr,s,mid,e)
    
def main():
    arr = [3,2,8,5,1,4,23]
    merge(arr,0,len(arr)-1)
    print(arr)

if __name__ == "__main__":
    main()
