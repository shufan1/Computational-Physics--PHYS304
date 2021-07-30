import numpy as np

# define matrix
A = np.array([[4,-1,-1,-1],
				[-1,3,0,-1],
				[-1,-1,-1,4],
				[-1,0,3,-1]], float)

# vecotr on the right hand side of B
B = np.array([[5],
				[0],
				[0],
				[5]], float)
#Solve Av = B
V = np.linalg.solve(A,B)

print("[I1,I2,I3] is: ",V)
# print(np.dot(A,V))