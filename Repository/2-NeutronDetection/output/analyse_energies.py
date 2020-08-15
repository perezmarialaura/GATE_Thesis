import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator, LogLocator, NullFormatter)
import matplotlib.axes as axes

def normalize(v):
    norm = np.sum(v)
    if norm == 0:
        return v
    return v / norm


plt.rc('font', family='Helvetica')
plt.rc('ytick', labelsize=24)
names = ['100eV', '1keV', '10keV', '100keV', '1MeV', '10MeV', '100MeV']
colors = ['red', 'orange', 'olivedrab', 'dodgerblue', 'mediumpurple', 'hotpink', 'grey', 'brown']
energies_f = []
spectra_f = []
energies_nf = []
spectra_nf = []
for i in range(len(names)):
    energies_f.append(np.genfromtxt('S0_'+names[i]+'_F.txt', unpack=True)[0])
    energies_nf.append(np.genfromtxt('S0_'+names[i]+'_NF.txt', unpack=True)[0])
    spectra_f.append(np.genfromtxt('S0_'+names[i]+'_F.txt', unpack=True)[1])
    spectra_nf.append(np.genfromtxt('S0_'+names[i]+'_NF.txt', unpack=True)[1])

fig, ax1 = plt.subplots(figsize=(14,10))
plt.title('Neutrons in air - No filter', fontsize=30, fontweight='bold')
plt.yscale('Log')
for i in range(len(names)):
    ax1.plot(energies_nf[i], spectra_nf[i], label='$E_0$ = '+names[i], linewidth=2, color=colors[i])
ax1.yaxis.set_major_locator(LogLocator(base=10.0, subs=(1.0, ), numticks=100))
ax1.yaxis.set_minor_locator(LogLocator(base=10.0, subs=np.arange(2, 10) * .1,
                                 numticks=100))
ax1.yaxis.set_minor_formatter(NullFormatter())
ax1.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1.tick_params(axis='both', which='minor', direction='in', length=6)
ax1.set_xlabel('Energy (keV)', fontweight='bold', fontsize=24)
ax1.set_ylabel('Detected counts', fontweight='bold', fontsize=24)
ax1.xaxis.set_minor_locator(MultipleLocator(10))
plt.legend(fontsize=22, ncol=2)
#plt.xlim(0, 250)
plt.savefig('S0_MoreEnergies_NoFilter.png')

fig, ax1 = plt.subplots(figsize=(14,10))
plt.title('Neutrons in air - Filtered with Gd', fontsize=30, fontweight='bold')
plt.yscale('Log')
for i in range(len(names)):
    ax1.plot(energies_f[i], spectra_f[i], label='$E_0$ = '+names[i], linewidth=2, color=colors[i])
ax1.yaxis.set_major_locator(LogLocator(base=10.0, subs=(1.0, ), numticks=100))
ax1.yaxis.set_minor_locator(LogLocator(base=10.0, subs=np.arange(2, 10) * .1,
                                 numticks=100))
ax1.yaxis.set_minor_formatter(NullFormatter())
ax1.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1.tick_params(axis='both', which='minor', direction='in', length=6)
ax1.set_xlabel('Energy (keV)', fontweight='bold', fontsize=24)
ax1.set_ylabel('Detected counts', fontweight='bold', fontsize=24)
ax1.xaxis.set_minor_locator(MultipleLocator(10))
plt.legend(fontsize=22, ncol=2)
#plt.xlim(0, 250)
plt.savefig('S0_MoreEnergies_Filter.png')
