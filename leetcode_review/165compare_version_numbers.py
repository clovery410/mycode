class Solution(object):
    def compareVersion(self, version1, version2):
        start_idx1 = start_idx2 = 0
        end_idx1 = end_idx2 = 0
        while True:
            if start_idx1 >= len(version1) or start_idx2 >= len(version2):
                break
            while end_idx1 < len(version1) and version1[end_idx1] != '.':
                end_idx1 += 1
            while end_idx2 < len(version2) and version2[end_idx2] != '.':
                end_idx2 += 1

            num1 = int(version1[start_idx1:end_idx1])
            num2 = int(version2[start_idx2:end_idx2])
            if num1 < num2:
                return -1
            if num1 > num2:
                return 1
            else:
                end_idx1 += 1
                start_idx1 = end_idx1
                end_idx2 += 1
                start_idx2 = end_idx2
        if start_idx1 < len(version1):
            for i in xrange(start_idx1, len(version1)):
                if version1[i] not in '.0':
                    return 1
        if start_idx2 < len(version2):
            for i in xrange(start_idx2, len(version2)):
                if version2[i] not in '.0':
                    return -1
        return 0

if __name__ == "__main__":
    sol = Solution()
    v1 = "1.2"
    v2 = "1.25"
    print sol.compareVersion(v1, v2)
