import itertools

# O(n^4)|O(n)
def fourNumberSum1(arr, s):
    all_sums = []
    for quad in itertools.combinations(arr, r=4):
        q_sum = sum(quad)
        if q_sum == s:
            all_sums.append(quad)
    return all_sums
#--------------------------------------------------------------------------------------------------

from collections import defaultdict

# O(n^3)|O(n^2)
# Θ(n^2)|O(n^2)
def fourNumberSum2(arr, s):

    arr_hash = defaultdict(lambda: [])
    found_quads = []
    arr_l = len(arr)

    for i in range(arr_l):

        n1 = arr[i]

        for j in range(i+1, arr_l):

            n2 = arr[j]
            P = n1+n2
            required_diff = s - P

            if required_diff in arr_hash:
                for pair in arr_hash[required_diff]:
                    quad = pair + [n1, n2]
                    found_quads.append(quad)
            else:
                pass

        for k in range(0, i):

            n2 = arr[k]
            P = n1+n2
            required_diff = s - P

            arr_hash[P].append([n1, n2])

    return found_quads
#--------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    arr = [-1, 1, 2, 4, 6, 7]
    s = 16
    ans = fourNumberSum2(arr, s)
    print(ans)
