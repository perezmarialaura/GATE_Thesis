import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import matplotlib.ticker as ticker
import matplotlib.axes as axes
from scipy import optimize
from scipy.signal import argrelextrema


plt.rc('font', family='Helvetica')
x = np.linspace(0, 180, 180)

#-------------FUNCTIONS----------------------------
def sinusoidal(x, amp, omega, phi, d):
    return amp*np.sin(omega*x*np.pi/180 + phi) + d
    
    
def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm

def y_func(bins, vals, initial_guess):
    params, _ = optimize.curve_fit(sinusoidal, bins, vals, p0=initial_guess, maxfev=5000)
    y = sinusoidal(x, params[0], params[1], params[2], params[3])
    maxangle = np.round(x[np.argmax(y)], 2)
    return y, maxangle
    
def y_func_poly(bins, vals):
    p = np.polyfit(bins, vals, 5)
    y = p[0]*x**5 + p[1] *x**4 + p[2]*x**3 + p[3]*x**2 + p[4]*x + p[5]
    #local_max = argrelextrema(y, np.greater)
    #local_min = argrelextrema(y, np.less)
    maxangle = np.round(x[np.argmax(y)], 2)
    return y, maxangle

#-----------------DATA------------------------------
#Filtered data for gammas
bins_gpr, vals_gpr =np.genfromtxt("S3A_Gammas_RadCurve.txt", unpack=True)
bins_gcr, vals_gcr =np.genfromtxt("S3B_Gammas_RadCurve.txt", unpack=True)

#Unfiltered data for gammas
bins_gpr_nf, vals_gpr_nf = np.genfromtxt("S3A_Gammas_RadCurve_NF.txt", unpack=True)
bins_gcr_nf, vals_gcr_nf = np.genfromtxt("S3B_Gammas_RadCurve_NF.txt", unpack=True)

#Filtered data for neutrons
bins_npr, vals_npr =np.genfromtxt("S3A_Neutrons_RadCurve.txt", unpack=True)
bins_ncr, vals_ncr = np.genfromtxt("S3B_Neutrons_RadCurve.txt", unpack=True)

#Unfiltered data for neutrons
bins_npr_nf, vals_npr_nf = np.genfromtxt("S3A_Neutrons_RadCurve_NF.txt", unpack=True)
bins_ncr_nf, vals_ncr_nf = np.genfromtxt("S3B_Neutrons_RadCurve_NF.txt", unpack=True)

#Fits
y_gpr_nf, maxangle_gpr_nf = y_func(bins_gpr_nf, vals_gpr_nf, [450, 2, 2, 0.07])
y_gpr, maxangle_gpr = y_func(bins_gpr, vals_gpr,[100, 2, 2, 0.07])
y_gcr_nf, maxangle_gcr_nf = y_func(bins_gcr_nf, vals_gcr_nf, [700, 2, 1, 0.07])
y_gcr, maxangle_gcr = y_func(bins_gcr, vals_gcr, [200, 1, 0, 400])


y_npr_nf, maxangle_npr_nf = y_func(bins_npr_nf, vals_npr_nf, [110, 1, 0, 60])
y_npr, maxangle_npr = y_func_poly(bins_npr, vals_npr)
y_ncr_nf, maxangle_ncr_nf = y_func(bins_ncr_nf, vals_ncr_nf, [80, 1, 0, 60])
y_ncr, maxangle_ncr = y_func_poly(bins_ncr, vals_ncr)

#--------------------GAMMA PLOT-------------------------------------
fig, ax1 = plt.subplots(1, 2, figsize=(22,10))
fig.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.9, wspace=0.25, hspace=0.1)
plt.suptitle('RadICAL curves - Gammas', fontsize=30, fontweight='bold')

ax1[0].set_title('Point source', fontsize=26)
ax1[0].scatter(bins_gpr_nf, vals_gpr_nf, label='Unfiltered data', color='deepskyblue', s=15)
ax1[0].scatter(bins_gpr, vals_gpr, label='Filtered data', color='royalblue', s=15)
ax1[0].plot(x, y_gpr_nf, linewidth=2, label='Fit - Max pos = '+str(maxangle_gpr_nf)+'º',  color='deepskyblue')
ax1[0].plot(x, y_gpr, linewidth=2, label='Fit - Max pos = '+str(maxangle_gpr)+'º', color='royalblue')

