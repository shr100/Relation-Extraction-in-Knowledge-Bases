import numpy as np
import math
import sys
import scipy.sparse as sp
from scipy.sparse import *
from sys import getsizeof
import random

def data_mat():
	file = open("Test/test_subtree.txt","r")
	# op = open("Data_Matrix/people.person.spouse.txt","w")
	# file = open("Subtree/test_sub.txt","r")
	op = open("Test/Intermediate/test_int.txt","w+")
	output = open("Test/Output/test_output.txt","w")
	new_f = file.readlines()
	file.close()

	filtered_list = []

	length = len(new_f)
	new_file1 = []
	i=0
	n_indexes = []
	n_indexes.append(0)
	while i<length :
		if(new_f[i] == '\n'):
			n_indexes.append(i+1)
		i = i+1
	j=0
	while j<(len(n_indexes)-1):
		new_file1.append(new_f[n_indexes[j]:n_indexes[j+1]])
		j = j+1
   
	for i,item in enumerate(new_file1):
		filtered_list.append(item)

	
	new_list = []

	for item in filtered_list:
		if(len(item) == 1):
			continue
		else:
			new_list.append(item)

	filtered_list = new_list
	length_filter = len(filtered_list)


	print("Length of original list : ",length_filter)
	new = []

	if(length_filter > 10):
		index = []
		for i in range(length_filter):
			index.append(i)


		index_list  = random.sample(index,10)

		#new = []
		for i in index_list :
			print(filtered_list[i],file=op)
			new.append(filtered_list[i])
		op.close()

	else :
		new = filtered_list

	print("Length of new list : ", len(new))


	i=0
	data_matrix = dok_matrix((len(new), len(new)), dtype=np.float32)
	# print(data_matrix[0,0])
	# print("Size in bytes : ",getsizeof(data_matrix))

	




	i=0

	while i<len(new):
		j=0
		while j<len(new):
			if(i!=j):
				list1 = list(set(new[i]).intersection(new[((j)%len(new))]))
				data_matrix[i,j] = float(len(list1)-1)
				print ("i : {} , j: {} , Sim : {} ".format(str(i),str(j), str(float(len(list1)-1))),file=output)
				j = j+1
			else:
				data_matrix[i,j] = 0.0
				print ("i : {} , j: {} , Sim : {} ".format(str(i),str(j), str(0.0)),file=output)
				j=j+1
		i = i+1

	# print(data_matrix)

	
	i = 0
	j = 0
	for i in range(len(new)):
		for j in range(len(new)):
			data_matrix[i,j] = data_matrix[i,j] + 0.01
			j = j+1
		i = i+1

	
	
	data_matrix_mat = data_matrix.toarray()
	print("Data matrix")
	return data_matrix_mat



# def main():
#  	data_mat()

# main()
