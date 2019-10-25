import itertools

# O(n^2)|O(1)
def twoNumberSum1(arr, s):
    for pair in itertools.combinations(arr, r=3):
        print(pair)
        pair_sum = sum(pair)
        if pair_sum == s:
            return sorted(pair)
    return []

# O(n)|O(n)
def twoNumberSum2(arr, s):
    nums = set()
    for n in arr:
        potential_match = s - n
        if potential_match in nums:
            return sorted([n, s-n])
        else:
            nums.add(n)
    return []

# O(nlog(n))|O(1)
def twoNumberSum3(arr, s):
    arr = sorted(arr)

    left = 0
    right = len(arr)-1

    while(left<right):
        expected_sum = arr[left] + arr[right]
        if expected_sum > s:
            right -= 1
        elif expected_sum < s:
            left += 1
        else:
            return [arr[left], arr[right]]

    return []

if __name__ == '__main__':
    arr = [7,1,3,2,4,5,6]
    s = 8
    ans = twoNumberSum3(arr, s)
    print(ans)
