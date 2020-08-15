import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import matplotlib.axes as axes
import pandas as pd

def normalize(v):
    norm = np.sum(v)
    if norm == 0:
        return v
    return v / norm

plt.rc('font', family='Helvetica')
plt.rc('ytick', labelsize=24)
energies_gate, spectrum_gate1 = np.genfromtxt('GammaTest_Am241.txt', unpack=True)
hexitec = pd.read_csv('Am241_Hexitec.txt', sep= ' ')
a = hexitec.iloc[::2]
a = a.to_numpy()
[energies_hex, spectrum_hex] = np.transpose(a)
totcounts_gate = int(np.sum(spectrum_gate))
totcounts_hex = int(np.sum(spectrum_hex))

fig, ax1 = plt.subplots(figsize=(14,10))
#plt.xticks(np.arange(0, 600, 50))
plt.title('Am-241 gamma source in air', fontsize=30, fontweight='bold')
ax1.plot(energies_gate, normalize(spectrum_gate), label='GATE ('+"{:.2e}".format(totcounts_gate)+' events)', linewidth=2)
ax1.plot(energies_hex, normalize(spectrum_hex), label='HEXITEC ('+"{:.2e}".format(totcounts_hex)+' events)', linewidth=2)
ax1.set_ylabel('Normalised Intensity', fontweight='bold', fontsize=24)
ax1.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1.tick_params(axis='both', which='minor', direction='in', length=5)
ax1.set_xlabel('Energy (keV)', fontweight='bold', fontsize=24)
ax1.xaxis.set_minor_locator(MultipleLocator(2))
ax1.yaxis.set_minor_locator(ticker.AutoMinorLocator())
plt.legend(fontsize=22)
plt.xlim(0, 80)
plt.savefig('Am241_HexVsGate.png')
