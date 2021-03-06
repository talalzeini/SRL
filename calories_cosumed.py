import matplotlib.pyplot as plt

timeInFlight = [0, 1, 2, 3, 4, 5, 6]

cal_consumed = [1045728.6293925, 1080586.25037225, 1045728.6293925, 1080586.25037225, 1115443.871352, 976013.3874329999,
                1080586.25037225]
carbs = []
proteins = []
fat = []
fatty_acids = []
for i in range(len(cal_consumed)):
    calories_for_month = sum(cal_consumed[:i])
    carbs.append((0.45 * calories_for_month))
    proteins.append((0.35 * calories_for_month))
    fat.append((0.20 * calories_for_month))

print(calories_for_month)
print(carbs)
print(proteins)
print(fat)
print()

print(carbs[-1] / 4000)
print(proteins[-1] / 4000)
print(fat[-1] / 9000)

print(sum([(carbs[-1] / 4000), (proteins[-1] / 4000), (fat[-1] / 9000)]))

plt.xlabel('Months after take off')
plt.ylabel('Kilocalories Consumed (1,000,000 Kcal)')
plt.title('Kilocalories Consumed by the Crew')
pal = ["#15ab00", "#ff1100", "#ff6600"]
plt.stackplot(timeInFlight, carbs, proteins, fat, labels=['Carbs', 'Proteins', 'Fat'], colors=pal)
plt.legend(loc='upper left')
plt.show()
