from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
# print("**************")
# print(iris)
# print("**************")

"""
print("**************")
# 2-D
print(iris.data)
print("**************")
print()
print("**************")
# 1-D
print(iris.target)
print("**************")
"""

# Create an Object of DecisionTreeClassifier API
clf = tree.DecisionTreeClassifier()
clf.fit(iris.data, iris.target)

flowerToBePredicted = [[5.9, 3.0, 5.1, 1.8]]
flower = clf.predict(flowerToBePredicted)

print(flower)

flowers = ["Setosa", "Versicolor", "Virginica"]

# if flower == 0:
#     print("Setosa")
# elif flower == 1:
#     print("Versicolor")
# elif flower == 2:
#     print("Virginica")

print(flowers[flower[0]])

import graphviz
# data = tree.export_graphviz(clf, out_file=None)
data = tree.export_graphviz(clf,
                            out_file=None,
                            feature_names=iris.feature_names,
                            class_names=iris.target_names,
                            filled=True,
                            rounded=True,
                            special_characters=True)
graph = graphviz.Source(data)
graph.render("IRIS TREE")
graph.view()