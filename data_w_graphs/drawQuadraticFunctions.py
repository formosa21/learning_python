'''
Quadratic funtion drawer
'''

from matplotlib import pyplot as plt


def set_x_range(initial, end, increment):
	x = []
	while initial < end:
		x.append(initial)
		initial += increment
	return x

def graph_qf(a, b, c, range_of_x):
	y = []
	for x in range_of_x:
		y.append(a*(x**2) + b*x + c)
	plt.plot(range_of_x, y)
	plt.xlabel('x value')
	plt.ylabel('y value')
	plt.title('Quadractic function drawer')

	plt.show()

if __name__ == '__main__':
	
	init = float(input('Enter the initial x value: '))
	end = float(input('Enter the end x value (that will be excluded): '))
	interval = float(input('What\'s the increment?: '))
	x = set_x_range(init, end, interval)
	
	a = float(input('Enter a: '))
	b = float(input('Enter b: '))
	c = float(input('Enter c: '))
	graph_qf(a, b, c, x)

	


	
