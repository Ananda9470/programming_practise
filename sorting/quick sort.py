import random
random.seed(30)

def quickSort(array):

    if len(array) == 0 or len(array) == 1:
        return array

    if len(array) == 2:
        if array[0] > array[1]:
            return list(reversed(array))
        else:
            return array

    pivot_idx = get_pivot_idx(array)
    array,correct_pivot = sort_out_pivot(array, pivot_idx)

    left_array = quickSort(array[: correct_pivot])
    right_array = quickSort(array[correct_pivot+1 :])

    return left_array + [array[correct_pivot]] + right_array

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
    array = [-1, 4, 2, 9, 5, 6, 1, 7, 7, 10]
    array = [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]
    # array = [-4, -10, -6, -4, -5, -1]
    # array = [2, 1]
    ans = quickSort(array)
    print(ans)