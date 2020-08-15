import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.rc('font', family='Helvetica')
particles = ['n', r'$\gamma$', 'e-', 'e+', r'$\nu_e$', r'$\bar{\nu}_e$', r'$\alpha$', 'deuteron', 'triton', 'O16', 'p+', 'others']
processes = ['pInelastic', 'nCapture', 'Compt', 'eBrem', 'hElastic', 'Annihil', 'eIoni', 'RDecay', 'dInelastic']

_, particle_data = np.genfromtxt('Particles_PBS.txt', skip_header=1, unpack=True)
_, process_data = np.genfromtxt('Processes_PBS.txt', skip_header=1, unpack=True)

nparts = len(particle_data)
fig, ax1 = plt.subplots(figsize=(18,10))
x = np.linspace(0, nparts-1, nparts)
ax1.bar(x, particle_data, log=True, color='dodgerblue')
ax1.xaxis.set_major_locator(ticker.FixedLocator(np.linspace(0, nparts-1, nparts)))
ax1.xaxis.set_major_formatter(ticker.FixedFormatter(particles))
ax1.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1.tick_params(axis='y', which='minor', direction='in', length=5)
ax1.tick_params(axis='y', which='major', direction='in', length=10)
plt.title('Particle creation inside water phantom', fontsize=30, fontweight='bold')
plt.ylabel(r'Number of particles per 1$\times$10$^8$ primaries', fontweight='bold', fontsize=24)
plt.xticks(rotation=20)
plt.savefig('S2_SecondaryParticles.png')

nprocs = len(process_data)
fig, ax1 = plt.subplots(figsize=(18,10))
x = np.linspace(0, nprocs-1, nprocs)
ax1.bar(x, process_data, log=True, color='olivedrab')
ax1.xaxis.set_major_locator(ticker.FixedLocator(np.linspace(0, nprocs-1, nprocs)))
ax1.xaxis.set_major_formatter(ticker.FixedFormatter(processes))
ax1.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1.tick_params(axis='y', which='minor', direction='in', length=5)
ax1.tick_params(axis='y', which='major', direction='in', length=10)
plt.title('Physical processes inside water phantom', fontsize=30, fontweight='bold')
plt.ylabel(r'Number of processes per 1$\times$10$^8$ primaries', fontweight='bold', fontsize=24)
plt.xticks(rotation=20)
plt.savefig('S2_PhysicalProcesses.png')
