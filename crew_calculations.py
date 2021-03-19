# Import astronaut crew data sheet and extract information
from typing import Optional

"""
Crew nutrition information and consumption
"""

days_per_month = {1: 32, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
initial_month = int(input("Enter the month, in number form where January is 1, when the mission is to start"))
number_crew = int(input("Enter the number of people on the mission to Mars: "))

# Dimensions will be taken in SI units
class Person:
    detail: Optional[str]

    def __int__(self, name, age, gender, education, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.education = education
        self.height = height
        self.weight = weight
        self.detail = ""

    # ERR Model
    def nutrition_requirement(self, level, month):
        if self.gender == 'M':
            PA = 1.25 if level == "high" else 1.11 if level == "low" else ValueError("Specify activity level")
            EER = 662 - (9.53 * self.age) + PA * (15.91 * self.weight + 539.6 * self.height)
        else:
            PA = 1.27 if level == "high" else 1.12 if level == "low" else ValueError("Specify activity level")
            EER = 354 - (6.91 * self.age) + PA * (9.36 * self.weight + 726 * self.height)
        return days_per_month[month + initial_month] * EER

    def BMI(self, comparison=False):
        BMIValue = (self.weight / pow(self.height, 2)) * 703
        if comparison:
            self.detail = "obese" if 30 >= BMIValue else "overweight" if BMIValue >= 25 else "normal weight" if BMIValue >= 18.5 else "underweight" if BMIValue < 18.5 else None
            return [BMIValue, self.detail]
        return [BMIValue]

"""
Cost for hiring crew
"""




crew_member_consumption_rates = []
consumption_rate = sum(crew_member_consumption_rates)