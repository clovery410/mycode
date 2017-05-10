class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        if A >= G or C <= E or B >= H or D <= F:
            overlap = 0
        else:
            length = min(C, G) - max(A, E)
            height = min(D, H) - max(B, F)
            overlap = length * height

        return (C - A) * (D - B) + (G - E) * (H - F) - overlap

    

    
