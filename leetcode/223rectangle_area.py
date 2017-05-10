class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        if E >= C or A >= G or F >= D or B >= H:
            length = height = 0
        else:
            length = ((C - A) + (G - E) - abs(A - E) - abs(C - G)) / 2
            height = ((D - B) + (H - F) - abs(B - F) - abs(D - H)) / 2
        double_area = length * height
        return (C - A) * (D - B) + (G - E) * (H - F) - double_area
