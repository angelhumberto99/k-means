import numpy as np
import matplotlib.pyplot as plt

X1 = np.random.rand(50,2)
X2 = np.random.rand(50,2) + 2
X3 = np.random.rand(50,2) - 2 

X = np.concatenate((X1, X2), axis=0)
X = np.concatenate((X, X3), axis=0)

plt.scatter(X[ : , 0], X[ :, 1], s = 50, c = "b")
plt.show()

print(X)
file = open("dataset.csv", 'w')
for i in X:
    file.write(str(i[0])+","+str(i[1])+"\n")
file.close()