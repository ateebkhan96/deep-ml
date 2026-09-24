import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:


	npmatrix = np.array(matrix)

	result = []

	if mode == 'column':

		for i in range(npmatrix.shape[1]):

			result.append(np.mean(npmatrix[:, i]))

	else:

		for i in range(npmatrix.shape[0]):

			result.append(np.mean(npmatrix[i]))


	return result