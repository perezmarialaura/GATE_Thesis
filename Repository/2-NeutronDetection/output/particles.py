import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.rc('font', family='Helvetica')
names = ['100eV', '1keV', '10keV', '100keV', '1MeV', '10MeV', '100MeV']
colors = ['dodgerblue', 'red', 'mediumpurple', 'orange', 'olivedrab', 'hotpink', 'grey']
particles1 = [r'$\gamma$', 'e-', 'e+', r'$\nu_e$', r'$\bar{\nu}_e$', 'p+', r'$\alpha$', 'Cd\n isotopes', 'Te\n isotopes', 'Gd\n isotopes']
particles2 = [r'$\gamma$', 'e-', 'e+', r'$\nu_e$', r'$\bar{\nu}_e$', 'p+', r'$\alpha$', 'Gd\n isotopes']

def load_data(volume, filter):
    vals_array = []
    for i in range(len(names)):
        _, vals = np.genfromtxt('Particles_'+volume+'_'+names[i]+filter+'.txt', skip_header=1, unpack=True)
        if volume == 'Detector':
            vals_array.append(vals[:-3])
        else:
            vals_array.append(vals[:-2])
    return vals_array

# The x val corresponds to energy. The y val corresponds to process.
Det_F = load_data('Detector', '_F')
Det_NF = load_data('Detector', '_NF')
Filt = load_data('Filter', '')

def plot(array, title, filterout, particles):
    nparts = len(array[0])
    fig, ax1 = plt.subplots(figsize=(18,10))
    for i in range(len(names)):
        x = np.linspace(-0.3+0.1*i, (nparts-1.3)+0.1*i, nparts)
        ax1.bar(x, array[i], label=names[i], log=True, width=0.1, color=colors[i])
    ax1.xaxis.set_major_locator(ticker.FixedLocator(np.linspace(0, nparts-1, nparts)))
    ax1.xaxis.set_major_formatter(ticker.FixedFormatter(particles))
    ax1.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
    ax1.tick_params(axis='y', which='minor', direction='in', length=5)
    ax1.tick_params(axis='y', which='major', direction='in', length=10)
    #ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(y),0)))).format(y)))
    plt.title('Particle creation inside '+title, fontsize=30, fontweight='bold')
    plt.ylabel(r'Number of particles per 5$\times$10$^7$ neutrons', fontweight='bold', fontsize=24)
    plt.xticks(rotation=20)
    plt.legend(fontsize=22, ncol=4)
    plt.savefig('S0_Particles_'+filterout+'.png')

plot(Det_F, 'Detector (Filtered)', 'Detector_F', particles1)
plot(Det_NF, 'Detector (Unfiltered)', 'Detector_NF', particles1)
plot(Filt, 'Filter', 'Filter', particles2)
