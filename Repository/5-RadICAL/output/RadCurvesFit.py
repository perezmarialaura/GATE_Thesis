import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import matplotlib.ticker as ticker
import matplotlib.axes as axes
from scipy import optimize
from scipy.signal import argrelextrema


plt.rc('font', family='Helvetica')
x = np.linspace(0, 360, 943) # The smallest angle which translates to 1 mm distance is 0.38 degrees

#-------------FUNCTIONS----------------------------
def sinusoidal(x_vals, amp, phi, d):
    return amp * np.abs( np.sin(np.pi * (x_vals-phi)/180) ) + d
    
    
def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


def y_func(bins, vals, initial_guess):
    params, _ = optimize.curve_fit(sinusoidal, bins, vals, p0=initial_guess, maxfev=5000)
    y = sinusoidal(x, params[0], params[1], params[2])
    local_min = argrelextrema(y, np.less)[0]
    min_angles = np.round(x[local_min], 2)
    #minangle = np.round(x[np.argmin(y)], 2)
    return y, min_angles
    
    
def error(theo, exp):
    return np.round(np.abs((theo-exp)), 2)
    
    
def distance_dif(angle1, angle2):
    x1 = np.abs(np.tan((angle1-90)*np.pi/180))
    x2 = np.abs(np.tan((angle2-90)*np.pi/180))
    return np.round(15*np.abs(x1-x2), 2)
    

#-----------------DATA------------------------------
#Data for gammas
bins_gpr, vals_gpr =np.genfromtxt("S3A_Gammas_RadCurve.txt", unpack=True)
bins_gcr, vals_gcr =np.genfromtxt("S3B_Gammas_RadCurve.txt", unpack=True)

#Filtered data for neutrons
bins_npr, vals_npr =np.genfromtxt("S3A_Neutrons_RadCurve.txt", unpack=True)
bins_ncr, vals_ncr = np.genfromtxt("S3B_Neutrons_RadCurve.txt", unpack=True)

#Unfiltered data for neutrons
bins_npr_nf, vals_npr_nf = np.genfromtxt("S3A_Neutrons_RadCurve_NF.txt", unpack=True)
bins_ncr_nf, vals_ncr_nf = np.genfromtxt("S3B_Neutrons_RadCurve_NF.txt", unpack=True)

#Fits
y_gpr, mins_gpr = y_func(bins_gpr, vals_gpr,[250, 20, 400])
y_gcr, mins_gcr = y_func(bins_gcr, vals_gcr, [400, 0, 600])
y_npr_nf, mins_npr_nf = y_func(bins_npr_nf, vals_npr_nf, [115, 0, 60])
y_npr, mins_npr = y_func(bins_npr, vals_npr, [45, -20, 10])
y_ncr_nf, mins_ncr_nf = y_func(bins_ncr_nf, vals_ncr_nf, [100, 0, 50])
y_ncr, mins_ncr = y_func(bins_ncr, vals_ncr, [20, 0, 20])

exp_angles = np.array([mins_gpr[1]-90, mins_gcr[0]-90, mins_npr_nf[0]-90, mins_npr[0]-90, mins_ncr[1]-90, mins_ncr_nf[0]-90])

theo_angles = np.array([99.83, 95.71, 80.54, 80.54, 71.56, 71.56])
angle_errors = error(theo_angles, exp_angles)
dist_errors = distance_dif(theo_angles, exp_angles)

print('Angle errors: ', angle_errors)
print('Distance errors: ', dist_errors)

#--------------------GAMMA PLOT-------------------------------------
fig, ax1 = plt.subplots(1, 2, figsize=(22,10))
fig.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.9, wspace=0.25, hspace=0.1)
plt.suptitle('RadICAL curves - Gammas', fontsize=30, fontweight='bold')

ax1[0].set_title('Point source', fontsize=26)
ax1[0].scatter(bins_gpr, vals_gpr, label='Data', color='royalblue', s=15)
ax1[0].plot(x, y_gpr, linewidth=2, label='Fit: min at '+str(mins_gpr[0])+', '+str(mins_gpr[1])+'º', color='royalblue')#- Max pos = '+str(maxangle_gpr)+'º')

