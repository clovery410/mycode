class Solution(object):
    def isReflected(self, points):
        yaxis = collections.defaultdict(set)
        for x, y in points:
            yaxis[y].add(x)

        reflection_line = None
        for val in yaxis.values():
            row = sorted(val)
            s, e = 0, len(row) - 1
            while s <= e:
                if reflection_line == None:
                    reflection_line = (row[e] - row[s]) / 2.0 + row[s]
                elif reflection_line != (row[e] - row[s]) / 2.0 + row[s]:
                    return False
                s += 1
                e -= 1
        return True

    #solution2, learned from discuss, find the smallest and largest x value, then if there is a reflection line, it must be (largest - smallest) / 2 + smallest, just check whether each pair has an opposite pair towards this line.
    def isReflected2(self, points):
        pairs = set()
        min_x, max_x = sys.maxint, -sys.maxint-1
        for x, y in points:
            pairs.add((x, y))
            min_x = min(min_x, x)
            max_x = max(max_x, x)

        reflection_sum = max_x + min_x
        for x, y in points:
            if (reflection_sum - x, y) not in pairs:
                return False
        return True
            
