# O(n) | O(d)
def productSum(array, multiplier=1):

    return sum([
        ele if isinstance(ele, int)
        else productSum(ele, multiplier + 1)
        for ele in array
    ])*multiplier

if __name__ == "__main__":
    array = [1, 2, 3, [4, 5, [5, 6], 7], 8]
    ans = productSum(array)
    print(ans)