ax1[1].set_title('Continuous source', fontsize=26)
ax1[1].scatter(bins_gcr_nf, vals_gcr_nf, label='Unfiltered data', color='yellowgreen', s=15)
ax1[1].scatter(bins_gcr, vals_gcr, label='Filtered data', color='olivedrab', s=15)
ax1[1].plot(x, y_gcr_nf, linewidth=2, label='Fit - Max pos = '+str(maxangle_gcr_nf)+'º',  color='yellowgreen')
ax1[1].plot(x, y_gcr, linewidth=2, label='Fit - Max pos = '+str(maxangle_gcr)+'º', color='olivedrab')

ax1[0].set_ylabel('N events', fontweight='bold', fontsize=24)
ax1[0].tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1[0].tick_params(axis='both', which='minor', direction='in', length=5)
ax1[0].xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1[0].yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1[0].set_xlabel('Rotation angle (deg)', fontweight='bold', fontsize=24)
ax1[0].set_xlim(0, 180)
ax1[0].set_ylim(0, 800)
ax1[0].legend(fontsize=24, ncol=2)

ax1[1].set_ylabel('N events', fontweight='bold', fontsize=24)
ax1[1].tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1[1].tick_params(axis='both', which='minor', direction='in', length=5)
ax1[1].xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1[1].yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1[1].set_xlabel('Rotation angle (deg)', fontweight='bold', fontsize=24)
ax1[1].set_xlim(0, 180)
ax1[1].set_ylim(0, 1200)
ax1[1].legend(fontsize=24, ncol=2)
plt.savefig('S3_Gammas.png')
#plt.show()

#--------------------NEUTRON PLOT-------------------------
fig, ax1 = plt.subplots(1, 2, figsize=(22,10))
fig.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.9, wspace=0.25, hspace=0.1)
plt.suptitle('RadICAL curves - Neutrons', fontsize=30, fontweight='bold')

ax1[0].set_title('Point source', fontsize=26)
ax1[0].scatter(bins_npr_nf, vals_npr_nf, label='Unfiltered data', color='deepskyblue', s=15)
ax1[0].scatter(bins_npr, vals_npr, label='Filtered data', color='royalblue', s=15)
ax1[0].plot(x, y_npr_nf, linewidth=2, label='Fit - Max pos = '+str(maxangle_npr_nf)+'º',  color='deepskyblue')
ax1[0].plot(x, y_npr, linewidth=2, label='Fit', color='royalblue')

ax1[1].set_title('Continuous source', fontsize=26)
ax1[1].scatter(bins_ncr_nf, vals_ncr_nf, label='Unfiltered data', color='yellowgreen', s=15)
ax1[1].scatter(bins_ncr, vals_ncr, label='Filtered data', color='olivedrab', s=15)
ax1[1].plot(x, y_ncr_nf, linewidth=2, label='Fit - Max pos = '+str(maxangle_ncr_nf)+'º',  color='yellowgreen')
ax1[1].plot(x, y_ncr, linewidth=2, label='Fit', color='olivedrab')

ax1[0].set_ylabel('N events', fontweight='bold', fontsize=24)
ax1[0].tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1[0].tick_params(axis='both', which='minor', direction='in', length=5)
ax1[0].xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1[0].yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1[0].set_xlabel('Rotation angle (deg)', fontweight='bold', fontsize=24)
ax1[0].set_xlim(0, 180)
ax1[0].set_ylim(0, 180)
ax1[0].legend(fontsize=24, ncol=2)

ax1[1].set_ylabel('N events', fontweight='bold', fontsize=24)
ax1[1].tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1[1].tick_params(axis='both', which='minor', direction='in', length=5)
ax1[1].xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1[1].yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1[1].set_xlabel('Rotation angle (deg)', fontweight='bold', fontsize=24)
ax1[1].set_xlim(0, 180)
ax1[1].set_ylim(0, 160)
ax1[1].legend(fontsize=24, ncol=2)
plt.savefig('S3_Neutrons.png')
