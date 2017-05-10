class Solution(object):
    def findMaximumXOR(self, nums):
        if len(nums) <= 1:
            return 0
        
        # build trie
        trie = {}
        for num in nums:
            root = trie
            mask = 1 << 31
            for i in xrange(32):
                cur_bit = 0 if num & mask == 0 else 1
                if cur_bit not in root:
                    root[cur_bit] = {}
                root = root[cur_bit]
                num >>= 1

        res = 0
        for num in nums:
            root = trie
            xor_res = 0
            for i in xrange(32):
                mask = 1 << (31 - i)
                num_bit = 0 if num & mask == 0 else 1
                cur_bit = 0 if num_bit == 1 else 0
                if cur_bit in root:
                    xor_res += mask
                    root = root[cur_bit]
                else:
                    root = root[num_bit]
            res = max(res, xor_res)

        return res

        
                    
                