ax1[1].set_title('Continuous source', fontsize=26)
ax1[1].scatter(bins_gcr, vals_gcr, label='Data', color='olivedrab', s=15)
ax1[1].plot(x, y_gcr, linewidth=2, label='Fit: min at '+str(mins_gcr[0])+', '+str(mins_gcr[1])+'º', color='olivedrab') #- Max pos = '+str(maxangle_gcr)+'º')

ax1[0].set_ylabel('N events', fontweight='bold', fontsize=24)
ax1[0].tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1[0].tick_params(axis='both', which='minor', direction='in', length=5)
ax1[0].xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1[0].yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1[0].set_xlabel('Rotation angle (deg)', fontweight='bold', fontsize=24)
ax1[0].set_xlim(0, 360)
ax1[0].set_ylim(300, 800)
ax1[0].legend(fontsize=24, ncol=2)

ax1[1].set_ylabel('N events', fontweight='bold', fontsize=24)
ax1[1].tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1[1].tick_params(axis='both', which='minor', direction='in', length=5)
ax1[1].xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1[1].yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1[1].set_xlabel('Rotation angle (deg)', fontweight='bold', fontsize=24)
ax1[1].set_xlim(0, 360)
ax1[1].set_ylim(500, 1200)
ax1[1].legend(fontsize=24, ncol=2)
plt.savefig('S3_Gammas.png')
#plt.show()

#--------------------NEUTRON PLOT-------------------------
fig, ax1 = plt.subplots(1, 2, figsize=(22,10))
fig.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.9, wspace=0.25, hspace=0.1)
plt.suptitle('RadICAL curves - Neutrons', fontsize=30, fontweight='bold')

ax1[0].set_title('Point source', fontsize=26)
ax1[0].scatter(bins_npr_nf, vals_npr_nf, label='Data (Unfilt)', color='deepskyblue', s=15)
ax1[0].scatter(bins_npr, vals_npr, label='Data (Filt)', color='royalblue', s=15)
ax1[0].plot(x, y_npr_nf, linewidth=2, label='Fit: min at '+str(mins_npr_nf[0])+', '+str(mins_npr_nf[1])+'º', color='deepskyblue')
ax1[0].plot(x, y_npr, linewidth=2, label='Fit: min at '+str(mins_npr[0])+', '+str(mins_npr[1])+'º', color='royalblue')

ax1[1].set_title('Continuous source', fontsize=26)
ax1[1].scatter(bins_ncr_nf, vals_ncr_nf, label='Data (Unfilt)', color='yellowgreen', s=15)
ax1[1].scatter(bins_ncr, vals_ncr, label='Data (Filt)', color='olivedrab', s=15)
ax1[1].plot(x, y_ncr_nf, linewidth=2, label='Fit: min at '+str(mins_ncr_nf[0])+'º',  color='yellowgreen')
ax1[1].plot(x, y_ncr, linewidth=2, label='Fit: min at '+str(mins_ncr[0])+', '+str(mins_ncr[1])+'º', color='olivedrab')

ax1[0].set_ylabel('N events', fontweight='bold', fontsize=24)
ax1[0].tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1[0].tick_params(axis='both', which='minor', direction='in', length=5)
ax1[0].xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1[0].yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1[0].set_xlabel('Rotation angle (deg)', fontweight='bold', fontsize=24)
ax1[0].set_xlim(0, 360)
ax1[0].set_ylim(0, 200)
ax1[0].legend(fontsize=24, ncol=2)

ax1[1].set_ylabel('N events', fontweight='bold', fontsize=24)
ax1[1].tick_params(axis='both', which='major', labelsize=24, direction='in', length=10)
ax1[1].tick_params(axis='both', which='minor', direction='in', length=5)
ax1[1].xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1[1].yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1[1].set_xlabel('Rotation angle (deg)', fontweight='bold', fontsize=24)
ax1[1].set_xlim(0, 360)
ax1[1].set_ylim(0, 200)
ax1[1].legend(fontsize=24, ncol=2)
plt.savefig('S3_Neutrons.png')
