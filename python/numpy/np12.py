import numpy as np

dice = np.random.randint(1, 7, size=10000)  # 10,000 rolls

# Count each face's frequency
for face in range(1, 7):
    print(f"{face}: {(dice == face).sum()} times")
