class Solution(object):
    def validUtf8(self, data):
        count = 0
        mask1 = 1 << 7
        mask2 = 1 << 6
        
        for num in data:
            if count > 0:
                if num & mask1 != 0 and num & mask2 == 0:
                    count -= 1
                else:
                    return False
            else:
                if num & mask1 == 0:
                    continue
                if num & mask2 == 0:
                    return False
                
                temp_mask = mask2
                while temp_mask & num != 0:
                    count += 1
                    temp_mask >>= 1
                    if count >= 4:
                        return False
                    
        return True if count == 0 else False

if __name__ == "__main__":
    sol = Solution()
    data = [145]
    print sol.validUtf8(data)
