# O(log(n)) | O(1)
def binarySearch(array, target):

    left, right = 0, len(array)-1
    middle = (left+right)//2

    while left <= right:
        middle_n = array[middle]
        if middle_n < target:
            left = middle + 1
        elif middle_n > target:
            right = middle - 1
        else:
            return middle

        middle = (left+right)//2

    return -1

if __name__ == "__main__":
    array = [1, 4, 6, 10, 15, 17, 21, 40]
    target = 40
    ans = binarySearch(array, target)
    print(ans)