# max{O(nlog(n) + O(mlog(m)) | O(1)
def smallestDifference(arrayOne, arrayTwo):

    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)

    arr1_idx = 0
    arr2_idx = 0

    least_diff = float("inf")

    while arr1_idx<len(arrayOne) and arr2_idx<len(arrayTwo):

        N1 = arrayOne[arr1_idx]
        N2 = arrayTwo[arr2_idx]

        if N1 < N2:
            curr_diff = N2 - N1
            arr1_idx += 1
        elif N1 > N2:
            curr_diff = N1 - N2
            arr2_idx += 1
        else:
            return [N1, N2]

        if curr_diff < least_diff:
            least_diff = curr_diff
            smallest_diff_pair = [N1, N2]

    return smallest_diff_pair


if __name__ == '__main__':
    arr1 = [-1, 5, 10, 20, 28, 3]
    arr2 = [26, 134, 135, 15, 17]
    ans = smallestDifference(arr1, arr2)
    print(ans)
