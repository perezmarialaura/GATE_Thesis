import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import matplotlib.ticker as ticker
import matplotlib.axes as axes

def normalize(v):
    norm = np.sum(v)
    if norm == 0:
        return v
    return v / norm

plt.rc('font', family='Helvetica')
plt.rc('ytick', labelsize=24)
energiesJC, int_nonfilt_unmoderated, int_gd_unmoderated, _, int_nonfilt_moderated, int_gd_moderated = np.genfromtxt('RAL_measurement_Gd0.5mm_filter.csv', skip_header=2, delimiter=';', unpack=True)
energies_fw, spectrum_fw = np.genfromtxt('S1_Filter_Water.txt', unpack=True)
energies_nfw, spectrum_nfw = np.genfromtxt('S1_NoFilter_Water.txt', unpack=True)

fig3, ax3 = plt.subplots(figsize=(14,10))
plt.title('AmBe neutron source in water - Unfiltered', fontsize=30, fontweight='bold')
ax3.plot(energies_nfw, normalize(spectrum_nfw), label='GATE ('+str(int(np.sum(spectrum_nfw)))+' events)', linewidth=2)
ax3.plot(energiesJC, normalize(int_nonfilt_moderated), label='Experimental ('+str(int(np.sum(int_nonfilt_moderated)))+' events)', linewidth=2)
ax3.set_ylabel('Normalised intensity', fontweight='bold', fontsize=24)
ax3.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax3.tick_params(axis='both', which='minor', direction='in', length=5)
ax3.xaxis.set_minor_locator(MultipleLocator(20))
ax3.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax3.set_xlabel('Energy (keV)', fontweight='bold', fontsize=24)
ax3.legend(fontsize=24)
plt.savefig('S1_Unfiltered_Water.png')

fig4, ax4 = plt.subplots(figsize=(14,10))
plt.title('AmBe neutron source in water - Filtered', fontsize=30, fontweight='bold')
ax4.plot(energies_fw, normalize(spectrum_fw), label='GATE ('+str(int(np.sum(spectrum_fw)))+' events)', linewidth=2)
ax4.plot(energiesJC, normalize(int_gd_moderated), label='Experimental ('+str(int(np.sum(int_gd_moderated)))+' events)', linewidth=2)
ax4.set_ylabel('Normalised intensity', fontweight='bold', fontsize=24)
ax4.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax4.tick_params(axis='both', which='minor', direction='in', length=5)
ax4.xaxis.set_minor_locator(MultipleLocator(20))
ax4.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax4.set_xlabel('Energy (keV)', fontweight='bold', fontsize=24)
ax4.legend(fontsize=24)
plt.savefig('S1_Filtered_Water.png')
