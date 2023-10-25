import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt
import Peca1_dados
import Peca2_dados
import Peca3_dados
import Peca4_dados

peca1_verts = Peca1_dados.peca1()
peca2_verts = Peca2_dados.peca2()
peca3_verts = Peca3_dados.peca3()
peca4_verts = Peca4_dados.peca4()
               
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

r = [-1,1]

####
X, Y = np.meshgrid(r, r)

ax.scatter3D(0,0,0)
ax.scatter3D(400,400,350)
ax.scatter3D(-400,400,350)

# plot sides
ax.add_collection3d(Poly3DCollection(peca1_verts, 
 facecolors='green', linewidths=1, edgecolors='k', alpha=.9))

ax.add_collection3d(Poly3DCollection(peca2_verts, 
 facecolors='yellow', linewidths=1, edgecolors='k', alpha=.9))

ax.add_collection3d(Poly3DCollection(peca3_verts, 
 facecolors='blue', linewidths=1, edgecolors='k', alpha=.9)) 

ax.add_collection3d(Poly3DCollection(peca4_verts, 
 facecolors='blue', linewidths=1, edgecolors='k', alpha=.5)) 


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


plt.show()

