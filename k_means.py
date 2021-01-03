import numpy as np

import nltk
from nltk.cluster.kmeans import KMeansClusterer
from nltk import cluster
import sklearn.cluster
import distance
import random_sample

def k_means_cluster():
    print("K means")

    # file = open("Subtree/sports.team.pro_athlete.txt","r")
    # op_pos = open("K_means/sports.team.pro_athlete_pos.txt","w")
    # op_neg = open("K_means/sports.team.pro_athlete_neg.txt","w")

    file = open("Test/test_subtree.txt","r")
    op_pos = open("Test/test_sub_pos.txt","w")
    op_neg = open("Test/test_sub_neg.txt","w") 

    new_list = file.readlines()
    new = []
    filtered_list = []
    temp_list = []

    for item in new_list:
        new.append(item)
        if(item=="\n"):
            temp_list.append(new)
            new = []

    for item in temp_list:
        if(len(item)==1):
            continue
        else:
            filtered_list.append(item)

    data_matrix = random_sample.data_mat()
    new = filtered_list
    NUM_CLUSTERS = 5
    print("Start assigning clusters")
    kclusterer = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance, repeats=100, avoid_empty_clusters=True)
    assigned_clusters = kclusterer.cluster(data_matrix, assign_clusters=True)
    #print("Assigned clusters ",assigned_clusters)
    c0 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    for item in assigned_clusters:
        if (item==0):
            c0 = c0+1
        if (item==1):
            c1 = c1+1
        if (item==2) :
            c2 = c2+1
        if (item==3) :
            c3 = c3+1
        if (item==4) :
            c4 = c4+1

    maximum = max(c0,c1,c2,c3,c4)
    print("Cluster grouping")
    if(maximum==c0):
        pos = []
        neg = []
        positive_pos = []
        negative_pos = []
        second_max = max(c1,c2,c3,c4)
        if (second_max == c1) :
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 1):
                    print(new[item],file=op_pos)

                    
                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_neg)
                    
                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_neg)
                   
        if (second_max == c2) :
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_pos)
                    
                if (assigned_clusters[item] == 1):
                    print(new[item],file=op_neg)
                    
                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_neg)


        if (second_max == c3) :
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_pos)
                    
                if (assigned_clusters[item] == 1):
                    print(new[item],file=op_neg)
                    
                    
                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_neg)


                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_pos)
                    

                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_neg)

        if (second_max == c4) :
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 1):
                    print(new[item],file=op_neg)
                   
                    
                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_neg)
                    

                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_pos)
                    
            

    if(maximum==c1):
        pos = []
        neg = []
        positive_pos = []
        negative_pos = []
        second_max = max(c0,c2,c3,c4)
        if(second_max == c0):
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 1):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_pos)
                    
                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_neg)
            
        if(second_max == c2):
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 1):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_neg)
                    
                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_neg)
            
        if(second_max == c3):
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 1):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_neg)
                    
                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_neg)
            
            return pos,neg,positive_pos,negative_pos
        if(second_max == c4):
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 1):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_neg)
                    
                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_pos)
            

    if(maximum==c2):
        pos = []
        neg = []
        positive_pos = []
        negative_pos = []
        second_max = max(c0,c1,c3,c4)
        if(second_max == c0):
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_pos)
                    
                if (assigned_clusters[item] == 1):       
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_neg)
            
            
        if(second_max == c1):
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_neg)
                    

                if (assigned_clusters[item] == 1):       
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_neg)
            
           
        if(second_max == c3):
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_neg)
                    
                if (assigned_clusters[item] == 1):       
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_neg)
            
            
        if(second_max == c4):
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_neg)
                    
                if (assigned_clusters[item] == 1):       
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_pos)
            
    

    if(maximum==c3):
        pos = []
        neg = []
        positive_pos = []
        negative_pos = []
        second_max = max(c0,c1,c2,c4)
        if(second_max == c0):
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_pos)
                    
                if (assigned_clusters[item] == 1):       
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_neg)
            
        if(second_max == c1):
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_neg)
                    
                if (assigned_clusters[item] == 1):       
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_neg)
            
            
        if(second_max == c2):
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_neg)
                    
                if (assigned_clusters[item] == 1):       
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_neg)
            
            return pos,neg,positive_pos,negative_pos
        if(second_max == c4):
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_neg)
                    
                if (assigned_clusters[item] == 1):       
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_pos)
            

    if(maximum==c4):
        pos = []
        neg = []
        positive_pos = []
        negative_pos = []
        second_max = max(c0,c1,c2,c3)
        if(second_max == c0):
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_pos)
                    
                if (assigned_clusters[item] == 1):       
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_neg)
            
           
        if(second_max == c1):
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_neg)
                    
                if (assigned_clusters[item] == 1):       
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_neg)
            
            
        if(second_max == c2):
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_neg)
                    
                if (assigned_clusters[item] == 1):       
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_pos)

           
        if(second_max == c3):
            for item in range(len(assigned_clusters)) : 
                if (assigned_clusters[item] == 4):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 0):
                    print(new[item],file=op_neg)
                    
                if (assigned_clusters[item] == 1):       
                    print(new[item],file=op_neg)

                if (assigned_clusters[item] == 3):
                    print(new[item],file=op_pos)

                if (assigned_clusters[item] == 2):
                    print(new[item],file=op_neg)
            
            


def main():
    k_means_cluster()

main()
