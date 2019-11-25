def minNumberOfCoinsForChange(n, denoms):
    n_coins = minNumberOfCoinsForChangeHelper(n, denoms)
    if n_coins == float("inf"):
        return -1
    return n_coins

def minNumberOfCoinsForChangeHelper(n, denoms):

    if n == 0:
        return 0

    if len(denoms) == 1:
        if (n%denoms[0]) == 0:
            return n//denoms[0]
        else:
            return -1

    list_prev = minNumberOfCoinsForChangeHelper(n, denoms[:-1])

    if denoms[-1] > n:
        n_prev = float("inf")
    else:
        n_prev = minNumberOfCoinsForChangeHelper(n-denoms[-1], denoms)

    if list_prev == -1:
        n_coins = n_prev+1
    else:
        n_coins = min(list_prev, n_prev+1)

    return n_coins


if __name__ == "__main__":
    n = 7
    denoms = [1, 5, 10]

    ans = minNumberOfCoinsForChange(n, denoms)
    print(ans)
