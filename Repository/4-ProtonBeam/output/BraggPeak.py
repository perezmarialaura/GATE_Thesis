import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator, LogLocator, NullFormatter)
import matplotlib.axes as axes
from scipy import ndimage

plt.rc('font', family='Helvetica')
# This funciton reads a '.mhd' file using SimpleITK and return the image array, origin and spacing of the image.

def load_itk(filename):
    # Reads the image using SimpleITK
    itkimage = sitk.ReadImage(filename)

    # Convert the image to a  numpy array first and then shuffle the dimensions to get axis in the order z,y,x
    ct_scan = sitk.GetArrayFromImage(itkimage)

    # Read the origin of the ct_scan, will be used to convert the coordinates from world to voxel and vice versa.
    origin = np.array(list(reversed(itkimage.GetOrigin())))

    # Read the spacing along each dimension
    spacing = np.array(list(reversed(itkimage.GetSpacing())))

    return ct_scan, origin, spacing

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

scanP, originP, spacingP = load_itk('ProtonDose-Dose.mhd')

newscan = scanP #ndimage.gaussian_filter(scanP, sigma=2)
bragg = []
yerr = []
x = np.arange(0, 200, 2)

for i in x:
    val = newscan[i, 99, 99]*1000
    bragg.append(val)
    yerr.append(0.078*val)

dmax = np.round(np.max(bragg),2)
posdmax = int(x[np.argmax(bragg)])
range_idx = find_nearest(bragg, dmax*0.2)
range = int(x[range_idx])

fig, ax1 = plt.subplots(figsize=(14,10))
ax1.errorbar(x, bragg, xerr=1, yerr=yerr, label='Dmax = '+str(dmax)+' mGy at '+str(posdmax)+' mm, \n R = '+str(range)+' mm', fmt='.', markersize=7, capsize=3)
ax1.tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1.tick_params(axis='both', which='minor', direction='in', length=5)
plt.title('Bragg peak for 100 MeV protons in water phantom', fontsize=30, fontweight='bold')
plt.xlabel('Depth (mm)', fontweight='bold', fontsize=24)
ax1.xaxis.set_major_locator(MultipleLocator(10))
ax1.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1.yaxis.set_minor_locator(ticker.AutoMinorLocator())
plt.ylabel('Dose (mGy)', fontweight='bold', fontsize=24)
plt.xlim(0, 100)
plt.legend(fontsize=22)
plt.savefig('Proton100MeV_BraggPeak.png')
