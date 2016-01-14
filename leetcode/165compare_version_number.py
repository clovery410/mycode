class Solution(object):
    def compareVersion(self, version1, version2):
        curr_1, _v1 = 0, []
        for item in version1:
            if item == '.':
                _v1.append(curr_1)
                curr_1 = 0
            else:
                curr_1 = curr_1 * 10 + int(item)
        _v1.append(curr_1)
        
        curr_2, _v2 = 0, []
        for item in version2:
            if item == '.':
                _v2.append(curr_2)
                curr_2 = 0
            else:
                curr_2 = curr_2 * 10 + int(item)
        _v2.append(curr_2)
        
        i = 0
        n_1, n_2 = len(_v1), len(_v2)
        while True:
            if i >= n_1 and i >= n_2:
                return 0
            
            elif i >= n_1:
                if _v2[i] != 0:
                    return -1
                else:
                    i += 1
                    continue
                
            elif i >= n_2:
                if _v1[i] != 0:
                    return 1
                else:
                    i += 1
                    continue
                
            elif _v1[i] < _v2[i]:
                return -1
            
            elif _v1[i] > _v2[i]:
                return 1
            
            i += 1
