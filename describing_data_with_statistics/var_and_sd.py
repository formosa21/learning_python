'''
find the variance and the standard deviation
of a list of numbers
'''

def calculate_mean(numbers):
	s = sum(numbers)
	N = len(numbers)
	mean = s/N
	return mean

def find_differences(numbers):
	mean = calculate_mean(numbers)
	diff = []
	for num in numbers:
		diff.append(num - mean)
	return diff

def calculate_variance(numbers):
	# find the list of differences
	diff = find_differences(numbers)
	# find the squared differences
	squared_diff = []
	for d in diff:
		squared_diff.append(d**2)
	# find the variance
	variance = sum(squared_diff)/len(numbers)
	return variance

if __name__ == '__main__':
	
	donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
	variance = calculate_variance(donations)
	print('The variance of the donations is {0}'.format(variance))

	std = variance**0.5
	print('The standard deviation of the donation is {0}'.format(std))
