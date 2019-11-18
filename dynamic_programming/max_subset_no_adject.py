# O(n) | O(n)
def maxSubsetSumNoAdjacent(array):
    sum, _ = maxSubsetSumNoAdjacentRecursor(array, sum_hash={})
    return sum

def maxSubsetSumNoAdjacentRecursor(array, sum_hash):

    if len(array) == 0:
        return 0, sum_hash

    if len(array) == 1:
        return array[0], sum_hash

    if len(array) == 2:
        if 2 in sum_hash:
            return sum_hash[2], sum_hash
        else:
            sum_hash[2] = max(array[0], array[1])
            return sum_hash[2], sum_hash

    if len(array) == 3:
        if 3 in sum_hash:
            return sum_hash[3], sum_hash
        else:
            sum_hash[3] = max(array[0]+array[2], array[1])
            return sum_hash[3], sum_hash

    if len(array[1:]) in sum_hash:
        sum_subset_1 = sum_hash[len(array[1:])]
    else:
        sum_subset_1, sum_hash = maxSubsetSumNoAdjacentRecursor(array[1:], sum_hash)
        sum_hash[len(array[1:])] = sum_subset_1

    if len(array[2:]) in sum_hash:
        sum_subset_2 = sum_hash[len(array[2:])] + array[0]
    else:
        sum_subset_2, sum_hash = maxSubsetSumNoAdjacentRecursor(array[2:], sum_hash)
        sum_subset_2 = sum_subset_2 + array[0]

    sum_hash[len(array)] = sum_subset_2
    return max(sum_subset_1, sum_subset_2), sum_hash

if __name__ == "__main__":
    array = [75, 105, 120, 75, 90, 135]
    ans = maxSubsetSumNoAdjacent(array)
    print(ans)