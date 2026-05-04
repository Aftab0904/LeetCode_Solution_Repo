import collections

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        initial_z = s.count('0')
        if initial_z == 0:
            return 0

        # Two DSUs to skip visited states for even and odd zero counts
        p_even = list(range(n // 2 + 2))
        p_odd = list(range((n - 1) // 2 + 2))

        def find(i, p):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != root:
                next_node = p[i]
                p[i] = root
                i = next_node
            return root

        def mark_visited(z):
            if z % 2 == 0:
                idx = z // 2
                p_even[idx] = find(idx + 1, p_even)
            else:
                idx = z // 2
                p_odd[idx] = find(idx + 1, p_odd)

        dist = [-1] * (n + 1)
        dist[initial_z] = 0
        mark_visited(initial_z)

        queue = collections.deque([initial_z])

        while queue:
            curr_z = queue.popleft()
            if curr_z == 0: return dist[0]

            # x = zeros flipped. Z' = curr_z + k - 2x
            low_x = max(0, k - (n - curr_z))
            high_x = min(k, curr_z)

            min_z = curr_z + k - 2 * high_x
            max_z = curr_z + k - 2 * low_x

            parity = (curr_z + k) % 2
            p = p_even if parity == 0 else p_odd

            idx = find(min_z // 2, p)
            while idx * 2 + parity <= max_z:
                next_z = idx * 2 + parity
                if dist[next_z] == -1:
                    dist[next_z] = dist[curr_z] + 1
                    queue.append(next_z)
                    p[idx] = find(idx + 1, p)
                idx = find(idx, p)

        return -1