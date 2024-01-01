# Reconstruction algorithms & phylogenetic trees
 
Phylogenetic trees are biological diagrams that show evolutionary relationships among several species or groups of organisms. By illustrating the branching patterns of their interactions, they illustrate the evolutionary history and the shared ancestry of all species. There exist two categories of trees:
- Those with a root: signifying the initial ancestor.
- Those without a root: where the oldest ancestor is unidentified. Here, a node is selected to serve as the root based on available information, or a new node is generated.
  
Within this structure:
- A node represents the most recent common ancestor.
- A leaf denotes an existing organism.
- The edges, or links, can be associated weights. These weights signify:
       - The count of mutations.
       - An estimation of the time taken for evolution.

Distance-Based Methods: 
A distance matrix M is said to be a metric if and only if :
* it is not negtive  $M_{ij} ≥ 0 $, for all  $i, j$
* it is symmetric: $M_{ij} = M_{ji}$ and M_{ii} = 0, for all $i, j$
* it satisfies the triangle inequality: $M_{ij}$ + $M_{jk} ≥ M_{ik}$, for all $i, j, k$

A distance matrix M can be additive ultrametric


UPGMA (Unweighted Pair Group Method with Arithmetic Mean)

Resources: 
* [Algorithms in Bioinformatics: Lecture 15-16: Phylogeny Reconstruction by Lucia Moura](https://www.site.uottawa.ca/~lucia/courses/5126-11/lecturenotes/16-17PhylogenyReconstruction.pdf)
* [Algorithmes de reconstruction des arbres phylogénétiques by Alessandra Carbone](https://www.ihes.fr/~carbone/L4_AAGB_Arbres_Phylogenetiques.pdf)

