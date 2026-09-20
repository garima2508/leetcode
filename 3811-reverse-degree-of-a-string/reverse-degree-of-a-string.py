class Solution(object):
    def reverseDegree(self, s):
        total_degree = 0
        for i, char in enumerate(s):
            reversed_index = 26 - (ord(char) - ord('a')) # Reverse alphabet index
            total_degree += reversed_index * (i + 1) # Multiply by position (1-indexed)
        return total_degree
        