# O(n) | O(1)
def isPalindrome1(string):

    left = 0
    right = len(string)-1
    while left<right:

        if string[left] != string[right]:
            return False

        left += 1
        right -= 1

    return True

# O(n) | O(n)
def isPalindrome2(string):
    if len(string) == 0:
        return True
    else:
        return string[0]==string[-1] and isPalindrome2(string[1:-1])

if __name__ == '__main__':
    string = "malayalam"
    ans = isPalindrome1(string)
    print(ans)
