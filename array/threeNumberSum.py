import itertools


# O(n^3)|O(1)
def threeNumberSum1(arr, s):
    all_trips = []
    for triplet in itertools.combinations(arr, r=3):
        arr_sum = sum(triplet)
        if arr_sum == s:
            all_trips.append(sorted(triplet))
    return all_trips

# O(n^2)|O(n)
def threeNumberSum2(arr, s):
    arr = sorted(arr)
    all_trips = []

    for i in range(len(arr) - 2):

        left = i+1
        right = len(arr)-1

        while(left < right):
            trip_sum = arr[i] + arr[left] + arr[right]
            if trip_sum > s:
                right -= 1
            elif trip_sum < s:
                left += 1
            else:
                all_trips.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

    return all_trips

# O(n^2)|O(1)
# Is not a complete solution because doesn't order the final array
def threeNumberSum3(arr, s):

    all_trips = []
    for i in range(len(arr)-2):

        n1 = arr[i]
        arr_hash = set()
        for j in range(i+1, len(arr)):

            n2 = arr[j]

            required_diff = s - (n1+n2)
            if required_diff in arr_hash:
                all_trips.append(sorted([n1, n2, required_diff]))
            else:
                arr_hash.add(n2)

    return all_trips


if __name__ == '__main__':
    arr = [8, 10, -2, 49, 14]
    s = 57
    ans = threeNumberSum3(arr, s)
    print(ans)
