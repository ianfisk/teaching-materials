def getUserInput():
	x = int(input("point x coordinate: "))
	y = int(input("y coordinate: "))
	return [x, y]



def getDistance(x1, y1, x2, y2):
	change_x = x2 - x1
	change_y = y2 - y1
	distance = ((change_x)**2 + (change_y)**2)**0.5
	return distance

def findMidpoint(x1, y1, x2, y2):
	xmid = (x1 + x2) / 2
	if xmid % 1 > 0:
		xmid = xmid
	elif xmid % 1 == 0:
		xmid = int(xmid)

	ymid = (y1 + y2) // 2
	return (xmid, ymid)


# Main program
pointNumbers = ['first', 'second']
for i in range(3):
	number = pointNumbers[i]
	print("Enter data for", number)
	if number == 'first':
		point1list = getUserInput()
		x1 = point1list[0]
		y1 = point1list[1]
	elif number == 'second':
		point2list = getUserInput()
		x2 = point2list[0]
		y2 = point2list[1]
	print()

# execute functions and print results
print("The straight line distance between these points is {0:0.3f}".format(getDistance(x1, y1, x2, y2)))
print("The midpoint of these points is", findMidpoint(x1, y1, x2, y2))
