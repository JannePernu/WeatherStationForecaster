import csv

def DataGather(kosteus, lampo, paine, kello, paiva, tempData):
	path = '/home/huginn/Downloads/'
	with open(path + 'DATA.csv', 'r', encoding = "ISO-8859-1") as f:
		reader = csv.reader(f, quoting=csv.QUOTE_ALL)
		for row in reader:
			paiva.append(str(row[0]) + '-' + str(row[1]) + 
						 '-' + str(row[2]))
			kello.append(row[3])
			try:
				paine.append(float(row[5]))
				kosteus.append(float(row[6]))
				lampo.append(float(row[7]))
			except:
				continue
			row_print = [lampo[-1], paine[-1], kosteus[-1]]
			tempData.append(row_print)
		return tempData
