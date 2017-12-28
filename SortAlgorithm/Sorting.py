def insertSort(myList):
    '''Sort list with ascending order using insert sort algorithm'''
    listLen = len(myList)
    for i in range(1,listLen):
        j = i
        tempVar = myList[i]    
        while j > 0 and myList[j-1] > tempVar: 
        #as long as a_j-1 > a_j (local descending order), exchange should happen
            myList[j] = myList[j-1]
            j-=1
        myList[j] = tempVar
    return myList

def mergeSort(myList):
    '''Sort list with ascending order using merging sort algorithm'''
    from math import floor as flr
    N =  len(myList)
    if N==1 :
        return myList
    else:
        # Divide into two parts
        subList_1 = myList[0:flr(N/2)]
        subList_2 = myList[flr(N/2):N]
        # Recursion to sort sublists
        mergeSort(subList_1)
        mergeSort(subList_2)
        # Merge two sublists
        pointer_1 = 0
        pointer_2 = 0
        max_max = max(subList_1[-1],subList_2[-1]) + 1.0
        for i in range(N):
            # set pointer for sublist 1
            if pointer_1 < len(subList_1):
                value_1 = subList_1[pointer_1]
            else:
                value_1 = max_max
            # set pointer for sublist 2
            if pointer_2 < len(subList_2):
                value_2 = subList_2[pointer_2]
            else:
                value_2 = max_max
            myList[i]=min(value_1,value_2)
            # Move pointer based on sorted sublists
            if value_1 < value_2:
                pointer_1+=1
            else:
                pointer_2+=1
        return myList
       