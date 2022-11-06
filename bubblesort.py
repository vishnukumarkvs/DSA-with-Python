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

#Complexity
#correct one = n(n-1)/2 == n*n == (1st cycle: n-1 comparisions, 2nd cycle: n-2 comparisions ...  last cycle: 1 comparision)
#Best case: O(n) [if array is already sorted]


def bubblesort(arr):
    a = len(arr)
    for iter in range(a):
        bol=0
        for i in range(a-1-iter):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                bol=bol+1
                print(arr)
        if(bol == 0):
            return arr
        print('iteration done')
    return arr
c = [1,5,2,3,0]
d = [1,2,3,4,5]
print('Final answer:',bubblesort(c))
print('Final answer:',bubblesort(d))
