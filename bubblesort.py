def bubblesort(arr):
    a = len(arr)
    for iter in range(a):
        for i in range(a-1-iter):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                print(arr)
        print('iteration done')
    return arr
c = [1,5,2,3,0]
print('Final answer:',bubblesort(c))

#repeatedly comparing pairs of adjacent elements and swapping them
#as a result, sorting goeas from right to left
