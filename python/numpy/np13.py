import numpy as np

# Simulated audio signal (raw amplitude values)
audio = np.array([-3000, -1000, 0, 1000, 3000])

# Normalize to range [-1, 1]
normalized_audio = audio / np.max(np.abs(audio))
print("Normalized audio:", normalized_audio)
