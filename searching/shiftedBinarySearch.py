def shiftedBinarySearch(array, target):

    start_idx = 0
    end_idx = len(array)-1
    mid_idx = (start_idx+end_idx)//2

    while True:

        start_n = array[start_idx]
        mid_n = array[mid_idx]
        end_n = array[end_idx]

        if (mid_idx == start_idx) or (mid_idx == end_idx):
            if target == start_n:
                return start_idx
            if target == end_n:
                return end_idx
            return -1

        if mid_n == target:
            return mid_idx

        if start_n >= end_n > mid_n:  # break in the left side of mid

            if mid_n < target < end_n:
                start_idx = mid_idx+1
            else:
                end_idx = mid_idx-1

        elif mid_n > start_n > end_n:  # break in the right side of the mid

            if start_n <= target < mid_n:
                end_idx = mid_idx-1
            else:
                start_idx = mid_idx+1

        elif end_n > mid_n > start_n:

            if start_n <= target < mid_n:
                end_idx = mid_idx-1
            else:
                start_idx = mid_idx+1

        mid_idx = (start_idx+end_idx)//2


if __name__ == "__main__":
    array = [7, 8, 9, 10, 0, 1, 2, 2, 3, 4, 5, 6]
    target = 2
    ans = shiftedBinarySearch(array, target)
    print(ans)