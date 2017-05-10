class Solution(object):
    def validUtf8(self, data):
        count = 0
        mask1, mask2 = 1 << 7, 1 << 6
        
        for num in data:
            if count == 0:
                if num & mask1 == 0:
                    continue
                mask = mask1
                while num & mask:
                    count += 1
                    mask >>= 1
                if count == 1 or count > 4: return False
                count -= 1
            elif num & mask1 != 0 and num & mask2 == 0:
                count -= 1
            else:
                return False
                
        return False if count else True

            
          
