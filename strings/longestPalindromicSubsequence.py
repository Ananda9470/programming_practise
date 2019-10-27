def longestPalindromeWithCenter(string, left, right):

    while (left>=0) and right<(len(string)):

        if string[left] == string[right]:
            left -= 1
            right += 1
        else:
            break

    return left+1, right-1
# O(n^2) | O(1)
def longestPalindromicSubstring(string):

    longest_palindrome = float("-inf")
    array_bounds = [0, 1]
    for i in range(1, len(string)-1):

        odd_left, odd_right = longestPalindromeWithCenter(string, i-1, i+1)
        length_of_odd_pal = odd_right - odd_left + 1

        even_left, even_right = longestPalindromeWithCenter(string, i, i+1)
        length_of_even_pal = max(even_right - even_left, 0) + 1

        if length_of_odd_pal > longest_palindrome:
            longest_palindrome = length_of_odd_pal
            array_bounds = [odd_left, odd_right]

        if length_of_even_pal > longest_palindrome:
            longest_palindrome = length_of_even_pal
            array_bounds = [even_left, even_right]

    return string[array_bounds[0]:array_bounds[1]+1]

if __name__ == '__main__':
    string = "absdefzzzz"
    ans = longestPalindromicSubstring(string)
    print(ans)
