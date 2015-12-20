'''
Fraction opeartions
'''

from fractions import Fraction

def add(a, b):
	print('Result of addition: {0}'.format(a+b))
	
def substract(a, b):
	print('Result of substraction: {0}'.format(a-b))
	
	
	

if __name__ == '__main__':
	
	a = Fraction(input('Enter the first fraction: '))
	b = Fraction(input('Enter the second fraction: '))
	op = input('Opeartion to perform - add, substract, divide, multiply: ')
	
	
	if op == 'add':
		add(a, b)
	if op == 'substract':
		substract(a, b)
		
