def isPalindrome(s):
    newstr = ""
    for c in s:
        if c.isalnum():
            newstr += c.lower()
    return newstr == newstr[::-1]


if __name__ == "__main__":
    isPalindrome("A man, a plan, a canal: Panama")
