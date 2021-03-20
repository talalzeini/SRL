"""
crew_calculations.py: Generates a plot of values that model the calorie intake of the crew.
"""

# Imports
from AstronautsDataAnalysis import degree_random, height_random, weight_random
from matplotlib.ticker import MaxNLocator, ScalarFormatter
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import random

# July 30 is the initial launch data according to wikipedia; https://en.wikipedia.org/wiki/Mars_2020
days_per_month = {1: 32, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
initial_month = 8

"""
The youngest astronaut to be in space was 32 years old and the average ages of an astronaut in 2013 was 36 years old;
therefore, we can add the difference of 36 and 32 to 36 and get our upper bound which in this case is 40. The randint
code will set a bounds of 32 to 39(controlling for older aged people).
"""


# Dimensions will be taken in SI units
class Person(object):

    def __init__(self, position_name):
        self.name = position_name
        self.age = random.randint(32, 40)
        self.sex = 'M' if (random.randint(0, 100) > 29) else 'F'
        self.education = degree_random(self.get_sex)
        self.height = height_random(self.get_sex)
        self.weight = weight_random(self.get_sex)
        self.detail = self.weight_detail

    # Get the sex of the crew member
    @property
    def get_sex(self):
        return self.sex

    # Get the age of the crew member
    @property
    def get_age(self):
        return self.age

    # Get the education subject of the crew member
    @property
    def get_education(self):
        return self.education

    # Get the height of the crew member(m)
    @property
    def get_height(self):
        return self.height

    # Get the weight of the crew member(kg)
    @property
    def get_weight(self):
        return self.weight

    # Get the BMI verbal estimate of the member
    @property
    def get_detail(self):
        return self.detail

    # ERR Model; Procures caloric requirement per month for each individual crew member
    def nutrition_requirement(self, level, month):
        if self.get_sex == 'M':
            PA = 1.25 if level == "high" else 1.11 if level == "low" else ValueError("Specify activity level")
            EER = 662 - (9.53 * self.get_age) + PA * (15.91 * self.get_weight + 539.6 * self.get_height)
        else:
            PA = 1.27 if level == "high" else 1.12 if level == "low" else ValueError("Specify activity level")
            EER = 354 - (6.91 * self.get_age) + PA * (9.36 * self.get_weight + 726 * self.get_height)
        return days_per_month[((month + initial_month) % 12) + 1] * EER

    # BMI function
    def BMI(self):
        return (self.get_weight / pow(self.get_height, 2.5)) * 1.3

    """
    # BMI comparison function
    @property
    def weight_detail(self):
        BMIValue = self.BMI()
        return "obese" if 30 >= BMIValue else "overweight" if BMIValue >= 25 else "normal weight" if BMIValue >= 18.5 \
            else "underweight" if BMIValue < 18.5 else None
    """


# Generate 12 crew member placeholders and use them to create class objects
crew_members = [Person(str(i)) for i in range(12)]

# Print out the randomized value descriptions for each crew member
[print(str(i.get_sex) + ", " + str(i.get_education) + ", " + str(i.get_height) + ", " + str(i.get_weight) + ", " + \
       str(i.get_detail)) for i in crew_members]

# Generate a plot and title
fig = plt.figure(figsize=(6.5, 6.5))
ax = fig.add_subplot(111)
ax.set_title("Crew Caloric Requirements per Month")

# Label axises
ax.set_xlabel("Months after take off")
ax.set_ylabel("Caloric In-take (1,000,000 kcal/month)")

# Set the length of the plot as well as the step
t = np.arange(0, 10, 1)

# Generate the y-values for each month and stores them
s_values = []
for num in range(len(t)):
    s_values.append(sum([v.nutrition_requirement("high", num) for v in crew_members]))

# Plots the x-values and y-values on a plot
ax.plot(t, s_values)

# Sets the range of the y-axis of the graph and sets it to only use integers
ax.set_ylim(0, 1_500_000)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

# Creates a grid patter on the plot
ax.grid(axis="x", color="green", alpha=.3, linewidth=2, linestyle=":")
ax.grid(axis="y", color="black", alpha=.5, linewidth=.5)

# Shows the plot
plt.show()

# Store the list of consumption rates per month so it can be used
# for nutrition.py program
Consumption_rate = s_values
