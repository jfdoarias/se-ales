from scipy import signal
from matplotlib import pyplot as plt
import numpy as np
import mysignals as sigs


corr_output_signal = signal.correlate(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response,mode ='same')
conv_output_signal = signal.convolve(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response,mode ='same')

plt.plot(conv_output_signal)
plt.show()
