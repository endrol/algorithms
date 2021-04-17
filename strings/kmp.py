"""kmp algorithm
"""


# get next array
#  abacdab
# [-1, 0, -1, 1, 0, -1, 0]
def get_next(p):
    """p is the pattern string"""
    next_array = [-1] * len(p)
    len_p = len(p)
    k = -1
    j = 0
    while j < len_p - 1:
        if k == -1 or p[j] == p[k]:
            k += 1
            j += 1
            if p[j] != p[k]:
                next_array[j] = k
            else:
                next_array[j] = next_array[k]

        else:
            k = next_array[k]

    return next_array


# search if string p belongs to string s
# if so, return the index of p
def kmp_search(s, p):
    """return the start index of matched s and p"""
    len_s, len_p = len(s), len(p)
    next_p = get_next(p)
    i, j = 0, 0
    while i < len_s and j < len_p:
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next_p[j]

    if j == len_p:
        return i - j
    else:
        return -1


def main():
    print(get_next('abacdab'))
    print(kmp_search('abcdabcd', 'bcda'))


if __name__ == "__main__":
    main()
