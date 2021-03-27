"""
AstronautsDataAnalysis.py: Used to analyze and create probabilities for astronaut description for
                           use in later test cases.
"""

# Imports
from random import randint
import csv

"""
For the education level of the astronauts we are only going to consider their undergraduate because we don't need to
what they ended-up studying in particular, only their general knowledge. We'll only consider the astronauts that came
after 2000 to stay as close to current trends as possible.
"""

# List for counting sex-ratio of astronauts
s_lst = []

# List for degree percentages between men and women astronauts
me_lst = []
we_lst = []

# Degree categories list
category = ["Math", "Physics", "Engineering", "Chemistry", "Biology", "Other"]

# Sets comparison year(only after this year [up until 2009] will be considered)
year = 1995

# Opens up astronaut csv file that was imported from kaggle
with open("astronauts.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    skip = True
    for row in csv_reader:
        if skip:
            skip = False
            continue
        if row[1] == '':
            continue
        if int(row[1]) > year:
            # Stores astronaut sex
            s_lst.append(row[6])
            if row[6] == "Male":
                # Stores male education
                me_lst.append(row[8])
            else:
                # Stores female education
                we_lst.append(row[8])

# Counts the number of men and women astronauts after the given year
number_men = s_lst.count("Male")
number_women = s_lst.count("Female")

# Converts the count to overall percentage score
percentage_of_men = str(100 * (number_men / (number_men + number_women)))[:5]
percentage_of_women = str(100 * (number_women / (number_men + number_women)))[:5]

# Function to count the subjects that each sex studied and produce percentages
def degree(lst):
    total_degree_number = 0
    degree_dict = {
        "Math": 0,
        "Physics": 0,
        "Engineering": 0,
        "Chemistry": 0,
        "Biology": 0,
        "Other": 0
    }

    for edu in lst:
        if "Math" in edu:
            degree_dict["Math"] += 1
        elif "Physic" in edu:
            degree_dict["Physics"] += 1
        elif "Engineer" in edu:
            degree_dict["Engineering"] += 1
        elif "Chem" in edu:
            degree_dict["Chemistry"] += 1
        elif "Bio" in edu:
            degree_dict["Biology"] += 1
        else:
            degree_dict["Other"] += 1
        total_degree_number += 1

    return [int(100 * (degree_dict[term] / total_degree_number)) for term in category]

# Generates a random speciality based on the previous data and a given astronaut sex
def degree_random(sex):
    per_lst = degree(me_lst) if sex == 'M' else degree(we_lst)
    tester = randint(0, 100)
    return "Math" if tester <= per_lst[0] else "Physics" if per_lst[0] <= tester <= sum(per_lst[:2]) else "Engineering" \
        if sum(per_lst[:2]) <= tester <= sum(per_lst[:3]) else "Chemistry" if sum(per_lst[:3]) <= tester <= sum(per_lst[:4])\
        else "Biology" if sum(per_lst[:4]) <= tester <= sum(per_lst[:5]) else "Other"


"""
For defining a height a weight, ranges will be extracted from the U.S Army's height and weight screening 
requirements for the time being (Military Standards for Fitness, Weight, and Body Composition). These estimations 
are based on the assumption that the astronauts are fit. Conversion rates are taken from the google calculator.
"""

# Generates a random height between height bounds for a specified sex
def height_random(sex):
    height_inches = (randint(620, 660) if sex == 'F' else randint(650, 720)) / 10
    return int(height_inches * 2.54) / 100

# Generates a random weight between weight bounds for a specified sex
def weight_random(sex):
    weight_pounds = (randint(128, 150) if sex == 'F' else randint(168, 206))
    return int((weight_pounds / 2.20462) * 100) / 100
