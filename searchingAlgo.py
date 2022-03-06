def linear_Search(List,target):
    '''Func performs Linear search ,
        List:Takes a list of elements
        target: Element to be searched
    '''
    for i in range(len(List)):
        if target == List[i]:
            return i
        
    return -1

def binary__Search(List,target,low,high):
    '''Func performs Binary search ,
        List:Takes a list of elements
        target: Element to be searched
    '''

    high = high -1
    while low <= high:

        mid = (low + high)//2

        if target == List[mid]:
            return mid
        elif target > List[mid]:
            low= mid + 1 #if target is bigger
        else:
            high = mid - 1
    
    return -1

