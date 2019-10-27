# O(n) \ O(1)
def findThreeLargestNumbers(array):

    l1 = float("-inf")
    l2 = float("-inf")
    l3 = float("-inf")
    for n in array:
        if n > l1:
            l3 = l2
            l2 = l1
            l1 = n
        elif n > l2:
            l3 = l2
            l2 = n
        elif n > l3:
            l3 = n
    return [l3, l2, l1]

if __name__ == "__main__":
    array = [5, -5, 10, 10, 7, 8, 20]
    ans = findThreeLargestNumbers(array)
    print(ans)