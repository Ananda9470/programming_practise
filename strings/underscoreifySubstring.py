# O(m*n) | O(n)
def underscorifySubstring(string, substring):

    all_underscore_pos = getUnderScorePositions(string, substring)
    reduced_underscore_pos = reduceUnderscorePos(all_underscore_pos)
    underscored_string = underscorify(string, reduced_underscore_pos)

    return underscored_string

def getUnderScorePositions(string, substring):

    idx = 0
    all_indices = []
    while True:
        lwr_idx = string.find(substring, idx)

        if lwr_idx == -1:
            break

        all_indices.append([lwr_idx, lwr_idx+len(substring)])
        idx = lwr_idx+1

    return all_indices

def reduceUnderscorePos(all_underscore_pos):

    if len(all_underscore_pos) == 0:
        return []

    reduced_underscore_pos = [all_underscore_pos[0]]
    for next_underscore_pos in all_underscore_pos[1:]:

        prev_underscore_pos = reduced_underscore_pos[-1]

        if prev_underscore_pos[1] < next_underscore_pos[0]:
            reduced_underscore_pos.append(next_underscore_pos)
        else:
            reduced_underscore_pos.pop()
            reduced_underscore_pos.append([prev_underscore_pos[0], next_underscore_pos[1]])

    return reduced_underscore_pos

def underscorify(string, reduced_underscore_pos):

    underscored_array = []

    str_idx = 0
    underscore_pos_idx = 0
    for str_idx, char_to_append in enumerate(string):

        if underscore_pos_idx < len(reduced_underscore_pos):
            if str_idx == reduced_underscore_pos[underscore_pos_idx][0]:
                underscored_array.append("_")

        underscored_array.append(char_to_append)

        if underscore_pos_idx < len(reduced_underscore_pos):
            if str_idx == reduced_underscore_pos[underscore_pos_idx][1]-1:
                underscored_array.append("_")
                underscore_pos_idx += 1


    return "".join(underscored_array)


if __name__ == "__main__":
    string = "woah this testthis is a test to see somethingtest testtest test text testhappenstest"
    string = "test this is a test to see if it works"
    string = "testthis is a testest to see if testtestes it works test"
    substring = "ffdsfe"
    ans = underscorifySubstring(string, substring)
    print(ans)