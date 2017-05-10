class Solution(object):
    def minWindow(self, s, t):
        count = collections.defaultdict(int)
        for c in t:
            count[c] += 1

        total_cnt = len(t)
        min_len = len(s) + 1
        start_idx = res_idx = idx = 0

        while True:
            if idx >= len(s):
                break
            
            c = s[idx]
            if count[c] > 0:
                total_cnt -= 1
            count[c] -= 1

            # if cnt == 0, it's a valid window now, then make it invalid
            while start_idx <= idx and total_cnt == 0:
                if idx - start_idx < min_len:
                    min_len = idx - start_idx
                    res_idx = start_idx
                if count[s[start_idx]] == 0:
                    total_cnt += 1
                count[s[start_idx]] += 1
                start_idx += 1

            idx += 1

        return s[res_idx:res_idx + min_len] if min_len < len(s) + 1 else ''
            
