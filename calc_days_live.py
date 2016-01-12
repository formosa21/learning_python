
# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def is_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
	#total days (start at 0)
	days = 0
	#dates of month
	dom = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	dom_leap = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	
	if year1 == year2:
		if is_leap(year1):
			while month1 <= month2:
				days += dom_leap[month1-1]
				month1 +=1
			days -= (day1 + (dom_leap[month2-1] - day2))
		else:
			while month1 <= month2:
				days += dom[month1]
				month1 +=1
			days -= (day1 + (dom[month2-1] - day2))
	else: #year1 < year2
		###calc days first year	
		if is_leap(year1):
			while month1 <= 11:
				days += dom_leap[month1-1]
				month1 +=1
		else: #not leap year		
			while month1 <= 11:
				days += dom[month1-1]
				month1 +=1	
			
		year1+=1
		days -= day1
		
		###calc days in between 1st and last (exclusive)
		if year1 < year2:
			while year1 < year2:
				if is_leap(year1):
					days += 366
					year1 += 1
				else:
					days += 365
					year1 += 1
		###calc days last year
		if is_leap(year2):
			i = 0
			while i <= month2:
				days += dom_leap[i-1]
				i += 1
			days -= (dom_leap[month2-1] - day2)
		else:
			i = 0
			while i <= month2:
				days += dom[i-1]
				i += 1
			days -= (dom[month2-1] - day2)
	
	return days
	
print(daysBetweenDates(1986,2,27,2016,1,12))


# Test routine
"""
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
"""
