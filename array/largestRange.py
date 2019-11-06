# O(n) | O(n)
def largestRange(arr):

    arr_set = set(arr)

    largest_range = []
    largest_range_len = 0

    while arr_set:
        n = arr_set.pop()
        range_of_n = [n, n]

        i = 1
        while True:
            m = n+i
            if m in arr_set:
                range_of_n[1] = m
                arr_set.remove(m)
                i += 1
            else:
                break
        i=1
        while True:
            m = n-i
            if m in arr_set:
                range_of_n[0] = m
                arr_set.remove(m)
                i += 1
            else:
                break

        if largest_range_len <= (range_of_n[1]-range_of_n[0]):
            largest_range = range_of_n
            largest_range_len = range_of_n[1]-range_of_n[0]

    return largest_range

if __name__ == "__main__":
    arr = [1]
    ans = largestRange(arr)
    print(ans)