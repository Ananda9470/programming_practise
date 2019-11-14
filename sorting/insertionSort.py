# O(n^2) | O(1)
# Θ(n^2) | O(1)
# Ω(n) | O(1)
def insertionSort(array):

    for i in range(1,len(array)):

        current = array[i]

        while i>0 and array[i-1]>current:
            array[i] = array[i-1]
            i = i-1
            array[i] = current

    return array

if __name__ == "__main__":
    array = [3, 4, 2, 9, 5, 6, 1, 4, 7, 8]
    array = [12, 10, 10, 11]
    ans = insertionSort(array)
    print(ans)