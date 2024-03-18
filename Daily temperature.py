class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temp)
        for index,value in enumerate(temp):
            while stack and value>temp[stack[-1]]:
                result[preIndex]=index-(preIndex:=stack.pop())
            stack.append(index)
        return result
with open('user.out', 'w') as f:
    for case in map(loads, stdin):
        f.write(f"[{','.join([str(x) for x in Solution().dailyTemperatures(case)])}]\n")
exit()