# O(log(n)) | O(1)
def searchForRange(array, target):
    left = getLeftIdx(array, target)
    right = getRighttIdx(array, target)

    return [left, right]

def getLeftIdx(array, target):

    left, right = 0, len(array)-1
    middle = (left+right)//2

    while left <= right:
        middle_n = array[middle]

        if middle_n < target:
            left = middle + 1
        elif middle_n > target:
            right = middle - 1
        else:
            if middle == 0:
                return middle
            if array[middle-1] == middle_n:
                right = middle - 1
            else:
                return middle

        middle = (left+right)//2

    return -1

def getRighttIdx(array, target):

    left, right = 0, len(array)-1
    middle = (left+right)//2

    while left <= right:
        middle_n = array[middle]

        if middle_n < target:
            left = middle + 1
        elif middle_n > target:
            right = middle - 1
        else:
            if middle == len(array)-1:
                return middle
            if array[middle+1] == middle_n:
                left = middle + 1
            else:
                return middle

        middle = (left+right)//2

    return -1

if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 8, 9, 10]
    target = 0
    ans = searchForRange(array, target)
    print(ans)