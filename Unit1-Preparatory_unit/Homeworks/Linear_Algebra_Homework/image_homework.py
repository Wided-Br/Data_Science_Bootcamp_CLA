import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from numpy.linalg import norm

def isDiag(M):
    i, j, k = np.nonzero(M)
    return np.all(i == j)

def isTrgL(M):
    return np.allclose(M, np.tril(M))

def isTrgU(M):
    return np.allclose(M, np.triu(M))


img = mpimg.imread("bird.jpg")
#plt.imshow(img)
#plt.show()
img_transpose = img.T

print("The matrix is diagonal:", isDiag(img))
print("The matrix is lower-triangular:", isTrgL(img))
print("The matrix is upper-triangular:", isTrgU(img))

vec = img[0][1]
print("The chosen row is: \n",vec)
l1 = norm(vec, 1)
print("The first norm =",l1)
l2 = norm(vec)
print("The second norm =",l2)
