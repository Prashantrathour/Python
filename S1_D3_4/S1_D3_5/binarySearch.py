array= [1, 2, 3, 4, 5, 6]
target = 3


def binarysearch(array, target):
    low=0
    high=len(array)-1
    try:
        array.index(target)
        while low<=high:
            mid=int((low+high)/2)
            if array[mid]==target:
                print(mid)
                return
            if array[mid]<target:
                low=mid
            elif array[mid]>target:
                 high=mid
    except ValueError:
        print(-1)
        return 

binarysearch(array, target)
       
           