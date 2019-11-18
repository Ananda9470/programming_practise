import random

def quickselect(array, k):

    pivot_idx = get_pivot_idx(array)
    array, sorted_idx = sort_out_pivot(array, pivot_idx)

    if sorted_idx+1 == k:
        return array[sorted_idx]
    elif sorted_idx+1 > k:
        k_small_ele = quickselect(array[:sorted_idx], k)
    else:
        k_small_ele = quickselect(array[sorted_idx+1:], k-sorted_idx-1)

    return k_small_ele

def sort_out_pivot(array, pivot_idx):

    pivot_ele = array[pivot_idx]
    swap_indices_of_array(array, pivot_idx, -1)

    left_idx = 0
    right_idx = len(array)-2
    while True:

        while array[left_idx] <= pivot_ele:
            left_idx += 1
            if left_idx >= len(array)-1:
                return array, len(array)-1

        while array[right_idx] >= pivot_ele:
            right_idx -= 1
            if right_idx <= -1:
                swap_indices_of_array(array, 0, -1)
                return array, 0

        if left_idx>=right_idx:
            break

        swap_indices_of_array(array, left_idx, right_idx)

        left_idx += 1
        right_idx -= 1

    swap_indices_of_array(array, left_idx, -1)
    return array, left_idx

def get_pivot_idx(array):
    return random.randint(0, len(array)-1)

def swap_indices_of_array(array, i, j):
    array[i], array[j] = array[j], array[i]

if __name__ == "__main__":
    array = [5, 6, 1, 3, 10, 9, 4, 8, 2, 7]
    k = 4
    ans = quickselect(array, k)
    print(ans)