"""
Exercise: Introduction to NumPy

In this script, we explore the fundamentals of NumPy for efficient data 
manipulation and analysis in Python.

Learning objectives:
- How to create, reshape, and manipulate arrays using NumPy.
- How to access and modify elements in NumPy arrays.
- How to apply key NumPy functions to analyse real-world problems.
"""

import numpy as np

print("=" * 80)
print("NumPy Exercises - Solutions")
print("=" * 80)

# Exercise 1
print("\nExercise 1: Day with Highest Average Pollution Level")
print("-" * 80)
print("pollution_data.mean(axis=1) calculates the average pollution level for each")
print("day (row). np.argmax finds the index of the day with the highest average")
print("pollution level.")

pollution_data = np.array([[45, 65, 70], [55, 60, 50], [60, 58, 67]])
most_polluted_day_index = np.argmax(pollution_data.mean(axis=1))
print(f"\nMost polluted day index: {most_polluted_day_index}")
print(f"Pollution data for that day: {pollution_data[most_polluted_day_index]}")

# Exercise 2
print("\nExercise 2: Total Forest Coverage Lost")
print("-" * 80)
print("100 - forest_coverage calculates the proportion of deforestation for each")
print("region. Summing these loss values and multiplying them by 100 (conversion to")
print("square kilometres) gives the total forest cover lost in square kilometres.")

forest_coverage = np.array([70, 80, 65, 90, 85])
total_forest_cover_lost = (100 - forest_coverage).sum() * 100
print(f"\nTotal forest cover lost: {total_forest_cover_lost} square kilometres")

# Exercise 3
print("\nExercise 3: Water Body with Worst Average Quality")
print("-" * 80)
print("water_quality.mean(axis=1) computes the average quality parameter for each")
print("water body (row). np.argmin finds the index of the water body with the")
print("worst average quality.")

water_quality = np.array([[7.8, 6.5, 8.0], [5.4, 7.2, 6.5]])
worst_water_quality_index = np.argmin(water_quality.mean(axis=1))
print(f"\nWorst water quality index: {worst_water_quality_index}")

# Exercise 4
print("\nExercise 4: Region with Highest Average Animal Sightings")
print("-" * 80)
print("animal_sightings.mean(axis=1) computes the average number of sightings per")
print("region. np.argmax finds the index of the region with the highest average.")

animal_sightings = np.array([[5, 7, 8], [3, 4, 6], [9, 10, 7]])
highest_sightings_region_index = np.argmax(animal_sightings.mean(axis=1))
print(f"\nHighest sightings region index: {highest_sightings_region_index}")

# Exercise 5
print("\nExercise 5: Reshape Bird Sightings Data")
print("-" * 80)
print("The reshape(4, 7) function reshapes the 1D array into a 2D array with 4 rows")
print("(weeks) and 7 columns (days). sum(axis=1) calculates the sum along the rows")
print("(each week), providing the total bird sightings per week.")

bird_sightings = np.array([3, 4, 2, 5, 1, 0, 4, 3, 5, 2, 1, 7, 8, 1, 2, 3, 4, 1, 
                          0, 5, 6, 2, 3, 4, 1, 4, 6, 7])
reshaped_sightings = bird_sightings.reshape(4, 7)
total_sightings_per_week = reshaped_sightings.sum(axis=1)
print(f"\nTotal sightings per week: {total_sightings_per_week}")

# Exercise 6
print("\nExercise 6: Transpose Climate Data")
print("-" * 80)
print("transpose() changes the shape of climate_data so that rows and columns are")
print("swapped. Now, the first row represents temperatures and the second row")
print("represents precipitation for each month. The mean() function calculates the")
print("average value for each of these rows, giving the average temperature and")
print("precipitation over the year.")

climate_data = np.array([[22, 50], [25, 43], [28, 35], [30, 20], [27, 25], 
                        [25, 30], [23, 40], [24, 55], [22, 60], [20, 65], 
                        [18, 70], [22, 58]])
transposed_climate_data = climate_data.transpose()
print(f"\nTransposed climate data shape: {transposed_climate_data.shape}")

average_temperature = transposed_climate_data[0].mean()
average_precipitation = transposed_climate_data[1].mean()
print(f"Average temperature: {average_temperature}")
print(f"Average precipitation: {average_precipitation}")

print("\n" + "=" * 80)
print("All exercises completed successfully!")
print("=" * 80)
