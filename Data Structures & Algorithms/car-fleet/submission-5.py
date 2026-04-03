class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position,speed))
        stack = []
        for pos,s in pairs[::-1]:
            dist = target - pos
            time = dist / s
            if stack:
                if time > stack[-1]:
                    stack.append(time)
                else:
                    stack.append(max(time,stack.pop()))
            else:
                stack.append(time)
        return len(stack)
