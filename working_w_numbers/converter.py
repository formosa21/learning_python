'''
Unit converter: miles and km
'''

def print_menu():
	print('1.km to miles')
	print('2.miles to km')
	print('3.Farenheit to Celcius')
	print('4.Celcius to Farenheit')
	print('5.Kg to pound')
	print('6.pound to Kg')
	
def km_miles():
	km = float(input('enter distance in km'))
	miles = km / 1.609
	
	print('Distance in miles: {0}'.format(miles))

def miles_km():
	miles = float(input('enter distance in miles'))
	km = miles * 1.609

	print('Distance in km: {0}'.format(km))
	
def F_to_C():
	f = float(input('enter F drgree: '))
	c = ((f-32) * 5) / 9
	
	print('{0} Farenheit is {1} Celcius'.format(f, c))

def C_to_F():	
	c = float(input('enter C drgree: '))
	f = (9*c)/5 + 32
	
	print('{0} Celcius is {1} Farenheit'.format(c, f))
	
	
if __name__ == '__main__':

	print_menu()
	choice = input('Which conversion would you like to do?: ')
	choice = int(choice)
	if choice == 1:
		km_miles()
	
	if choice == 2:
		miles_km()
		
	if choice == 3:
		F_to_C()
		
	if choice == 4:
		C_to_F()
		
		
		
			

