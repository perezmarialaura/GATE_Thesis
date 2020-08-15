import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator, LogLocator, NullFormatter)
import matplotlib.axes as axes
plt.rc('font', family='Helvetica')

raw = pd.read_csv("S2_PhaseSpace_Secondaries.txt", sep=" ", header=1)
a = raw.iloc[::8]
data = a.to_numpy()
del a, raw
[particles, x, y, z, energies, theta, phi, process] = np.transpose(data)

def divide_per_particle(variable, title, xlabel, plot, figname):
    new_variable_gamma = []
    new_variable_neutron = []
    for i in range(len(variable)):
        if particles[i] == "gamma":
            new_variable_gamma.append(variable[i])
        elif particles[i] == "neutron":
            new_variable_neutron.append(variable[i])
        else:
            continue
    if plot == True:
        fig, ax1 = plt.subplots(figsize=(14,10))
        ax1.hist(new_variable_neutron, label='Neutrons', histtype='step', bins=100, density=True, linewidth=2)
        ax1.hist(new_variable_gamma, label='Gammas', histtype='step', bins=100, density=True, linewidth=2)
        ax1.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
        ax1.tick_params(axis='both', which='minor', direction='in', length=5)
        plt.title(title, fontsize=30, fontweight='bold')
        plt.xlabel(xlabel, fontweight='bold', fontsize=24)
        ax1.xaxis.set_minor_locator(MultipleLocator(5))
        ax1.yaxis.set_minor_locator(ticker.AutoMinorLocator())
        plt.ylabel('Probability', fontweight='bold', fontsize=24)
        plt.legend(fontsize=22)
        plt.savefig(figname+'.png')
    return new_variable_gamma, new_variable_neutron

x_gamma, x_neutron = divide_per_particle(x, r'Production in X axis', r'X pos [mm] ', True, 'Xpos_secondaries')
y_gamma, y_neutron = divide_per_particle(y, r'Production in Y axis', r'Y pos [mm] ', True, 'Ypos_secondaries')
z_gamma, z_neutron = divide_per_particle(z, r'Production in Z axis', r'Z pos [mm] ', True, 'Zpos_secondaries')
theta_gamma, theta_neutron = divide_per_particle(theta, r'Emittance X $\theta$', r'$\theta$ [deg]', True, 'emittanceX_secondaries')
phi_gamma, phi_neutron = divide_per_particle(phi, 'Emittance Y $\phi$', '$\phi$ [deg]', True, 'emittanceY_secondaries')
e_gamma, e_neutron = divide_per_particle(energies, '', '', False, '')

del x, y, z, energies, phi, theta

fig, ax1 = plt.subplots(figsize=(15,10))
ax1.hist(particles, histtype='step', log=True, bins=np.linspace(-0.5, 7.5, 9), label=r'Number of primaries = 1$\times$10$^8$', linewidth=2)
ax1.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1.tick_params(axis='y', which='minor', direction='in', length=5)
plt.title('Particle creation inside phantom', fontsize=30, fontweight='bold')
plt.xlabel('Particle type', fontweight='bold', fontsize=24)
plt.ylabel('Number of events', fontweight='bold', fontsize=24)
plt.legend(fontsize=22)
plt.savefig('SecondaryParticles.png')

fig, ax1 = plt.subplots(figsize=(20,10))
ax1.hist(process, histtype='step', log=True, label=r'Number of primaries = 1$\times$10$^8$', bins=np.linspace(-0.5, 13.5, 15), linewidth=2)
ax1.tick_params(axis='both', which='major', labelsize=16, direction='in', length=10)
ax1.tick_params(axis='y', which='minor', direction='in', length=5)
plt.title('Secondary particle production mechanisms', fontsize=30, fontweight='bold')
plt.xlabel('Process name', fontweight='bold', fontsize=24)
plt.xticks(rotation=20)
plt.ylabel('Number of events', fontweight='bold', fontsize=24)
plt.legend(fontsize=22)
plt.savefig('ParticleProcesses.png')

fig, ax1 = plt.subplots(figsize=(14,10))
ax1.hist(e_neutron, label='Neutrons', histtype='step', bins=300, log=True, linewidth=2)
ax1.hist(e_gamma, label='Gammas', histtype='step', bins=300, log=True, linewidth=2)
ax1.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1.tick_params(axis='both', which='minor', direction='in', length=5)
plt.title('Kinetic energy of secondary particles', fontsize=30, fontweight='bold')
plt.xlabel('Energy [MeV]', fontweight='bold', fontsize=24)
ax1.set_xscale('log')
ax1.xaxis.set_major_locator(LogLocator(base=10.0, subs=(1.0, ), numticks=100))
ax1.xaxis.set_minor_locator(LogLocator(base=10.0, subs=np.arange(2, 10) * .1,
                                 numticks=100))
ax1.xaxis.set_minor_formatter(NullFormatter())
plt.ylabel('Number of events', fontweight='bold', fontsize=24)
plt.legend(fontsize=22)
plt.savefig('EnergySpectra_Secondaries.png')
