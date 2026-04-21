"""
218. Bus Routes

Time Complexity: O(V + E) where V is stops, E is buses
Space Complexity: O(V + E)
"""
from typing import List
import collections

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
            
        adj = collections.defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                adj[stop].append(i)
                
        q = collections.deque([(source, 0)]) # stop, bus_count
        visit_stops = set([source])
        visit_buses = set()
        
        while q:
            stop, buses = q.popleft()
            if stop == target:
                return buses
                
            for bus in adj[stop]:
                if bus not in visit_buses:
                    visit_buses.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop not in visit_stops:
                            visit_stops.add(next_stop)
                            q.append((next_stop, buses + 1))
                            
        return -1
