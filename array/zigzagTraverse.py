# O(n) \ O(n): n is number of element in the 2d matrix
def zigzagTraverse(arr):

    m = len(arr)
    n = len(arr[0])

    i, j = 0, 0
    flip = -1

    zz_arr = []

    while i<=m-1 and j<=n-1:

        zz_arr.append(arr[i][j])

        if flip == -1:  # i inc, j dec
            i += 1
            j -= 1
        else:  # i dec, j inc
            i -= 1
            j += 1

        if -1<i<m and -1<j<n:
            pass
        else:
            if i>=m:
                i = min(i, m-1)
                j += 2

            if j>=n:
                j = min(j, n-1)
                i += 2

            if i<0 or j<0:
                i = max(i, 0)
                j = max(j, 0)

            flip *= -1

    return zz_arr

if __name__ == '__main__':
    arr = [
        [1, 3, 4, 10],
        [2, 5, 9, 11],
        [6, 8, 12, 15],
        [7, 13, 14, 16],
    ]
    # arr = [[1]]
    ans = zigzagTraverse(arr)
    print(ans)