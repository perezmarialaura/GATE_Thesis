import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator, LogLocator, NullFormatter)
import matplotlib.axes as axes
plt.rc('font', family='Helvetica')

def normalize(v):
    norm = np.sum(v)
    if norm == 0:
        return v
    return v / norm

protons = np.genfromtxt('DoseDepth_Proton.txt')
n_neutrons, _, n_gammas, _ = np.genfromtxt('Zpos_data.txt', skip_header=1, unpack=True)
x = np.arange(0,200,2)

fig, ax1 = plt.subplots(figsize=(14,10))
ax1.plot(x, normalize(n_neutrons), label='Neutrons', linewidth=2, marker='o')
ax1.plot(x, normalize(n_gammas), label='Gammas', linewidth=2, marker='o')
ax1.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1.tick_params(axis='both', which='minor', direction='in', length=5)
plt.title('Particle production relative to Bragg Peak', fontsize=30, fontweight='bold')
plt.xlabel('Depth (mm)', fontweight='bold', fontsize=24)
ax1.xaxis.set_minor_locator(MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1.set_ylabel('Production probability', fontweight='bold', fontsize=24)
ax1.legend(fontsize=22)

ax2 = ax1.twinx()
ax2.plot(x, protons, linestyle='--', label='Proton Bragg Peak', linewidth=3, color='olivedrab')
ax2.set_ylabel('Dose (mGy)', fontsize=24)
ax2.tick_params(axis='y', which='major', labelsize=24, direction='in', length=10)
ax2.tick_params(axis='y', which='minor', direction='in', length=5)
ax2.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax2.legend(fontsize=22, loc=3)
plt.xlim(0,130)
plt.savefig('Zpos_BraggPeak.png')
