class Solution(object):
    def strStr(self, haystack, needle):
        haystack_len = len(haystack)
        needle_len = len(needle)

        for i in range(haystack_len - needle_len + 1):
            if haystack[i:i + needle_len] == needle:
                return i
        return -1
        