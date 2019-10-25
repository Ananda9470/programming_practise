# O(nlog(n)) | O(1)
def subarraySort(arr):

    arr_sorted = sorted(arr)
    first_time = True
    for i in range(len(arr)):

        n1 = arr[i]
        n2 = arr_sorted[i]

        if n1 != n2:

            if first_time:
                i1 = i
                first_time = False
            else:
                i2 = i

    if first_time:
        return [-1, -1]
    else:
        [i1, i2]
    return [i1, i2]

if __name__ == '__main__':
    arr = [2, 4, 6, 8, 10, 9, 11, 15, 17, 13, 20, 21]
    ans = subarraySort(arr)
    print(ans)