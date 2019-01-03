'''
Finding Regular Total Distance
'''
from collections import defaultdict
import random
import time
import numpy as np

class Calculate_dist(object):
	def __init__(self):
		print("Enter Distance Calculation")

	def euc_dist(self, *args):
	    x1,y1,x2,y2=args
	    return np.sqrt((x1-x2)**2+(y1-y2)**2)

	def checkIdprime(self, cityid):
	    for i in range(2, cityid):
	        if cityid%i==0:
	            return False
	    return True

	def compare_windowed_dist(self, points, ref_point, cities):
	    x1,y1=cities['X'][ref_point],cities['Y'][ref_point]
	    distances = defaultdict(int)
	    for point in points:
	        x2,y2=cities['X'][point],cities['Y'][point]
	        distances[point]=self.euc_dist(x1,y1,x2,y2)
	    retpoint = min(distances, key=distances.get)
	    return retpoint
	        

	def form_random_tsp(self, numofcities, cities, random, Xinit, Yinit, include_xshift, sortedcities, window):
	    d = defaultdict(list)
	    res, visited = [0], []
	    distance=0
	    step=0
	    
	    ## This is for inluding y values after we receive the list of cities that are sorted based on x axis
	    if not include_xshift:
	        listofnodes = [i for i in range(1, numofcities)] if random else list(cities['CityId'][:])
	    else:
	        listofnodes = sortedcities
	    
	    if random:
	        x1,y1=cities['X'][0],cities['Y'][0]
	    else:
	        x1,y1=Xinit,Yinit
	    
	    start=time.time()
	    
	    while listofnodes:
	        if not include_xshift:
	            if random:
	                idx_ = np.random.randint(0,len(listofnodes)-1) if len(listofnodes) >1 else 0
	                pick=listofnodes[idx_]
	                listofnodes.remove(pick)
	            else:
	                pick=listofnodes.pop(0)
	            res.append(pick)
	            x2,y2=cities['X'][pick],cities['Y'][pick]
	            step+=1
	            if step%10==0:
	                distance+=self.euc_dist(x1,y1,x2,y2)
	            else:
	                temp=self.euc_dist(x1,y1,x2,y2)
	                if not self.checkIdprime(cities['CityId'][pick]):
	                    distance+=temp*(1.1)
	                else:distance+=temp
	            x1,y1=cities['X'][pick],cities['Y'][pick]
	        else:
	            if step==0:
	                ref=listofnodes.pop(0)
	                visited.append(ref)
	                points = listofnodes[:window-1]
	                next_pick=self.compare_windowed_dist(points=points, ref_point=ref, cities=cities)
	                position = listofnodes.index(next_pick)
	                x2,y2=cities['X'][next_pick],cities['Y'][next_pick]
	            else:
	                if len(listofnodes)>=window:
	                    ref = next_pick
	                    visited.append(ref)
	                    if position>=window-1:
	                        points = listofnodes[:window-1]
	                    else:
	                        points = listofnodes[:position]+listofnodes[position+1:window]
	                    listofnodes.remove(ref)
	                    next_pick=self.compare_windowed_dist(points=points, ref_point=ref, cities=cities)
	                    position = listofnodes.index(next_pick)
	                    x2,y2=cities['X'][next_pick],cities['Y'][next_pick]
	                else:
	                    next_pick = listofnodes.pop(0)
	                    visited.append(next_pick)
	                    x2,y2=cities['X'][next_pick],cities['Y'][next_pick]
	            step+=1
	            if step%10==0:
	                distance+=self.euc_dist(x1,y1,x2,y2)
	            else:
	                temp=self.euc_dist(x1,y1,x2,y2)
	                if not self.checkIdprime(cities['CityId'][next_pick]):
	                    distance+=temp*(1.1)
	                else:distance+=temp
	            x1,y1=cities['X'][next_pick],cities['Y'][next_pick]
	    if include_xshift: 
	        res=visited
	    end=time.time()
	    print(f'total time taken for random approach = {end-start}')
	    print(f'total distance = {distance}')
	    return res, distance
