import numpy as np
import matplotlib.pyplot as plt

sampling = 100
x_range = -10, 10
n_waves = 2
amplitudes = 1.7, .8
wavelength = 4, 7.5
velocity = 2, 1.5

x_ = np.linspace(x_range[0], x_range[1], sampling)

for time in np.arange(0, 40, .2):
    waves = [amplitudes[idx] * np.sin((2*np.pi/wavelength[idx])*(x_ - velocity[idx]*time)) for idx in range(n_waves)]
    superimposed_wave = sum(waves)
    
    plt.clf()
    plt.plot(x_, superimposed_wave)
    plt.ylim(-3, 3)
    plt.pause(.01)

