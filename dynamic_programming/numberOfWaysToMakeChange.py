# O(nd) | O(n)
def numberOfWaysToMakeChange1(n, denoms):
    ways = [0]*(n+1)
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[-1]

def numberOfWaysToMakeChange2(n, demons):
    return numberOfWaysToMakeChangeRecursor(n, demons)

def numberOfWaysToMakeChangeRecursor(n, denoms):

    if n == 0:
        return 1

    if len(denoms) == 1:
        if (n%denoms[0]) == 0:
            return 1
        else:
            return 0

    n_slef = numberOfWaysToMakeChange(n, denoms[:-1])

    if denoms[-1] > n:
        n_prev = 0
    else:
        n_prev = numberOfWaysToMakeChange(n-denoms[-1], denoms)

    n_ways = n_slef + n_prev

    return n_ways

if __name__ == "__main__":

    n = 20
    denoms = [1, 2, 4, 10, 20, 25]

    ans = numberOfWaysToMakeChange1(n, denoms)
    print(ans)