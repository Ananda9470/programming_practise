# O(2^n) | O(n)
def getNthFib1(n):

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib1(n-1) + getNthFib1(n-2)

# O(n) | O(n)_
def getNthFib2(n, memoize={1:0, 2: 1}):
    
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib2(n-1, memoize) + getNthFib2(n-2, memoize)
        return memoize[n]
    
if __name__ == "__main__":
    N = 20
    ans = getNthFib2(N)
    print(ans)