class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Total number of unique binary codes of size k is 2^k
        needed_count = 1 << k
        seen = set()

        # Iterate through the string with a window of size k
        for i in range(len(s) - k + 1):
            # Extract the current substring of length k
            code = s[i : i + k]
            seen.add(code)

            # Early exit: if we've already found all 2^k codes
            if len(seen) == needed_count:
                return True

        return len(seen) == needed_count