class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            if not stack:
                stack.append((i,heights[i]))
            else:
                currentMaxArea = 0
                noPopped = 0
                lastIndex = i
                while stack and stack[-1][1] > heights[i]: 
                    index, height = stack[-1] 
                    currentMaxArea = max(currentMaxArea,height*(i - index))
                    noPopped += 1
                    lastIndex = index
                    stack.pop()
                stack.append((lastIndex,heights[i]))
                maxArea = max(currentMaxArea,maxArea) 
        while stack:
            index, height = stack.pop()
            area = (len(heights) - index) * height
            maxArea = max(maxArea, area)
        
        return maxArea