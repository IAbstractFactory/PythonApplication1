

def BubbleSort(array):
    
	for i in range(len(array)):
		for j in range(len(array) - i - 1):
			if array[j] < array[j + 1]:
				array[j],array[j + 1] = array[j + 1],array[j]
				
nums = [1,2,3,4,5,6,7,8]

	
print(nums)
BubbleSort(nums)
print(nums)
input()