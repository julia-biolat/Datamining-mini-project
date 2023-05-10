# Datamining-mini-project
#assignment 2
Purpose
Understanding of partition-based clustering algorithms
Practice of applying clustering techniques to high-dimensional data

Description
A time-series gene expression data set is provided to discover gene sets with co-expression patterns (similar expressions during a given time range). The co-expressed genes are likely to have the same cellular functions. Implement k-Means with k=10 to find 10 clusters of genes. Use Euclidean distance to measure distance between data objects. Your python code should take an input file name as a command-line argument, and return an output file named "assignment2_output.txt". The output file should have the gene IDs of each cluster at each line (space-delimited) starting with the size of the cluster. For example, "6: 0 24 56 139 285 471" where '6' is the cluster size and "0 24 56 139 285 471" are the six gene IDs in the cluster.

Data Set
Time-series gene expression data are given with 12 different time-points for 500 genes in a tab-delimited text file. Each row has time-series expression values for each gene (i.e., each row represents each gene). Each column has the expression values for each time point (i.e., each column represents the time point). Use the row number starting from 0 as a gene ID.

Submission
Submit your Python code, named "assignment2.py", and the output file via LearnUs.

Note
The algorithm of k-Means should be implemented. Just calling the library function of k-Means in a module is NOT allowed.
Euclidean distance measurement should be implemented. Just calling the library function of Euclidean distance is NOT allowed.
Round the Euclidean distance and the mean points to 3 decimal places.
Put your name as a comment at the first line of your code.

#assignment 3

Purpose
Understanding of the improved partition-based clustering algorithms such as k-medoids
Practice of applying clustering techniques to high-dimensional data

Description
A time-series gene expression data set is provided to discover gene sets with co-expression patterns (similar expressions during a given time range). The co-expressed genes are likely to have the same cellular functions. Implement improved k-Medoids (described below) with k=10 to find 10 clusters of genes. Use Euclidean distance to measure distance between data objects. Your python code should take an input file name as a command-line argument, and return an output file named "assignment3_output.txt". In an output file, show the gene IDs of each cluster at each line (space-delimited) starting with the size of the cluster. For example, "6: 0 24 56 139 285 471" where '6' is the cluster size and "0 24 56 139 285 471" are the six gene IDs in the cluster. Print the elapsed time of your python script in microseconds to the screen.

Improved k-Medoids Algorithm
Select initial medoids:
Calculate the distance between every pair of objects.
Calculate the sum of distance for each object.
Select k objects having the smallest sum of distance as initial medoids.
Obtain the initial clusters by assigning each non-medoid to the nearest medoid.
Update medoids iteratively:
For each cluster, calculate the sum of distance within the cluster for each object and select a new medoid having the smallest sum of distance.
Obtain the updated clusters by assigning each non-medoid to the nearest medoid.
Repeat steps 2-1 and 2-2 until the clusters do not change.

Data Set
Time-series gene expression data are given with 12 different time-points for 500 genes in a tab-delimited text file. Each row has time-series expression values for each gene (i.e., each row represents each gene). Each column has the expression values for each time point (i.e., each column represents the time point). Use the row number starting from 0 as a gene ID.

Submission
Submit your Python code, named "assignment3.py", and the output file via LearnUs.
Note
Round the Euclidean distance and the mean points to 3 decimal places.
Put your name as a comment at the first line of your code.

#assignment 4
Purpose
Understanding of hierarchical clustering methods
Practice of applying clustering techniques to high-dimensional data

Description
A time-series gene expression data set is provided to discover gene sets with co-expression patterns (similar expressions during a given time range). The co-expressed genes are likely to have the same cellular functions. Implement Agglomerative Hierachical Clustering (a bottom-up hierarchical algorithm described below) with the maximum distance threshold of 5. Make single link distance and complete link distance functions to measure distance between clusters. Use Euclidean distance to measure distance between data objects. Your python code should take an input file name as a command-line argument, and return two output files, named "assignment4_output1.txt" for clustering results with single link distance and "assignment4_output2.txt" for clustering results with complete link distance. In each output file, show the gene IDs of each cluster at each line (space-delimited) starting with the size of the cluster. For example, "6: 0 24 56 139 285 471" where '6' is the cluster size and "0 24 56 139 285 471" are the six gene IDs in the cluster. Print the elapsed time of your python script in microseconds to the screen.

Agglomerative Hierarchical Clustering
Create initial clusters:
Make each cluster contain only one object.
Merge clusters iteratively:
Calculate the distance between each cluster pair.
Merge the closest clusters.
Repeat steps 2-1 and 2-2 while the distance between the closest clusters is smaller than 5.

