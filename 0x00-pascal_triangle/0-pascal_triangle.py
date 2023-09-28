#!/usr/python3

def pascal_triangle(n):
	num_list = []
	if n <= 0:
		return num_list
	
	result = [1]
	num_list.append(result)
	for i in range(1, n):
		temp = [0] + result + [0]
		result = []
		for j in range(len(temp) - 1):
			result.append(temp[j] + temp[j + 1])
		num_list.append(result)

	return num_list
