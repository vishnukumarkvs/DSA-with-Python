def insertionsort(arr):
    
    for i in range(1,len(arr)):
        key=arr[i]
        last=i-1
        while last>=0 and key<arr[last]:
            arr[last+1]=arr[last]
            last=last-1
        arr[last+1]=key
    return arr
    
ab = [8,9,2,4,1]
d=[1,2,7,9,2]
print(insertionsort(ab),insertionsort(d))
