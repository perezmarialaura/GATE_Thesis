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


scanP, originP, spacingP = load_itk('ProtonDose-Dose.mhd')
scanG, originG, spacingG = load_itk('GammaDose-Dose.mhd')
scanN, originN, spacingN = load_itk('NeutronDose-Dose.mhd')

def get_dose2D(scan, particle):
    img = np.zeros((200,200))
    for i in range(200):
        img[i] = scan[i, 99, :]
    fig, ax1 = plt.subplots(figsize=(14,10))
    fig.suptitle(particle+' 2D dose distribution', fontsize=34)
    if particle == "Proton":
        f = ax1.imshow(img*1000, cmap='nipy_spectral', extent=[-10,10,20,0])#, vmin=0, vmax=220)
        cbar = fig.colorbar(f, ax=ax1, fraction=0.03, pad=0.04)
        cbar.set_label('Dose (mGy)', fontsize=28)
    else:
        f = ax1.imshow(img*1E6, cmap='nipy_spectral', extent=[-10,10,20,0])#, vmin=0, vmax=220)
        cbar = fig.colorbar(f, ax=ax1, fraction=0.03, pad=0.04)
        cbar.set_label('Dose (µGy)', fontsize=28)
    cbar.ax.tick_params(labelsize=28)
    plt.xlabel('Distance from beam axis (cm)', fontsize=28)
    plt.ylabel('Depth (cm)', fontsize=28)
    ax1.tick_params(labelsize=28)
    ax1.set_yticks([0,5,10,15,20])
    plt.savefig(particle+'Dose2D.png')

get_dose2D(scanP, "Proton")
get_dose2D(scanG, "Gamma")
get_dose2D(scanN, "Neutron")


bragg = []
x = np.arange(0, 200, 2)

for i in x:
    val = scanP[i, 99, 99]*1000
    bragg.append(val)

np.savetxt('DoseDepth_Proton.txt', bragg, fmt='%.2f')
