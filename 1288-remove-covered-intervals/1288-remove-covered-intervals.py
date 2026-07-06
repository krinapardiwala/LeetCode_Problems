class Solution(object):
    def removeCoveredIntervals(self, intervals):
        def sort_interval(interval):
            return (interval[0],-interval[1])
        intervals.sort(key=sort_interval)

        count=0
        max_right=0

        for left, right in intervals:
            if right>max_right:
                count+=1
                max_right=right

        return count