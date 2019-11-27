def Averaging(data, avgData):
	temp = []
	j=0

	for i in range(0, 3):
		for r in range(0, len(data[i])):
			temp.append(data[i][r])
			if j == 24:
				avg = sum(temp)/24
				avgData[i].append(avg)
				temp = []
				j=0
			j = j+1
	return avgData
