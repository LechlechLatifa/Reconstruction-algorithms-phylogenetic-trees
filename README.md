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


Phylogeny reconstruction refers to inferring the evolutionary relationships among different species or groups. Numerous methodologies are employed within this field, delineated by their categorization based on input data types:
* Character based methods take as input a character state matrix.
  * Maximum Parsimony (Fitch algorithm, Sankoff algorithm)
  * Maximum Likelihood
  * Bayesian Inference
* Distance based methods take as input a distance matrix, this is determined by calculating the evolutionary distance or dissimilarity between the taxa.
  * Unweighted Pair Group Method with Arithmetic Mean (UPGMA), clustering
  * Neighbor Joining (NJ)

  A distance matrix M is said to be a metric if and only if :
  * it is not negtive  $M_{ij} ≥ 0 $, for all  $i, j$
  * it is symmetric: $M_{ij} = M_{ji}$ and $M_{ii} = 0$, for all $i, j$
  * it satisfies the triangle inequality: $M_{ij}$ + $M_{jk} ≥ M_{ik}$, for all $i, j, k$

  Although they both serve as matrices for representing distances or differences between objects, additive and ultrametric matrices have different underlying structures and properties:
  * In an additive matrix, the distances between objects obey the triangle inequality, which means that the direct distance between two objects is less than or equal to the sum of their distances through a third object. Based on Buneman’s 4-point condition Theorem:  M is additive if and only if the 4-point condition is satisfied. It doesn't necessarily imply a hierarchical structure.
  * On the other hand, an ultrametric matrix satisfies a stronger condition known as ultrametricity. matrices often represent hierarchical relationships among entities. Based on 3-point condition Theorem: M is ultrametric if and only if the 3-point condition is satisfied.
 
 
## Unweighted Pair Group Method with Arithmetic Mean (UPGMA)
UPGMA is a clustring algorithm, join twi point into on cluster if they are near to each others.
* Unweighted : all pairwise distances contribute equally
* Pair Group : groups are combined in pairs (dichotomies only)
* Arithmetic Mean : pairwise distances to each group (clade) are mean distances to all members of that group

Steps: 
1. Align & name
2. **Mismatche matrix** compare sequences using pairwise sequence alignment and count the mismatches and records them in the mismatche matrix
3. **Find the Closest Pair** $(i,j)$ with the smallest distance $d_{ij}$ and create a new cluster u that joins clusters $i$ and $j$.
   *  Define the height (i.e. distance from leaves) of $u$ to be $l_{ij} := \frac{d_{ij}}{2}$
   * The distance between two clusters $C_{i}$ and $C_{j}$ is calculated as following:
   $$d_{ij}= \frac{1}{|C_{i}|.|C_{j}|} \sum_{p \in C_{i}, q \in C_{j}} d_{pq}$$
  
4. **Update the Matrix** To represent the newly created cluster, replace the rows and columns that correspond to the two clustered items with a new row and column. Based on the average distance from the newly created cluster, the distances to the other objects in the matrix are computed.
5. **Repeat** step 3 and 4 until one cluster is reached.

The complexity of UPGMA is $O(n^{2})$: there are n-1 iterations, with $O(n)$ operations performed in each.

## Neighbor Joining (NJ)
The Neighbor-Joining (NJ) algorithm (Saitou and Nei, 1987) is a polynomial-time phylogenetic tree construction method. It is agglomerative, so it constructs ancestral relationships between taxa by clustering the most closely related taxa at each step until a complete phylogeny is formed.[[2]](https://www.frontiersin.org/articles/10.3389/fgene.2020.584785/full#:~:text=The%20Neighbor%2DJoining%20(NJ),a%20complete%20phylogeny%20is%20formed.)

Steps:
1. **Mismatche matrix** start with a matrix of pairwise distances between all taxa.
2. **Compute $r^{'}_{i}$**for each terminal node using the following formula: $$ r^{'}_{i} = \frac{\sum d_{ij}{n-2} $$ where n is the number of texa.
3. **Compute D' matrix** for each terminal node by applying the formula that follows: $$d^{'}_{ij} = d_{ij} -r^{'}_{i} -r^{'}_{j}  $$
4. **Find the Closest Pair** $(i,j)$ with the smallest distance $d_{ij}$
5. **Calculate branch length** $$v_{i} = 0.5 \times $d_{ij}$ + 0.5 \times (r^{'}_{i} -r^{'}_{j}) $$ $$v_{j} = 0.5 \times $d_{ij}$ + 0.5 \times (r^{'}_{j}-r^{'}_{i}) $$
6. **Upadate the distance matrix** Create a new row and column and replace the ones that match the two grouped items. The distance between the new cluster and the others terminal node is calculated as follow:
   $$d_{ij,k} = \frac{d_{ik}+d_{jk}-d_{ij}}{2}$$
7. **Repeat** the steps from step 2 until one cluster is reached.


The complexity of Neighbor Joining (NJ) algorithm is  $O(n^{3})$, where n is the number of sequences or taxa

Resources: 
* [Algorithms in Bioinformatics: Lecture 15-16: Phylogeny Reconstruction by Lucia Moura](https://www.site.uottawa.ca/~lucia/courses/5126-11/lecturenotes/16-17PhylogenyReconstruction.pdf)
* [Algorithmes de reconstruction des arbres phylogénétiques by Alessandra Carbone](https://www.ihes.fr/~carbone/L4_AAGB_Arbres_Phylogenetiques.pdf)
* [Molecular Phylogenetics (Hannes Luz)](https://www.molgen.mpg.de/3373145/evolution.pdf)
* [UPGMA Worked Example](http://www.slimsuite.unsw.edu.au/teaching/upgma/)

