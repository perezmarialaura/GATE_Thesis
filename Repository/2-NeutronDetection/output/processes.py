import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.rc('font', family='Helvetica')

names = ['100eV', '1keV', '10keV', '100keV', '1MeV', '10MeV', '100MeV']
colors = ['dodgerblue', 'red', 'mediumpurple', 'orange', 'olivedrab', 'hotpink', 'grey']
processes = ['nCapture', 'Phot', 'Compt', 'Conv', 'eBrem', 'Annihil', 'eIoni', 'RDecay', 'nucPhot', 'nInelastic', 'hIoni', 'hElastic', 'ionIoni', 'pInelastic']#, 'dInelastic', 'Primary']

def load_data(volume, filter):
    vals_array = []
    for i in range(len(names)):
        _, vals = np.genfromtxt('Processes_'+volume+'_'+names[i]+filter+'.txt', skip_header=1, unpack=True)
        vals_array.append(np.array(vals[:-2]))
    return vals_array
  
# The x val corresponds to energy. The y val corresponds to process.
Det_F = load_data('Detector', '_F')
Det_NF = load_data('Detector', '_NF')
Filt = load_data('Filter', '')

def plot(array, title, filterout):
    fig, ax1 = plt.subplots(figsize=(21,10))
    for i in range(len(names)):
        x = np.linspace(-0.3+0.1*i, 12.7+0.1*i, 14)
        ax1.bar(x, array[i], label=names[i], log=True, width=0.1, color=colors[i])
    ax1.xaxis.set_major_locator(ticker.FixedLocator(np.linspace(0, 13, 14)))
    ax1.xaxis.set_major_formatter(ticker.FixedFormatter(processes))
    ax1.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
    ax1.tick_params(axis='y', which='minor', direction='in', length=5)
    ax1.tick_params(axis='y', which='major', direction='in', length=10)
    #ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(y),0)))).format(y)))
    plt.title('Processes inside '+title, fontsize=30, fontweight='bold')
    #plt.xlabel('Physical processes', fontweight='bold', fontsize=24)
    plt.ylabel(r'Number of events per $5\times10^7$ neutrons', fontweight='bold', fontsize=24)
    plt.xticks(rotation=20)
    plt.legend(fontsize=22)
    plt.savefig('S0_Processes_'+filterout+'.png')

plot(Det_F, 'Detector (Filtered)', 'Detector_F')
plot(Det_NF, 'Detector (Unfiltered)', 'Detector_NF')
plot(Filt, 'Filter', 'Filter')
