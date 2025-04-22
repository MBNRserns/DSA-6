#Merge Sorting
array = [6,5,12,10,9,1]
print("Before Sorting: ")
print(array)

def MergeSort(array):
    if len(array) > 1:
        # to find the midpoint
        m=len(array)//2
        # : is in front of m to see everything from the start of the array to the midpoint
        L=array[:m]
        # : is behind of m to see everything from the midpoint till the end of the array
        R=array[m:]
        MergeSort(L)
        MergeSort(R)
        #i - left element of Left array
        #j - left element of Right array
        #k - merged array index
        i= j= k= 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i=i+1
            else:
                array[k] = R[j]
                j=j+1
            k=k+1
        while i<len(L):
            array[k] = L[i]
            i+=1
            k+=1
        while j<len(R):
            array[k] = R[j]
            j+=1
            k+=1
def displayResult(array):
    for i in range(len(array)):
        print(array[i], end=" ")


MergeSort(array)
print("After Sorting")
displayResult(array)

