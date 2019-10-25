import itertools

# O(n^4)|O(n)
def fourNumberSum1(arr, s):
    all_sums = []
    for quad in itertools.combinations(arr, r=4):
        q_sum = sum(quad)
        if q_sum == s:
            all_sums.append(quad)
    return all_sums

if __name__ == '__main__':
    arr = [-1, 1, 2, 4, 6, 7]
    s = 16
    ans = fourNumberSum1(arr, s)
    print(ans)
