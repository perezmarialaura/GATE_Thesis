import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator,LogLocator, NullFormatter)
import matplotlib.axes as axes
#import matplotlib.font_manager
#matplotlib.font_manager._rebuild()
plt.rc('font', family='Helvetica')

raw = pd.read_csv("S2_PhaseSpace_Protons.txt", sep=" ", header=1)
a = raw.iloc[::8]
data = a.to_numpy()
del a, raw
[particles, x, y, z, energies, theta, phi] = np.transpose(data)

def divide_per_particle(variable, title, xlabel, figname):
    fig, ax1 = plt.subplots(figsize=(14,10))
    ax1.hist(variable, label=str(len(variable))+' events', histtype='step', bins=100, density=True, linewidth=2)
    ax1.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
    ax1.tick_params(axis='both', which='minor', direction='in', length=5)
    plt.title(title, fontsize=30, fontweight='bold')
    plt.xlabel(xlabel, fontweight='bold', fontsize=24)
    ax1.xaxis.set_minor_locator(MultipleLocator(5))
    ax1.yaxis.set_minor_locator(ticker.AutoMinorLocator())
    plt.ylabel('Probability', fontweight='bold', fontsize=24)
    plt.legend(fontsize=22)
    plt.savefig(figname+'_Primaries.png')

divide_per_particle(theta, r'Emittance X $\theta$', r'$\theta$ [deg]', 'emittanceX')
divide_per_particle(phi, 'Emittance Y $\phi$', '$\phi$ [deg]', 'emittanceY')
divide_per_particle(x, 'X position', '$x$ [cm]', 'Xpos')
divide_per_particle(y, 'Y position', '$y$ [cm]', 'Ypos')
divide_per_particle(z, 'Z position', '$z$ [cm]', 'Zpos')

del x, y, z, phi, theta

fig, ax1 = plt.subplots(figsize=(15,10))
ax1.hist(particles, histtype='step', log=True, bins=np.linspace(-0.5, 15.5, 17), label=r'Number of primaries = 1$\times$10$^8$', linewidth=2)
ax1.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1.tick_params(axis='y', which='minor', direction='in', length=5)
plt.title('Particles entering the phantom', fontsize=30, fontweight='bold')
plt.xlabel('Particle type', fontweight='bold', fontsize=24)
#ax1.yaxis.set_minor_locator(MultipleLocator(5000))
plt.ylabel('Number of events', fontweight='bold', fontsize=24)
plt.legend(fontsize=22)
plt.savefig('PrimaryParticles.png')


fig, ax1 = plt.subplots(figsize=(14,10))
ax1.hist(energies, label='Primary energy: 100 MeV', histtype='step', bins=300, log=True, linewidth=2)
ax1.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1.tick_params(axis='both', which='minor', direction='in', length=5)
plt.title('Energy of incoming particles', fontsize=30, fontweight='bold')
plt.xlabel('Energy [MeV]', fontweight='bold', fontsize=24)
ax1.set_xscale('log')
ax1.xaxis.set_major_locator(LogLocator(base=10.0, subs=(1.0, ), numticks=100))
ax1.xaxis.set_minor_locator(LogLocator(base=10.0, subs=np.arange(2, 10) * .1,
                                 numticks=100))
ax1.xaxis.set_minor_formatter(NullFormatter())
plt.ylabel('Number of events', fontweight='bold', fontsize=24)
plt.legend(fontsize=22)
plt.savefig('EnergySpectra_Primaries.png')
