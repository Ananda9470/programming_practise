# O(n^2) | O(1)
# Θ(n^2) | O(1)
# Ω(n) | O(1)
def bubbleSort(array):
    for counter in range(len(array)-1):
        for i in range(0, len(array) - counter -1):
            if array[i+1] > array[i]:
                array[i+1], array[i] = array[i], array[i+1]
    return sorted(array)

if __name__ == "__main__":
    array = [3, 4, 2, 9, 5, 6, 1, 4, 7, 8]
    ans = bubbleSort(array)
    print(ans)