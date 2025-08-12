import numpy as np

# Historical sales data (units sold per week)
sales = np.array([100, 105, 110, 120, 130])

# Estimate average weekly increase
growth_rate = np.mean(np.diff(sales))

# Forecast next 3 weeks
future = sales[-1] + growth_rate * np.arange(1, 4)

print("Forecast:", future)
