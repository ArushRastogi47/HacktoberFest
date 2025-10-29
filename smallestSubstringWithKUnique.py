class Solution:
    def smallestSubstringWithKUnique(self, s: str, k: int) -> str:
        n = len(s)
        unique_chars = set(s)
        if k > len(unique_chars):  
            return ""

        left = 0
        freq = {}
        unique = 0
        min_len = float('inf')
        start = 0

        for right in range(n):
            char = s[right]
            freq[char] = freq.get(char, 0) + 1
            if freq[char] == 1:
                unique += 1

            
            while unique > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    unique -= 1
                    del freq[s[left]]
                left += 1

            
            if unique == k and (right - left + 1) < min_len:
                min_len = right - left + 1
                start = left

        return s[start:start + min_len] if min_len != float('inf') else ""
