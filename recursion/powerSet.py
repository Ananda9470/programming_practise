def powerset(array, power_set=[[]]):

    if len(array) == 0:
        return power_set

    if len(array) == 1:
        power_set.append(array)
        return power_set

    if len(array) == 2:
        return [
            [],
            [array[0]],
            [array[1]],
            array
        ]

    for ele in array:
        reduced_array = [e for e in array if e is not ele]

        if reduced_array not in power_set:
            reduced_power_set = powerset(reduced_array, power_set)
            power_set.extend([ps for ps in reduced_power_set if ps not in power_set])

    power_set.append(array)

    return power_set

if __name__ == "__main__":
    array = [1, 2, 3]
    ans = powerset(array)
    print(ans)