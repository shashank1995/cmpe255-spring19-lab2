def mean_num_friends(x):
	total = 0
	for a in x:
		total = total + a
	mean = total / len(x)
	return mean

def median_num_friends(x):
	x.sort()
	if len(x)%2 == 0:
		median = (x[len(x)/2] + x[(len(x)/2)-1])/2
	else:
		median = x[int(len(x)/2)]
	return median

num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print("mean={}".format(mean_num_friends(num_friends)))
print("median={}".format(median_num_friends(num_friends)))


