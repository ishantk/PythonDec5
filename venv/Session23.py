"""

    K-Means Clustering

    Data Set
    X       Y       P
    ------------------
    1       1       A
    1       0       B
    0       2       C
    2       4       D
    3       5       E
    -----------------

    Step1 Draw Points on Graph

    Step2 Take any 2 Random Points
    eg : A and C

    Consider Point A and Point C is Centroid of 2 Clusters
    C1 -> 1, 1 (A)
    C2 -> 0, 2 (B)

    Step3
    Calculate Distance between points from C1 and C2
    Eucildean Distance -> sqrt (  sq(y2-y1) + sq(x2-x1) )

    P   Dist from C1        Dist from C2

    A   0                   1.4
    B   1                   2.2
    C   1.4                 0
    D   3.2                 2.8
    E   4.5                 4.2

    Observation:
    A and B have less distance from C1
    C, D and E have less distance from C2

    Re-Draw Graph with the points A and B in one Cluster, C, D and E in other Cluster

    Step4
    Calculate Mean of Cluster1 and Cluster 2
    x1 + x2 +.. +xn/n, y1 +y2 +.. yn/n

    Cluster1 Mean : 1, .5
    Cluster2 Mean : 1.7, 3.7

    Step5
    Lets Recalculate New Distance from new Mean

    Eucildean Distance -> sqrt (  sq(y2-y1) + sq(x2-x1) )

    Data Set
    X       Y       P
    ------------------
    1       1       A
    1       0       B
    0       2       C
    2       4       D
    3       5       E
    -----------------

    NC1 : 1, .5
    NC2 : 1.7, 3.7

    P   Dist from NC1        Dist from NC2

    A   .5                  2.7
    B   .5                  3.7
    C   1.8                 2.4
    D   3.6                 0.5
    E   4.9                 1.9

    Observation:
    A, B and C have less distance from NC1
    D and E have less distance from NC2


    Will Re-Repeat the same steps again
    NNC1 Mean
    NNC2 Mean

    Solve the algo in Python

"""