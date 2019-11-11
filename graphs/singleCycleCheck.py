# O(n) | O(1)
def hasSingleCycle(array):

    node_idx = 0
    node_val = array[node_idx]

    for _ in range(len(array)-1):

        node_idx = (node_val+node_idx)%len(array)
        node_val = array[node_idx]

        if node_idx == 0:
            return False

    node_idx = (node_val + node_idx) % len(array)
    if node_idx == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    array = [2, 3, 1, -4, -4, 2]
    # array = [1, 1, 1]
    # array = [1, -1, 1, -1]
    array = [0, 1, 1, 1, 1, 1]
    ans = hasSingleCycle(array)
    print(ans)