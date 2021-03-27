import matplotlib.pyplot as plt 

timeInFlight = [0,1,2,3,4,5,6,7,8,9] 

cal_consumed = [1045728.6293925, 1080586.25037225, 1045728.6293925, 1080586.25037225, 1115443.871352, 976013.3874329999, 1080586.25037225, 1045728.6293925, 1080586.25037225, 1045728.6293925] 

summ = 0
production_list = [7730,7730,7730,7730,7730,7730,7730,7730,7730,7730,7730]
sumList = []
for i in range(len(timeInFlight)):       
  summ = sum(production_list[:i])-sum(cal_consumed[:i])
  sumList.append(summ)

print(sumList)
plt.plot(timeInFlight, sumList) 
plt.xlabel('Months after take off') 
plt.ylabel('Calories Left 1,000,000 kcal/month') 
plt.title('Calories Left for the crew per Month') 
plt.show()
