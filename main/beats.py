import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 1000)

f1 = 10
f2 = 12

f_beats = abs(f1 - f2)
print(f"Beat frequency: {f_beats} Hz")

y1 = np.sin(2 * np.pi * f1 * t)
y2 = np.sin(2 * np.pi * f2 * t)

y_total = (y1 + y2)

envelope = 2 * np.abs(np.cos(np.pi * (f1 - f2) * t))

fig, ax = plt.subplots(3, 1, figsize=(10, 8))

ax[0].plot(t, y1)
ax[1].plot(t, y2)
ax[2].plot(t, y_total)

ax[2].plot(t, envelope, label="Upper Envelope")
ax[2].plot(t, -envelope, label="Lower Envelope")

ax[0].set_title("First Wave")
ax[0].set_xlabel("Time")
ax[0].set_ylabel("Amplitude")

ax[1].set_title("Second Wave")
ax[1].set_xlabel("Time")
ax[1].set_ylabel("Amplitude")

ax[2].set_title("Sum Of Two Waves")
ax[2].set_xlabel("Time")
ax[2].set_ylabel("Amplitude")

ax[0].grid()
ax[1].grid()
ax[2].grid()

ax[2].legend(loc="upper right")

fig.tight_layout()

plt.show()