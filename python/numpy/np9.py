import numpy as np

# Closing prices over 5 days
prices = np.array([150, 152, 149, 153, 158])

# Daily return = (today - yesterday) / yesterday
returns = np.diff(prices) / prices[:-1]

print("Daily returns:", returns)