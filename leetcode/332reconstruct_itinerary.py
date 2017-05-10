from collections import defaultdict, deque
import time
class Solution(object):
    #Solution1, dfs with backtracing
    def findItinerary(self, tickets):
        def dfs(source):
            if len(res) == len(tickets) + 1:
                return res
            edges = sorted(graph[source])
            for edge in edges:
                res.append(edge)
                graph[source].remove(edge)
                if dfs(edge):
                    return res
                graph[source].append(edge)
                res.pop()
            
        graph = defaultdict(list)
        res = ["JFK"]
        for flight in tickets:
            graph[flight[0]].append(flight[1])

        return dfs("JFK")

    #Solution2, use deque for the loop
    def findItinerary2(self, tickets):
        def dfs(source):
            if len(res) >= len(tickets) + 1:
                return True
            if source not in graph or len(graph[source]) == 0:
                return False
            i= 0
            while i < len(graph[source]):
                new_source = graph[source].pop()
                res.append(new_source)
                if dfs(new_source):
                    return True
                res.pop()
                graph[source].appendleft(new_source)
                i += 1
            return False
        
        graph = defaultdict(list)
        for flight in tickets:
            graph[flight[0]].append(flight[1])
        for key in graph:
            graph[key].sort(reverse = True)
            graph[key] = deque(graph[key])
        res = ["JFK"]
        if dfs("JFK"):
            return res
        return []
            
    #Solution3, Eulerian path, use greedy DFS
    def findItinerary3(self, tickets):
        def dfs(source):
            while source in graph and len(graph[source]) > 0:
                new_source = graph[source][-1]
                graph[source].pop()
                dfs(new_source)
            res.append(source)
                
        graph = defaultdict(list)
        for flight in tickets:
            graph[flight[0]].append(flight[1])
        for key in graph:
            graph[key].sort(reverse = True)
        res = []
        dfs("JFK")
        return res[::-1]
            
if __name__ == "__main__":
    tickets = [["ADL","EZE"],["SYD","CNS"],["ELH","BNE"],["CBR","MHH"],["BNE","MHH"],["AXA","SYD"],["FPO","CNS"],["BAK","FPO"],["MHH","ADL"],["DAC","LST"],["INN","CBR"],["BAH","BAK"],["JFK","BAK"],["BRU","OOL"],["CBR","AXA"],["BAK","CNS"],["DAC","BGI"],["FPO","AUA"],["PER","AUA"],["ELH","BRU"],["NAS","CRL"],["DRW","TBI"],["TBI","GGT"],["SYD","HBA"],["DAC","BAH"],["BAH","SYD"],["CNS","LST"],["ELH","EZE"],["EZE","BAK"],["CRL","CBR"],["CNS","DRW"],["LST","CNS"],["SYD","NAS"],["DRW","CBR"],["AUA","ANU"],["MHH","JFK"],["EZE","GGT"],["TCB","AUA"],["LST","AXA"],["DRW","HBA"],["TIA","ELH"],["GGT","BNE"],["TIA","TBI"],["BRU","INN"],["MEL","AXA"],["CNS","MHH"],["BAH","JFK"],["TCB","INN"],["NAS","PER"],["DRW","BAH"],["JFK","CNS"],["GGT","DAC"],["BGI","NAS"],["GGT","TIA"],["BIM","JFK"],["CBR","DRW"],["BAH","DRW"],["BAK","VIE"],["CRL","PER"],["BIM","CRL"],["TBI","CBR"],["OOL","BRU"],["GGT","OOL"],["AUA","BAH"],["DAC","EZE"],["VIE","BIM"],["MHH","FPO"],["TBI","TIA"],["BGI","VIE"],["JFK","CBR"],["INN","DAC"],["AUA","OOL"],["ADL","JFK"],["CNS","BAH"],["FPO","TIA"],["BAK","INN"],["AXA","BRU"],["PER","MEL"],["CBR","NAS"],["BGI","ASD"],["OOL","GGT"],["VIE","TCB"],["TIA","JFK"],["FPO","AXA"],["NAS","BIM"],["LST","EZE"],["ANU","DRW"],["BNE","TIA"],["ASD","CNS"],["OOL","VIE"],["EZE","CRL"],["BAH","EZE"],["PER","DRW"],["OOL","JFK"],["EZE","BIM"],["NAS","GGT"],["BIM","MEL"],["BAK","TCB"],["BNE","BGI"],["DRW","GGT"],["AUA","CBR"],["DRW","BRU"],["BIM","BNE"],["BGI","OOL"],["BAH","ASD"],["CBR","NAS"],["JFK","CNS"],["INN","AUA"],["DRW","GGT"],["NAS","ADL"],["GGT","ANU"],["VIE","CNS"],["AXA","COO"],["BNE","DRW"],["CNS","PER"],["BRU","ASD"],["CNS","DAC"],["JFK","DRW"],["AXA","BGI"],["FPO","DAC"],["BIM","CNS"],["VIE","SYD"],["CRL","OOL"],["ASD","PER"],["BGI","ELH"],["GGT","EZE"],["ADL","NAS"],["CBR","BNE"],["MEL","GGT"],["JFK","BIM"],["HBA","PER"],["ASD","BGI"],["HBA","GGT"],["OOL","TIA"],["EZE","MHH"],["HBA","VIE"],["INN","HBA"],["TCB","ELH"],["MHH","CRL"],["AXA","FPO"],["MEL","BRU"],["CNS","BGI"],["BRU","INN"],["TBI","AUA"],["TIA","FPO"],["PER","BRU"],["CRL","LST"],["TIA","INN"],["OOL","NAS"],["BNE","AXA"],["GGT","BNE"],["ADL","TBI"],["NAS","BAH"],["SYD","LST"],["MEL","CNS"],["ANU","DRW"],["GGT","BNE"],["CNS","BAK"],["BRU","MEL"],["LST","TIA"],["BNE","CNS"],["TIA","ADL"],["PER","BAK"],["CNS","FPO"],["VIE","TCB"],["EZE","ADL"],["AUA","SYD"],["BRU","OOL"],["INN","DAC"],["CNS","FPO"],["ASD","BAH"],["DRW","BIM"],["CNS","VIE"],["JFK","MEL"],["DAC","ASD"],["FPO","TBI"]]
    # tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    sol = Solution()
    time1 = time.time()
    print sol.findItinerary(tickets)
    print "solution1 --- %s second ---" % (time.time() - time1)
    time2 = time.time()
    print sol.findItinerary2(tickets)
    print "solution2 --- %s second ---" % (time.time() - time2)
    time3 = time.time()
    print sol.findItinerary3(tickets)
    print "solution3 --- %s second ---" % (time.time() - time3)
        

        
        
