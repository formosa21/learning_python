'''
simple plot using pyplot
'''


import matplotlib.pyplot as plt

#import the entire pyplot module from the matplotlib
#to use it, we have to use the syntax: matplotlib.pyplot.something
#where "something" is the class or function we want to use
#---------useful, when using a couple functions from that module



def create_graph():
	x_numbers = [1,2,3]
	y_numbers = [2,4,6]
	
	plt.plot(x_numbers, y_numbers)
	plt.show()
	
if __name__ == '__main__':
	create_graph()
