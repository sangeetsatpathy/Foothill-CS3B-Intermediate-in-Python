#Sangeet Satpathy
#CS 3B
#Lab 8
#5/29/22
#Challenge 1
import numpy as np

def rotate_array(array, k):
	translated_array = [i for i in array]
	for i in range(array.size):
		if i+k > array.size-1:
			distance_last_index = (array.size-1)-i
			remaining_distance = k-distance_last_index-1
			array[0+remaining_distance] = translated_array[i]
		else:
			array[i+k] = translated_array[i]

nums = np.array([1,2,3,4,5,6,7])
k = 3
rotate_array(nums, 3)
print(nums)