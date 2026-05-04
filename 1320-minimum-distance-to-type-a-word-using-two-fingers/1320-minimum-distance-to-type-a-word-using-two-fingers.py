class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_dist(c1, c2):
            if c1 == 26: return 0 # Free start for the second finger
            r1, col1 = divmod(c1, 6)
            r2, col2 = divmod(c2, 6)
            return abs(r1 - r2) + abs(col1 - col2)

        chars = [ord(c) - ord('A') for c in word]
        # dp[other] is min distance when one finger is at current_char
        # and the other finger is at character 'other' (26 = not placed)
        dp = [0] * 27

        for i in range(len(word) - 1):
            curr, next_char = chars[i], chars[i+1]
            new_dp = [float('inf')] * 27

            for other in range(27):
                if dp[other] == float('inf'): continue

                # Option 1: Move the finger currently at 'curr' to 'next_char'
                new_dp[other] = min(new_dp[other], dp[other] + get_dist(curr, next_char))

                # Option 2: Move the finger currently at 'other' to 'next_char'
                # (The other finger then stays at 'curr')
                new_dp[curr] = min(new_dp[curr], dp[other] + get_dist(other, next_char))

            dp = new_dp

        return min(dp)