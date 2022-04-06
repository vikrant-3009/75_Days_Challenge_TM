class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nsel = []
        nser = [0] * n
        
        # nsel -> next smaller element on the left 
        st = []
        for i in range(n):
            while len(st) > 0 and st[-1][0] >= heights[i]:
                st.pop()
                
            if len(st) > 0:
                nsel.append(st[-1][1])
            else:
                nsel.append(-1)
                
            st.append([heights[i], i])
            
        # nser -> next smaller element on the right
        st = []
        for i in range(n-1, -1, -1):
            while len(st) > 0 and st[-1][0] >= heights[i]:
                st.pop()
            
            if len(st) > 0:
                nser[i] =  st[-1][1]
            else:
                nser[i] = n
            
            st.append([heights[i], i])
        
        # Now, calculate the area
        area = []
        for i in range(n):
            a = (nser[i] - nsel[i] - 1) * heights[i]
            area.append(a)
        
        return max(area)