Data Set
Time-series gene expression data are given with 12 different time-points for 500 genes in a tab-delimited text file. Each row has time-series expression values for each gene (i.e., each row represents each gene). Each column has the expression values for each time point (i.e., each column represents the time point). Use the row number starting from 0 as a gene ID.

Submission
Submit your Python code, named "assignment4.py", and two output files via LearnUs.
Note
Just calling the library function of Agglomerative Hierarchical Clustering in a module is NOT allowed.
Just calling the library function of Euclidean distance, single link distance, or complete link distance in a module is NOT allowed.
Round the Euclidean distance and the mean points to 3 decimal places.
Put your name as a comment at the first line of your code.


#assignment EC

Purpose
Understanding of cluster validation methods

Description
Cluster validation is the process of assessing quality of clustering results. Clustering results are validated to compare the performance of clustering algorithms. Implement the cluster validation method using incident matrices. Take four clustering results of k-Means (Assignment-2), improved k_Medoids (Assignment-3), and agglomerative clustering with single link distance and complete link distance (Assignment-4) as input. Compute the clustering accuracy using the Jaccard index of the entry values between two incident matrices. Print the accuracy of four clustering results to an output file.

Data Set
Time-series gene expression data are given with 12 different time-points for 517 genes in a tab-delimited text file. Each row has time-series expression values for each gene (i.e., each row represents each gene). The first column has ground-truth cluster IDs. ("-1" means the gene is an outlier.) The expression value on each time-point comes from the second column.

Submission
Submit your Python code and the output file via LearnUs.

Note
If at least one gene of a gene pair is an outlier in the ground-truth clusters, then the entry for this gene pair in the incident matrix must be 0.


#assignment 5

Purpose
Understanding of density-based graph clustering algorithms
Practice of applying graph clustering techniques to large-scale graph data

Description
Genetic interaction data are provided to discover gene sets densely connected each other. The densely connected genes are likely to have the same cellular functions. Implement the maximal clique algorithm using the anti-monotonic property for density-based graph clustering. Your python code should take an input file name as a command-line argument, and return an output file ("assignment5_output.txt") which has the cliques of size-8 or greater. In an output file, show each cluster at each line in the format of the size and gene names in the cluster, for example, "4: YBR160W YDR224C YPL231W YBR081C".

Maximal Clique Search using Antimonotonic Property
Create initial clusters:
Find all cliques of size-2.
Increase k, size of cliques, iteratively:
Apply selective joining.
Find all cliques of size-k.
Repeat steps 2-1 and 2-2 until no more cliques are made.

Data Set
Gene-gene interaction data are given in a tab-delimited text file. Each row represents an interaction (edge) between two genes (vertices).

Submission
Submit your Python code, "assignment5.py", and the output file via LearnUs.

Note
Just calling the library function of Maximal Cliques in a module is NOT allowed.
The algorithm in your code must follow the anti-monotonic property.
Put your name as a comment at the first line of your code.


#assignment 6

Purpose
Understanding of hierarchical graph clustering algorithms
Practice of applying graph clustering techniques to large-scale graph data

Description
Genetic interaction data are provided to discover gene sets densely connected each other. The densely connected genes are likely to have the same cellular functions. Implement the top-down hierarchical graph clustering algorithm by least common neighbors using a density threshold of 0.4. Your python code should take an input file name as a command-line argument, and return an output file ("assignment6_output.txt") including the gene clusters of size-10 or greater. In an output file, show each cluster at each line in the format of the size and gene names in the cluster, for example, "4: YBR160W YDR224C YPL231W YBR081C". Print the clusters in a decreasing order of their size.

Top-Down Hierarchical Graph Clustering Based on Common Neighbors
Repeatedly remove an edge whose two ending vertices have the smallest Jaccard index of the sets of their neighbors until the graph is disconnected.
If the graph is disconnected into two sub-graphs:
If each sub-graph meets the density threshold, output the sub-graph as a cluster.
Otherwise, apply steps 1 and 2 to the sub-graph recursively until all vertices are returned as cluster members.

Data Set
Gene-gene interaction data are given in a tab-delimited text file. Each row represents an interaction (edge) between two genes (vertices).

Submission
Submit your Python code, "assignment6.py", and the output file via LearnUs.

Note
Because the provided input graph is disconnected, measure the density of each connected sub-graph, and output the sub-graph as a cluster if it meets the density threshold.
If two or more edges have the same value of the smallest Jaccard index, (1) select the vertex pairs having such edges, (2) sort two vertices in each pair in an alphabetic order of their gene names, (3) sort the vertex pairs in an alphabetic order of the first occurring gene names, and (4) remove the edges in the sorted order.
Put your name as a comment at the first line of your code.
