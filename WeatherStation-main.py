import csvDataGather as csv
import sqlDataHandler as sql
import weatherPredictor as wp
import arimaTrainer as at
import averager as avg

season = 23
progress_indicator = 0
i = 0

prediction, paiva, kello, lampo, kosteus, paine = [], [], [], [], [], []
data = [kosteus, lampo, paine, paiva]
avgData = [[],[],[]]

while True:
	print('Starting')
	if progress_indicator == 0:		
		sql.DataRetreiver(data)
		avg.Averaging(data, avgData)
		dt_g_indicator = 1
	if progress_indicator!=2:
		#for i in range(2, 3):
		#	avgData[i] = at.modelTraining(avgData[i], season, i)
		for i in range(1, 3):
			wp.Prediction(avgData[i], season, prediction, i, data[3])
		progress_indicator=2

