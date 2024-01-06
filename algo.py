import numpy as np
import pandas as pd
from io import StringIO
from Bio import Phylo

class phylogenetic_tree_reconstruction:

    def __init__(self) -> None:
        pass

    # Common functions
    ## pairwise_sequence_alignment
    def pairwise_sequence_alignment(self,seq_1,seq_2):
        count_missmatch = 0
        for i in range(len(seq_1)):
            if seq_1[i] != seq_2[i]:
                count_missmatch += 1
        return count_missmatch
    
    ## mismatche_matrix function 
    def  mismatche_matrix(self,seq_list):
        n = len(seq_list)
        mismatch_m = np.zeros((n,n))

        for i in range(n):
            sub_seq_list = seq_list[i+1:]
            for j in range(len(sub_seq_list)):
                matrix_j = j+i+1
                pairwise_seq = self.pairwise_sequence_alignment(seq_list[i],sub_seq_list[j])
                mismatch_m[i][matrix_j] = mismatch_m[matrix_j][i] = pairwise_seq

        return mismatch_m
    
    def mismatche_matrix_to_df(slef,mismatch_m,seq_names):
        return pd.DataFrame(data=mismatch_m, columns=seq_names ,index=seq_names)
    
    ## This function plot Dendrogram : tree in Hiarchical form 
    def plot_dendrogram(self,tree_newick_format):
        # Read the tree from the Newick format string
        tree = Phylo.read(StringIO(tree_newick_format), "newick")
        # Plot the tree
        Phylo.draw(tree)

    ## This function return Minimum value greater than 0 in a dataframe
    def min_val_index_df(slef,df): 
        # Finding the minimum value greater than 0
        min_val = df[df > 0].min().min()
        # Getting the indices of the minimum value
        indices = df[df == min_val].stack().index.tolist()

        return min_val, list(indices[-1])
    

    # UPGMA algorithm 
    ## Compute distance between clusters
    def cal_cluster_distance_upgma(self, df,df_copy,new_cluster_name):
        cluster_missmatch_socre = []
        for col in df_copy.columns:
            distance = 0
            # caclulate distance between 
            for sub_cluster in col:
                for pairs in new_cluster_name:
                    distance += df[sub_cluster][pairs]
            distance = distance / (len(col)*len(new_cluster_name))
            #print("Distance between",col,new_cluster_name,"is",distance)
            cluster_missmatch_socre.append(distance)
        return cluster_missmatch_socre
    
    ## construct_tree_upgma (umga algo starting from the mismatch matrix)
    def construct_tree_upgma(self,mismatch_m,seq_names):
        df = self.mismatche_matrix_to_df(mismatch_m,seq_names)
        dict_tree_newick_format = {} 
        df_copy = df.copy()
        while len(df_copy) > 1 :
            min_val, min_indices = self.min_val_index_df(df_copy)
            #print(min_val, min_indices )

            # Create new cluster  for pairs (i,j)
            ## intialize the new cluster name u 
            new_cluster_name = min_indices[0]+min_indices[1]
            ## calculate the distance between u_i and u_z
            cluster_branch_distance = min_val/2
            ## update the tree_newick_format 
            i = str(min_indices[0])
            j = min_indices[1]

            cluster_branch_distance_i = cluster_branch_distance_j = cluster_branch_distance

            
            if len(min_indices[0]) > 1:
                i = dict_tree_newick_format[min_indices[0]][1]
                cluster_branch_distance_i = cluster_branch_distance - dict_tree_newick_format[min_indices[0]][0]/2
            if len(min_indices[1]) > 1:
                j = dict_tree_newick_format[min_indices[1]][1]
                cluster_branch_distance_j = cluster_branch_distance - dict_tree_newick_format[min_indices[1]][0]/2

            tree_newick_format = "("+i+":"+str(cluster_branch_distance_i)+","+j+":"+str(cluster_branch_distance_j)+")"
            dict_tree_newick_format[new_cluster_name] = [min_val,tree_newick_format]
    
            df_copy.drop(min_indices, axis=1, inplace=True)
            df_copy.drop(min_indices, axis=0, inplace=True)

            ## Compute the distance between the new cluster and the others 
            cluster_missmatch_socre = self.cal_cluster_distance_upgma(df,df_copy,new_cluster_name)
            #print(cluster_missmatch_socre)

            # Upadte the mismatch matrix
            ## create new col with new cluster name and a new row 
            ### add col
            df_copy[new_cluster_name] = cluster_missmatch_socre
            ### add row 
            cluster_missmatch_socre.append(0)
            df_copy.loc[new_cluster_name] = cluster_missmatch_socre

        return list(dict_tree_newick_format.items())[-1][1][1]
    
    ## upgma algorithm
    def upgma(self,seq_names,seq_list=None,mismatch_m =None):
        if mismatch_m == None:
            mismatch_m = self.mismatche_matrix(seq_list)
        return self.construct_tree(mismatch_m,seq_names)
    

    # Neighbor Joining
    
