def getPermutations(array):

    if len(array) == 1:
        return [array]

    if len(array) == 2:
        return [[array[0], array[1]], [array[1], array[0]]]

    perms = []
    for ele in array:
        reduced_array = [a for a in array if a is not ele]
        reduced_perms = getPermutations(reduced_array)

        for reduced_perm in reduced_perms:
            perm = [ele] + reduced_perm
            perms.append(perm)

    return perms

if __name__ == "__main__":
    array = [1, 2, 3, 4]
    ans = getPermutations(array)
    print(len(ans))
