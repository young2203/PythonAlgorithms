from SortAlgorithm.Sorting import mergeSort
from SortAlgorithm.Sorting import insertSort

def mergeTest(scale_size):
    import numpy as np
    myList = list(np.random.randint(0,1000,scale_size))
    mergeSort(myList)
    
def insertTest(scale_size):  
    import numpy as np
    myList = list(np.random.randint(0,1000,scale_size))
    insertSort(myList)