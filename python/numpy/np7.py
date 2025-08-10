##Author P tripathi

import numpy as np

# Each row = a city, each column = temperature for a day
temperatures = np.array([
    [30, 32, 31, 29, 28, 33, 35],  # City A
    [25, 26, 27, 26, 25, 24, 26],  # City B
    [40, 42, 41, 39, 38, 37, 36]   # City C
])

# Average temperature per city
avg_per_city = np.mean(temperatures, axis=1)
print("Average temperatures for each city:", avg_per_city)

# Average temperature per day
avg_per_day = np.mean(temperatures, axis=0)
print("Average temperature for each day of the week:", avg_per_day)

# City with the highest average
highest = np.argmax(avg_per_city)
print("City with highest average temperature is City", chr(65 + highest))
