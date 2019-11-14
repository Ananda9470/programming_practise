# O(n^2) | O(1)
# Θ(n^2) | O(1)
# Ω(n^2) | O(1)
def selectionSort(array):

    for idx in range(len(array)):
        min_idx = array[idx:].index(min(array[idx:]))+idx
        array[idx], array[min_idx] = array[min_idx], array[idx]

    return array

if __name__ == "__main__":
    array = [3, 4, 2, 9, 5, 6, 1, 4, 7, 8]
    array = [12, 10, 10, 11]
    ans = selectionSort(array)
    print(ans)