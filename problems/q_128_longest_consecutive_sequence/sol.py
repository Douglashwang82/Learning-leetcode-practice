class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        my_dict = {number: 1 for number in nums}
        maximum = [0]
        visited = set()
        
        def dfs(x, start):
            visited.add(x)
            
            next = my_dict.get(x + 1)
            if next:
                if x + 1 in visited:
                    my_dict[start] += next
                else:
                     my_dict[start] += 1
                     dfs(x + 1, start)
        
            maximum[0] = max(my_dict[start], maximum[0])
                        
        for number in nums:
            if number not in visited:
                dfs(number, number)
        
        return maximum[0]