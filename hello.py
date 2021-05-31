def isPalindrome(s):
    # simple idea, two pointers
    # one point the last index, another point the first index, and sliding them facing to each other
    if len(s)==0:
        return True
    left, right = 0, len(s)-1
    while left!=right:
        # if s[left] is not a char or digit, move right
        if not s[left].isalpha() and not s[left].isdigit():
            print('here')
            left += 1
            continue
        if not s[right].isalpha() and not s[right].isdigit():
            right -= 1
            continue

        if s[left]==s[right] or s[left].isalpha() and s[right].isalpha() and s[left].lower()==s[right].lower():
            print('left and rihgt are ', s[left], s[right])
            left += 1
            right -= 1
        else:
            return False
    return left==right

print(isPalindrome("race a car"))

