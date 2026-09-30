def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	
	trace = matrix[0][0] + matrix[1][1]

	det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

	eigenvalue_1 = trace + (trace**2 - 4 * det)**0.5
	eigenvalue_2 = trace - (trace**2 - 4 * det)**0.5
	
	eigenvalues = [eigenvalue_1/2, eigenvalue_2/2]
	return eigenvalues