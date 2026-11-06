class Solution(object):
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda log: log[1])
        sorted_queries = sorted((time, i) for i, time in enumerate(queries) )

        arr = [0]*len(queries)
        freq={}
        left=0
        right=0

        for time, idx in sorted_queries:
            start=time-x
            while right<len(logs) and logs[right][1]<=time:
                server=logs[right][0]
                freq[server]=freq.get(server,0)+1
                right+=1

            while left<right and logs[left][1]<start:
                server=logs[left][0]
                freq[server]-=1
                if freq[server]==0:
                    del freq[server]
                left+=1
            
            arr[idx]=n-len(freq)
        return arr

'''solution that caused tle ie. not optimal:
class Solution(object):
    def countServers(self, n, logs, x, queries):
        arr=[]
        
        for q in queries:
            active=set()
            for server,time in logs:
                if q-x<=time<=q:
                    active.add(server)
            arr.append(n-len(active))

        return arr'''