class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        res = []

        # Split the string into its independent "Special" components
        for j, char in enumerate(s):
            count += 1 if char == '1' else -1
            if count == 0:
                # Recursively process the inner part of the special string
                # Every special string starts with 1 and ends with 0
                res.append('1' + self.makeLargestSpecial(s[i + 1 : j]) + '0')
                i = j + 1

        # Sort components in descending order to make the string lexicographically largest
        res.sort(reverse=True)

        return "".join(res)