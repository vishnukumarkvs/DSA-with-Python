def selectionsort(arr):
    a = len(arr)
    base_index=0
    for iter in range(a):
        minn=arr[iter]
        k=-1
        for i in range(iter,a-1):
            if(minn>arr[i+1]):
                minn=arr[i+1]
                k=i+1
            else:
                k=iter
        arr[k],arr[iter]=arr[iter],arr[k]
        print(arr,k)
    return arr  
        
        
        
c = [1,5,2,3,0]
print('Final answer:',selectionsort(c))


###########################################

def ss(arr):
    for i in range(len(arr)):
        min_x=i
        for itr in range(i+1,len(arr)):
            if arr[itr]<arr[min_x]:
                min_x=itr
        arr[i],arr[min_x]=arr[min_x],arr[i]
    return arr
        
        
d = [1,5,2,3,0]
print('Final answer:',ss(d))
