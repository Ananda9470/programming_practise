from functools import reduce

# O(n) | O(n)
def caesarCipherEncryptor(string, key):

    string = "_" + string

    enc_string = reduce(
        lambda s, c: s+chr(((ord(c)-97)+key)%26+97),
        string
    )
    return enc_string[1:]

if __name__ == '__main__':
    string = "xyz"
    key = 2
    ans = caesarCipherEncryptor(string, key)
    print(ans)
