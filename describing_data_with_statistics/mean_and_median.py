
def calculate_mean(numbers):
	s = sum(numbers)
	N = len(numbers)
	mean = s/N
	return mean

def calculate_median(numbers):
	N = len(numbers)
	numbers.sort()

	# find the median
	if N%2 == 0:
		# if N is even
		m1 = N/2
		m2 = (N/2) + 1
		# convert to integer, match position
		m1 = int(m1) - 1
		m2 = int(m2) - 1
		median = (numbers[m1] + numbers[m2])/2
	else:
		m = (N+1)/2
		# Convert to integer, match position
		m = int(m) - 1
		median = numbers[m]

	return median 

if __name__ == '__main__':


	num = int(input('Enter the number you want in an array: '))
	arr = []
	for value in range(num):
		arr.append(input('Enter the position {0}\'value in an array: '.format(value)))
	arr = [int(i) for i in arr]
	mean = calculate_mean(arr)
	median = calculate_median(arr)	
	print('mean: {0}'.format(mean))
	print('median: {0}'.format(median))
