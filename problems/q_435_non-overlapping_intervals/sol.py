class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        length = len(intervals)
        def getMinimum(first, second,removed):
            if second < length:
                if intervals[second][0] < intervals[first][1]:              # overlap
                    if intervals[second][1] < intervals[first][1]:          # greedy: pick the interval with smaller scope
                        return getMinimum(second, second + 1, removed + 1) 
                    else:
                        return getMinimum(first, second + 1, removed + 1)
                else:
                    return getMinimum(second, second + 1, removed)          # no overlap
                
            return removed                                                  # the end of the list
        
        return getMinimum(0, 1, 0)                                          # (first_element, second_element, NumberOfRemovedElement)