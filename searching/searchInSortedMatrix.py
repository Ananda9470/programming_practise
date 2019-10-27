# O(n+m) \ O(1)
def searchInSortedMatrix(matrix, target):
    r = 0
    c = len(matrix[0])-1

    while r<len(matrix) and c>=0:
        n = matrix[r][c]
        if n > target:
            c -= 1
        elif n < target:
            r += 1
        else:
            return [r, c]

    return [-1, -1]


if __name__ == "__main__":
    matrix = [
        [10, 13, 30, 40, 50],
        [11, 21, 31, 41, 51],
        [12, 22, 42, 43, 52],
        [13, 23, 45, 46, 53],
        [20, 24, 47, 48, 57],
    ]
    target = 100
    ans = searchInSortedMatrix(matrix, target)
    print(ans)