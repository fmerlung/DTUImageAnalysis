# %%
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import decomposition

def cov(a, b):
    if (len(a) != len(b)):
        return -1

    sum = 0
    mean_a = np.mean(a)
    mean_b = np.mean(b)
    for i in range(len(a) - 1):
        sum += (a[i] - mean_a) * (b[i] - mean_b)

    return  1/(len(a) - 1) * sum  

# %%
# exercise 1
in_dir = "data\\"
txt_name = "irisdata.txt"
iris_data = np.loadtxt(in_dir + txt_name, comments="%")
# x is a matrix with 50 rows and 4 columns
x = iris_data[:50, :4]

n_feat = x.shape[1]
n_obs = x.shape[0]
print(f"Number of features: {n_feat} and number of observations: {n_obs}")

# exercise 2
sep_l = x[:, 0]
sep_w = x[:, 1]
pet_l = x[:, 2]
pet_w = x[:, 3]

# Use ddof = 1 to make an unbiased estimate
var_sep_l = sep_l.var(ddof=1)
var_sep_w = sep_w.var(ddof=1)
var_pet_l = pet_l.var(ddof=1)
var_pet_w = pet_w.var(ddof=1)

# print("sepal width variance: " + str(var_sep_w))
# print("sepal length variance: " + str(var_sep_l))
# print("petal width variance: " + str(var_pet_w))
# print("petal length variance: " + str(var_pet_l))

# exercise 3
# print(f"covariance of sep_l and sep_w: {cov(sep_l, sep_w)}")
# print(f"covariance of sep_l and pet_l: {cov(sep_l, pet_l)}")



# exercise 4
# Transform the data into a Pandas dataframe
d = pd.DataFrame(x, columns=['Sepal length', 'Sepal width',
 							  'Petal length', 'Petal width'])
# sns.pairplot(d)
# plt.show()

# exercise 5
mn = np.mean(x, axis=0)
data = x - mn
c_x = np.cov(x, ddof=1, rowvar=False)
labels = ['sepal length', 'sepal width', 'petal length', 'petal width']
# sns.heatmap(c_x, annot=True, fmt='g', xticklabels=labels, yticklabels=labels, cmap='jet')

# exercise 6
values, vectors = np.linalg.eig(c_x)

# exerise s7
# v_norm = values / values.sum() * 100
# plt.xlabel('Principal component')
# plt.ylabel('Percent explained variance')
# plt.ylim([0, 100])
# plt.plot(v_norm)
# plt.show()

pc_proj = vectors.T.dot(data.T)
plt.plot(pc_proj)
plt.show()

pca = decomposition.PCA()
pca.fit(d)
values_pca = pca.explained_variance_
exp_var_ratio = pca.explained_variance_ratio_
vectors_pca = pca.components_

data_transform = pca.transform(d)
pca_result = pd.DataFrame(data_transform, columns=['Sepal length', 'Sepal width',
 							  'Petal length', 'Petal width'])
sns.pairplot(pca_result)
# %%
