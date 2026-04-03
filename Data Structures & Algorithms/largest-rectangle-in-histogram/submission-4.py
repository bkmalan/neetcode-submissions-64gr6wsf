class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            if not stack:
                stack.append((i,heights[i]))
            else:
                currentMaxArea = 0
                startIndex = i
                while stack and stack[-1][1] > heights[i]: 
                    index, height = stack.pop()
                    maxArea = max(maxArea,height*(i - index))
                    startIndex = index
                stack.append((startIndex,heights[i]))
                maxArea = max(currentMaxArea,maxArea) 
        
        while stack:
            index, height = stack.pop()
            area = (len(heights) - index) * height
            maxArea = max(maxArea, area)
        
        return maxArea