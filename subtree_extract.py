import spacy
from nltk import Tree
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import json
import random
import pandas as pd
from pandas import DataFrame
import nltk
import numpy as np


def subtree():
	# file = open("Tree/people.person.nationality.txt",'r')
	# op = open("Subtree/people.person.nationality.txt",'a')
	file = open("Test/test_tree.txt",'r')
	op = open("Test/test_subtree.txt","w")
	new_f = file.readlines()

	test = []

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
	    test.append(item)


	new_file = []
	sub_l = []
	obj_l = []
	sub_count_l = []
	obj_count_l = []

	# Get index of subject and object
	class BreakIt(Exception): pass
	for test1 in test:
		obj = 0
		sub = 0
		try:
			for i,item in enumerate(test1):
				wordList = word_tokenize(item)
				for word in wordList:
					match_sub = re.match(r'SUBJECT.*',word)
					if match_sub is not None:
						word = re.sub(r'SUBJECT.*',"SUBJECT",word)
					if(word=="SUBJECT"):
						sub = test1.index(item)
						sub_l.append(sub)
						raise BreakIt
		except BreakIt:
			pass

		try:
			for i,item in enumerate(test1):
				wordList = word_tokenize(item)
				for word in wordList:
					match_obj = re.match(r'OBJECT.*',word)
					if match_obj is not None:
						word = re.sub(r'OBJECT.*',"OBJECT",word)
					if(word=="OBJECT"):
						obj = test1.index(item)
						obj_l.append(obj)
						raise BreakIt
		except BreakIt:
			pass
   
	position = [] #List of spaces for all sentences [[],[]]

	# Find subtree space of sub and obj
	for j,test1 in enumerate(test):
		sub_count = 0
		obj_count = 0
		item_count = 0
		length = len(test1)
		pos_sentence = []
		for i,item in enumerate(test1):
			if(i==length-1):
				pos_sentence.append(-1)
			else:
				item_count = item.count(" ")
				item_count = item_count - 2
				pos_sentence.append(item_count)
				if(i==sub_l[j]):
					sub_count = item.count(" ")
					sub_count = sub_count - 2
					sub_count_l.append(sub_count)
				if(i==obj_l[j]):
					obj_count = item.count(" ")
					obj_count = obj_count - 2
					obj_count_l.append(obj_count)
	    
		position.append(pos_sentence)
	
	pos_list_final = [] #Contains list of pos  for all sentences [[],[]]
	for j,test1 in enumerate(test):

	# SUB appears first
		if(sub_l[j]<obj_l[j]):
			pos_list = []  #List of pos for every sentence
			obj_pos = obj_l[j] #Position of object
			sub_pos = sub_l[j] #Position of subject
			obj_space = obj_count_l[j]  #Number of spaces in object
			sub_space = sub_count_l[j]  #Number of spaces in subject
			pos_list.append(obj_pos)
			pos_list.append(sub_pos)

        #Obj and sub on same space level
			try:
				if(sub_space == obj_space):
					for i,item in enumerate(test1):
						if(i>obj_l[j]):
							count = item.count(" ")
							count = count - 2
							if(count>obj_count_l[j]):
								pos_list.append(i)
							else:
								break
					for i,item in enumerate(test1):
						if(i>sub_l[j]):
							count = item.count(" ")
							count = count - 2
							if(count>sub_count_l[j]):
								pos_list.append(i)
							else:
								break
					k = obj_pos
					if(sub_space == 2) or (obj_space==2):
						for item in position[j]:
							if(item==0):
								pos_list.append(item)
								raise BreakIt
					else:
						while k>0:
							k = k-1
							if(position[j][k] > obj_space):
								k = k-1
							if(position[j][k] == obj_space):
								k = k-1
							if(position[j][k]<obj_space):
								a = k+1
								b = k-1
								if(position[j][a]>position[j][k]) and (position[j][b]<=position[j][k]):
									pos_list.append(k)
									if(position[j][b]>=position[j][k]):
										obj_ancestor = k
										break
									else:
										obj_ancestor = b
										pos_list.append(b)
										break

						while(k>sub_pos):
							k = k-1
						if(k==sub_pos):
							while k>0:
								k = k-1
								if(position[j][k] > sub_space):
									k = k-1
								if(position[j][k] == sub_space):
									k = k-1
								if(position[j][k]<sub_space):
									a = k+1
									b = k-1
									if(position[j][a]>position[j][k]) and (position[j][b]<=position[j][k]):
										pos_list.append(k)
										if(position[j][b]>=position[j][k]):
											sub_ancestor = k
											break
										else:
											sub_ancestor = b
											pos_list.append(b)
											break
							if(position[j][sub_ancestor]==position[j][obj_ancestor]):
								if(position[j][sub_ancestor]==2):
									while k>0:
										k = k-1
										if(position[j][k]==0):
											pos_list.append(k)
											raise BreakIt
								if(position[j][sub_ancestor]>2):
									k = sub_ancestor
									while k>0:
										k = k-1
										if(position[j][k] > position[j][sub_ancestor]):
											k = k-1
										if(position[j][k] == position[j][sub_ancestor]):
											k = k-1
										if(position[j][k]<position[j][sub_ancestor]):
											pos_list.append(k)
											raise BreakIt
                            
			except BreakIt:
				pass

        # Sub space lesser than Obj space
			try:
				if(sub_space<obj_space):
                    # sub_ancestor = -1
                    # obj_ancestor = -1
					for i,item in enumerate(test1):
						if(i>obj_l[j]):
							count = item.count(" ")
							count = count - 2
							if(count>obj_count_l[j]):
								pos_list.append(i)
							else:
								break
					for i,item in enumerate(test1):
						if(i>sub_l[j]):
							count = item.count(" ")
							count = count - 2
							if(count>sub_count_l[j]):
								pos_list.append(i)
							else:
								break
					k = obj_pos
					while k>0:
							k = k-1
							if(position[j][k] > obj_space):
								k = k-1
							if(position[j][k] == obj_space):
								k = k-1
							if(position[j][k]<obj_space):
								a = k+1
								b = k-1
								if(position[j][a]>position[j][k]) :
									if(position[j][b]>=position[j][k]):
										obj_ancestor = k
										pos_list.append(k)
										break
									else:
										obj_ancestor = b
										pos_list.append(k)
										pos_list.append(b)
										break
                                    

					if(sub_space <= position[j][obj_ancestor]):
						if(sub_space == 2):
							k = obj_ancestor - 1
							while(k>sub_pos):
								if(position[j][k] == 2):
									if(position[j][k]!=sub_space):
										pos_list.append(k)
									while k>0:
										k = k-1
										if(position[j][k]==0):
											pos_list.append(k)
											break
								else:
									k = k-1

						if(sub_space>2):
							k = sub_pos
							if(k-1 == 0):
								sub_ancestor = 0
							else : 
								while k>0:
									k = k-1
									if(position[j][k]>=sub_space):
										k = k-1
									if(position[j][k] < sub_space):
										sub_ancestor = k
										if(position[j][sub_ancestor]!=position[j][obj_ancestor]):
											pos_list.append(sub_ancestor)
											break

					if(sub_space > position[j][obj_ancestor]):
						k = sub_pos
						if(k-1 == 0):
							sub_ancestor = 0
						else:
							while k>0:
								k = k-1
								if(position[j][k]>=sub_space):
									k = k-1
								if(position[j][k] < sub_space):
									sub_ancestor = k
									if(position[j][sub_ancestor]!=position[j][obj_ancestor]):
										pos_list.append(sub_ancestor)
										break
									if(position[j][sub_ancestor]==position[j][obj_ancestor]):
										pos_list.append(sub_ancestor)
										while k>0:
											k = k-1
											if(position[j][k]==0):
												pos_list.append(k)
												break

			except BreakIt:
				pass

            # Sub_space greater than obj space
			try:
				if(sub_space>obj_space):
					for i,item in enumerate(test1):
						if(i>obj_l[j]):
							count = item.count(" ")
							count = count - 2
							if(count>obj_count_l[j]):
								pos_list.append(i)
							else:
								break
					for i,item in enumerate(test1):
						if(i>sub_l[j]):
							count = item.count(" ")
							count = count - 2
							if(count>sub_count_l[j]):
								pos_list.append(i)
							else:
								break
					k = obj_pos
					while k>0:
							k = k-1
							if(position[j][k] > obj_space):
								k = k-1
							if(position[j][k] == obj_space):
								k = k-1
							if(position[j][k]<obj_space):
								a = k+1
								b = k-1

								if(position[j][a]>position[j][k]) :
                                    # pos_list.append(k)

									if(position[j][b]>=position[j][k]):
										obj_ancestor = k
										pos_list.append(k)
										break
									else:
										obj_ancestor = b
										pos_list.append(b)
										break
							else : 
								obj_ancestor = obj_pos
					k = sub_pos
					while k>0:
						k = k-1
						if(position[j][k]>=sub_space):
							k = k-1
						if(position[j][k] < sub_space):
							sub_ancestor = k
							pos_list.append(k)
							break
                    
					if(position[j][sub_ancestor]<position[j][obj_ancestor]):
						pos_list.append(sub_ancestor)
					if(position[j][sub_ancestor] == position[j][obj_ancestor]):
						if(position[j][sub_ancestor] == 2):
							k = sub_ancestor
							while k > 0:
								k = k-1
								if(position[j][k]==0):
									pos_list.append(k)
									break
						if(position[j][sub_ancestor] > 2):
							k = sub_ancestor
							while k>0:
								k = k-1
								if(position[j][k]<position[j][sub_ancestor]):
									pos_list.append(k)
									break

					if(position[j][sub_ancestor]>position[j][obj_ancestor]):
						k = sub_ancestor
						while (position[j][k]>position[j][obj_ancestor]):
							k = k-1
							if(position[j][k]==position[j][obj_ancestor]):
								break

						pos_list.append(k)
						if(position[j][k] == 2):
							z = k
							while z > 0:
								z = z-1
								if(position[j][z]==0):
									pos_list.append(z)
									break
						if(position[j][k] > 2):
							z = k
							while z>0:
								z = z-1
								if(position[j][z]<position[j][k]):
									pos_list.append(z)
									break

			except BreakIt:
				pass



        # OBJ appears first
		if(sub_l[j]>obj_l[j]):
			pos_list = []  #List of pos for every sentence
			obj_pos = obj_l[j] #Position of object
			sub_pos = sub_l[j] #Position of subject
			# print(obj_pos)
			# print(sub_pos)
			obj_space = obj_count_l[j]  #Number of spaces in object
			sub_space = sub_count_l[j]  #Number of spaces in subject
			pos_list.append(obj_pos)
			pos_list.append(sub_pos)
            #print(pos_list)

        #Sub space = Obj space
			try:
				if(sub_space == obj_space):
					for i,item in enumerate(test1):
						if(i>obj_l[j]):
							count = item.count(" ")
							count = count - 2
							if(count>obj_count_l[j]):
								pos_list.append(i)
							else:
								break
					for i,item in enumerate(test1):
						if(i>sub_l[j]):
							count = item.count(" ")
							count = count - 2
							if(count>sub_count_l[j]):
								pos_list.append(i)
							else:
								break
					k = sub_pos
					if(sub_space == 2) or (obj_space==2):
						for item in position[j]:
							if(item==0):
								pos_list.append(item)
								raise BreakIt
					else:
						while k>0:
							k = k-1
							if(position[j][k] > sub_space):
								k = k-1
							if(position[j][k] == sub_space):
								k = k-1
							if(position[j][k] < sub_space):
								a = k+1
								b = k-1
								if(position[j][a]>position[j][k]) and (position[j][b]<=position[j][k]):
									pos_list.append(k)
									if(position[j][b]>=position[j][k]):
										sub_ancestor = k
										break
									else:
										sub_ancestor = b
										pos_list.append(b)
										break

						while(k>obj_pos):
							k = k-1
						if(k==obj_pos):
							while k>0:
								k = k-1
								if(position[j][k] > obj_space):
									k = k-1
								if(position[j][k] == obj_space):
									k = k-1
								if(position[j][k]<obj_space):
									a = k+1
									b = k-1
									if(position[j][a]>position[j][k]) and (position[j][b]<=position[j][k]):
										pos_list.append(k)
										if(position[j][b]>=position[j][k]):
											obj_ancestor = k
											break
										else:
											obj_ancestor = b
											pos_list.append(b)
											break
                            


							if(position[j][sub_ancestor]==position[j][obj_ancestor]):
								if(position[j][obj_ancestor]==2):
									while k>0:
										k = k-1
										if(position[j][k]==0):
											pos_list.append(k)
											raise BreakIt
                                    
								if(position[j][obj_ancestor]>2):
									k = obj_ancestor
									while k>0:
										k = k-1
										if(position[j][k] > position[j][obj_ancestor]):
											k = k-1
										if(position[j][k] == position[j][obj_ancestor]):
											k = k-1
										if(position[j][k]<position[j][obj_ancestor]):
											pos_list.append(k)
											raise BreakIt
			except BreakIt:
				pass

    #Obj space lesser than sub space
			try:
				if(sub_space>obj_space):
					for i,item in enumerate(test1):
						if(i>obj_l[j]):
							count = item.count(" ")
							count = count - 2
							if(count>obj_count_l[j]):
								pos_list.append(i)
							else:
								break
					for i,item in enumerate(test1):
						if(i>sub_l[j]):
							count = item.count(" ")
							count = count - 2
							if(count>sub_count_l[j]):
								pos_list.append(i)
							else:
								break
					k = sub_pos
					while k>0:
                            #print("Inf1")
							k = k-1
							if(position[j][k] > sub_space):
								k = k-1
							if(position[j][k] == sub_space):
								k = k-1
							if(position[j][k]<sub_space) :
								a = k+1
								b = k-1

								if(position[j][a]>position[j][k])   :
									if(position[j][b]>=position[j][k]):
                                        
										sub_ancestor = k
										pos_list.append(k)
										break
									else:
										sub_ancestor = b
										pos_list.append(b)
										break

					if(obj_space <= position[j][sub_ancestor]):
						if(obj_space == 2):
							k = sub_ancestor - 1
							while(k>obj_pos):
								if(position[j][k] == 2):
									pos_list.append(k)
									while k>0:
										k = k-1
										if(position[j][k]==0):
											pos_list.append(k)
											raise BreakIt
								else:
									k = k-1
						if(obj_space>2):
							k = obj_pos
							while k>0:
								k = k-1
								if(position[j][k]>=obj_space):
									k = k-1
								if(position[j][k] < obj_space):
									obj_ancestor = k
									if(position[j][obj_ancestor]!=position[j][sub_ancestor]):
										pos_list.append(obj_ancestor)
										raise BreakIt

					if(obj_space > position[j][sub_ancestor]):
						k = obj_pos
						while k>0:
							k = k-1
							if(position[j][k]>=obj_space):
								k = k-1
							if(position[j][k] < obj_space):
								obj_ancestor = k
								if(position[j][obj_ancestor]!=position[j][sub_ancestor]):
									pos_list.append(obj_ancestor)
									raise BreakIt
								if(position[j][obj_ancestor]==position[j][sub_ancestor]):
									pos_list.append(obj_ancestor)
									while k>0:
										k = k-1
										if(position[j][k]==0):
											pos_list.append(k)
											raise BreakIt
                                      
                                        
			except BreakIt:
				pass

        # Obj space greater than subject space
			try:
				if(sub_space<obj_space):
					for i,item in enumerate(test1):
						if(i>obj_l[j]):
							count = item.count(" ")
							count = count - 2
							if(count>obj_count_l[j]):
								pos_list.append(i)
							else:
								break
					for i,item in enumerate(test1):
						if(i>sub_l[j]):
							count = item.count(" ")
							count = count - 2
							if(count>sub_count_l[j]):
								pos_list.append(i)
							else:
								break
					k = sub_pos
					while k>0:
							k = k-1
							if(position[j][k] > sub_space):
								k = k-1
							if(position[j][k] == sub_space):
								k = k-1
							if(position[j][k]<sub_space):
								a = k+1
								b = k-1

								if(position[j][a]>position[j][k]) :
                                    # pos_list.append(k)

									if(position[j][b]>=position[j][k]):
										sub_ancestor = k
										pos_list.append(k)
										break
									else:
										sub_ancestor = b
										pos_list.append(b)
										break
							else :
								sub_ancestor = sub_pos
					k = obj_pos
					while k>0:
						k = k-1
						if(position[j][k]>=obj_space):
							k = k-1
						if(position[j][k] < obj_space):
							obj_ancestor = k
							pos_list.append(k)
							break

                    #print(obj_ancestor)
					if(position[j][obj_ancestor]<position[j][sub_ancestor]):
						pos_list.append(obj_ancestor)
					if(position[j][sub_ancestor] == position[j][obj_ancestor]):
						if(position[j][obj_ancestor] == 2):
							k = obj_ancestor
							while k > 0:
								k = k-1
								if(position[j][k]==0):
									pos_list.append(k)
									break
						if(position[j][obj_ancestor] > 2):
							k = obj_ancestor
							while k>0:
								k = k-1
								if(position[j][k]<position[j][obj_ancestor]):
									pos_list.append(k)
									break

					if(position[j][obj_ancestor]>position[j][sub_ancestor]):
						k = obj_ancestor
						while (position[j][k]>position[j][sub_ancestor]):
							k = k-1
							if(position[j][k]==position[j][sub_ancestor]):
								break

						pos_list.append(k)
						if(position[j][k] == 2):
							z = k
							while z > 0:
								z = z-1
								if(position[j][z]==0):
									pos_list.append(z)
									break
						if(position[j][k] > 2):
							z = k
							while z>0:
								z = z-1
								if(position[j][z]<position[j][k]):
									pos_list.append(z)
									break

			except BreakIt:
				pass





		
		#pos_list_final.append(pos_list)
		final_list = list(set(pos_list))
		final_list.sort(reverse=False)
		

		new_list = []
		for item in final_list:
			new_list.append(test[j][item])
		for item in new_list:
			it = item.replace("\n","")
			print(it,file=op)
		print("\n",file=op)


	print("Subtree")

def main():
	subtree()

main()


