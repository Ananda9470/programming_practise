from collections import defaultdict

# O(n) | O(n)
def longestSubstringWithoutDuplication(string):

    char_hash = defaultdict(lambda : float("-inf"))
    unq_str = ""
    lower_idx = 0

    for upper_idx, c in enumerate(string):

        if (c in char_hash) and (char_hash[c] >= lower_idx):
            lower_idx = char_hash[c] + 1
        else:
            unq_str = max(
                unq_str,
                string[lower_idx: upper_idx + 1],
                key=lambda s: len(s)
            )

        char_hash[c] = upper_idx

    return unq_str

if __name__ == "__main__":
    string = "abcb"
    # string = "clementisacap"
    # string = "abcdeabcdefc"
    ans = longestSubstringWithoutDuplication(string)
    print(ans)  # abcdef