'''
Local TSP Solver- Implementing the 2-opt method to solve a TSP.
'''

import sys, os
import pandas as pd
from glob import glob
import numpy as np
from itertools import combinations_with_replacement, combinations, permutations
from haversine import haversine
import time
from concorde.tsp import TSPSolver
from find_dist import Calculate_dist

class Two_opt(object):
	'''Using the 2-opt algoirthm to improve on the TSP solver'''
	def __init__(self,arg):
		'''Return the global variable cities as a numpy array.'''
		self.path = arg
		self.newpoints = []
		for f in glob(self.path+"/*.csv", recursive=True):
			if 'cities' in f:
				self.cities = pd.read_csv(f, usecols = ['X','Y']).values
				self.cities_raw = pd.read_csv(f)
			if 'submission_29_orig_' in f:
				self.route = pd.read_csv(f)
				print(self.route.head())
		self.route_new = sorted(self.route['Path'][:2000])
		for v in self.route_new:
			self.newpoints.append(self.cities[v])

	def useConcordeSolver(self):
		pass

	def cost(self, cost_mat, route):
		#print(f"here do {np.roll(route, 1)}, globe \n {route}")
		return cost_mat[np.roll(route, 1), route].sum()

	def two_opt(self, cost_mat, route):
		best=route
		improved=True
		while improved:
			improved=False
			for i in range(1, len(route)-2):
				for j in range(i+1, len(route)):
					if j-i==1:
						continue
					new_route=route[:]
					new_route[i:j] = route[j-1:i-1:-1] # This is the 2-opt swap
					if self.cost(cost_mat, new_route)<self.cost(cost_mat, best):
						best=new_route
						improved=True
						route=best
		return best

	def saving_adj_mat_method2(self, ind1, ind2):
		'''Utility funtion to Calculate the haversine distance for the cost matrix.'''
		start=time.time()
		adj_mat =  np.empty(2000**2)
		points = self.newpoints[ind1:ind2]
		flag=False
		count=0
		cl=0
		adj_mat_list = []
		# for i, (point1, point2) in enumerate(combinations_with_replacement(points,2)):
		# 	if i%10==0 and i>0 and not flag:
		# 		idx=i//10
		# 		while idx>0:
		# 			adj_mat[i]=adj_mat[idx]
		# 			idx-=1
		# 			adj_mat[i+1]=haversine(point1, point2)
		# 			flag=True	
		# 	else:
		# 		if flag:
		# 			count=i
		# 			count+=1
		# 			adj_mat[count]=haversine(point1, point2)
		# 			flag=False
		# 		else:
		# 			adj_mat[count]=haversine(point1, point2)
		# 			count+=1
		for (point1,point2) in combinations_with_replacement(points, 2):
			# if cl%11==0:
			# 	adj_mat_list.append(haversine(point1, point1))
			# 	cl+=1
			adj_mat_list.append(haversine(point1, point2))
			cl+=1
		newlist = [[None]*2000 for i in range(2000)]
		close=[]
		start=2000
		for i in range(2000):
			if i>=1:
				close=[]
				#print(f'i is {i}')
				for x in range(i):
					#print("index = ", i-x-1 , newlist[i-x-1])
					close.append(newlist[i-x-1][i])
				close=close[::-1]
				#print("close", close)
				val, indx, stack=None,0,[adj_mat_list[start]]
				while val!=0:
					start+=1
					if start<len(adj_mat_list):
						val=adj_mat_list[start]
					else:
						break
					stack.append(val)
				if i<(2000-1):stack.pop()
				#newlist[i] = close+adj_mat_list[10*i-i+1:(10*i)+(10-i)]
				newlist[i] = close+stack
			if i==0:newlist[i] = close+adj_mat_list[2000*i:(2000*i)+(2000-i)]
		#print(f"newlist printed here {newlist}")
		#adj_mat_list.append(haversine(point1,point1))
		adj_mat_new=np.asarray(newlist)
		#adj_mat_new.reshape(20000,20000)
		# for i in range(10):
		# 	adj_mat = np.concatenate((adj_mat[0:((10*i)+i)],[haversine(points[i], points[i])],adj_mat[((10*i)+i):]), axis=0)
		# adj_mat=adj_mat[:10**2]
		#adj_mat.reshape(10, 10)
		print(len(adj_mat_new))
		end=time.time()
		print(f'Time taken for {round(float(end-start),3)}')
		return adj_mat_new

	def saving_adj_mat_method1(self, ind1, ind2):
		'''Utility funtion to Calculate the haversine distance for the cost matrix.'''
		start=time.time()
		adj_mat =  np.empty(10**2)
		points = self.cities[ind1:ind2]
		for i, (point1, point2) in enumerate(permutations(points,2)):
			adj_mat[i]=haversine(point1, point2)
		for i in range(10):
			adj_mat = np.concatenate((adj_mat[0:((10*i)+i)],[haversine(points[i], points[i])],adj_mat[((10*i)+i):]), axis=0)
		adj_mat=adj_mat[:10**2]
		adj_mat.reshape(10, 10)
		end=time.time()
		print(f'Time taken for {round(float(end-start),3)}')
		return adj_mat
	
	def adjmat(self):
		'''Function to calculate the adj Matrix/Cost matrix.'''
		adj_mat1 =  np.empty(2000**2)
		adj_mat2 =  np.empty(20000**2)
		adj_mat3 =  np.empty(20000**2)
		adj_mat4 =  np.empty(20000**2)
		adj_mat5 =  np.empty(20000**2)
		adj_mat6 =  np.empty(20000**2)
		adj_mat7 =  np.empty(20000**2)
		adj_mat8 =  np.empty(20000**2)
		adj_mat9 =  np.empty(20000**2)
		adj_mat10 = np.empty((len(self.cities)-(9*20000))**2)

		#print(self.cities[:5])
		print(f'Number of new cities {len(self.newpoints)}')

		
		# 1st 20k points
		#adj_mat1 	= self.saving_adj_mat_method1(0,20000)
		adj_mat1c 	= self.saving_adj_mat_method2(0,2000)
		
		'''
		#2nd 20k points
		adj_mat2 = self.saving_adj_mat(20000,40000)

		#3rd 20k points
		adj_mat3 = self.saving_adj_mat(40000,60000)

		#4th 20k points
		adj_mat4 = self.saving_adj_mat(60000,80000)

		#5th 20k points
		adj_mat5 = self.saving_adj_mat(80000,100000)

		#6th 20k points
		adj_mat6 = self.saving_adj_mat(100000,120000)

		#7th 20k points
		adj_mat7 = self.saving_adj_mat(120000,140000)

		#8th 20k points
		adj_mat8 = self.saving_adj_mat(140000,160000)

		#9th 20k points
		adj_mat9 = self.saving_adj_mat(160000,180000)

		# #Last points
		adj_mat10 = self.saving_adj_mat(180000,len(self.cities))
		'''
		#store the array
		# file = self.path + '/adjmat_method1.npz'
		# np.savez(file, adj_mat1)

		file = self.path + '/adjmat_method2.npz'
		np.savez(file, adj_mat1c)

	def getnumpyarr(self):
		'''loading the pre-calculated numpy matrices'''
		datavals = []
		for f in glob(self.path + "/*.npz", recursive=True):
			datavals.append(np.load(f))
		return datavals

	def getcompletemat(self, *args):
		'''Get the matrix reshaped and combined to be used for the algorithm.'''
		data1 = args[0]
		arr1 = data1['arr_0'].reshape(2000, 2000)
		# arr2 = data1['arr_1'].reshape(20000, 20000)
		# arr3 = data1['arr_2'].reshape(20000, 20000)
		# arr4 = data1['arr_3'].reshape(20000, 20000)
		# arr5 = data1['arr_4'].reshape(20000, 20000)
		# arr6 = data1['arr_5'].reshape(20000, 20000)
		# arr7 = data1['arr_6'].reshape(20000, 20000)
		# arr8 = data1['arr_7'].reshape(20000, 20000)
		# arr9 = data2['arr_0'].reshape(20000, 20000)
		# arr10 = data2['arr_1'].reshape((len(self.cities)-(9*20000)), (len(self.cities)-(9*20000)))
		start=time.time()
		#print(f"enter complete 2-opt : {arr1}")
		indices = [self.route_new.index(v) for v in self.route['Path'][:2000]]
		return self.two_opt(arr1, indices)
		end=time.time()
		print(f'Time taken for 2-opt is {end-start}')

	def getnewpath_after_2opt(self, changed_path):
		return [self.route_new[ind] for ind in changed_path]

	def get_total_distance(self, obj_, starter):
		numofcities=len(self.cities)
		x1, y1 = self.cities_raw['X'][0], self.cities_raw['Y'][0]
		print(f"Number of cities {numofcities}")
		chosen_res = starter+list(self.route['Path'][2000:])
		citieshere = self.cities_raw
		print(f'checking the original distance')
		obj_.form_random_tsp(numofcities, citieshere, False,  x1, y1, True, list(self.route['Path']), 5)
		print(f'checking the 2-opt distance')
		obj_.form_random_tsp(numofcities, citieshere, False,  x1, y1, True, chosen_res, 5)
		#return res, distance

if __name__ == "__main__":
	wd = os.getcwd()
	path = wd.split("/")
	newpath = "/".join(path[:-1])
	check_npz=False
	for f in glob(newpath + "/*.npz", recursive=True):
		check_npz=True
	obj=Two_opt(newpath)
	if not check_npz:obj.adjmat()
	datalist = obj.getnumpyarr()
	
	for i in range(len(datalist)):
		print(f'data present \n data1 - {datalist[i]} \n')
		print(f'keys of data1 {datalist[i].files}')
		best_route = obj.getcompletemat(datalist[i])
		file = newpath + '/best_route.npz'
		np.savez(file, best_route)
	
	# for i in range(len(datalist)):
	# 	print(f'data present \n data1 - {datalist[i]} \n')
	# 	print(f'keys of data1 {datalist[i].files}')
	# 	if i==0: changed_path = datalist[i]['arr_0']

	# starter = obj.getnewpath_after_2opt(changed_path)

	# dist = Calculate_dist()
	# res, total_distance = obj.get_total_distance(dist, starter)