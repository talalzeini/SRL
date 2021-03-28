import matplotlib.pyplot as plt

       
timeInFlight = [0,1,2,3,4,5,6,7] 

cal_consumed = [1045728.6293925, 1080586.25037225, 1045728.6293925, 1080586.25037225, 1115443.871352, 976013.3874329999, 1080586.25037225, 1045728.6293925] 
carbs = [] 
proteins = []
fat = []
fatty_acids = []
for i in range(len(cal_consumed)):
  calories_for_month = sum(cal_consumed[:i])
  carbs.append( (45 * calories_for_month))
  proteins.append( (30 * calories_for_month))
  fat.append( (20 * calories_for_month))
  fatty_acids.append( (5 * calories_for_month))

plt.xlabel('Months after take off') 
plt.ylabel('Kilocalories Consumed 1,000,000 kcal/month') 
plt.title('Kilocalories Consumed by the crew') 
plt.stackplot(timeInFlight, fatty_acids, fat, proteins, carbs, labels=['Fatty Acids','Fat','Proteins', 'Carbs'])
plt.legend(loc='upper left')
plt.show()
