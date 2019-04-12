import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, ticker
from NRowAverage import avg
import sys

f = "20150628_ground_aps+smps_merged.dat"  # sys.argv[1]
#print(f)
fileType = "OPSS"  # sys.argv[2]

table = np.genfromtxt(f, delimiter="\t", skip_header=False)
prefix = f.split(".")[0]
print(table)
if fileType == "SMPS":
    diameter = table[0, 4:]
    times = table[1::2, 0]
    concentrations = table[1::2, 4:]
    numberOfScans = concentrations.shape[0]

    concentrations[concentrations <= 0] = np.nan
    z = np.ma.array(concentrations.transpose(), mask=np.isnan(concentrations.transpose()))
    print(z)

    plt.figure(figsize=(9, 4.5), dpi=300)
    levels = np.logspace(np.log10(np.nanmin(z)), np.log10(np.nanmax(z)), 1000)
    locator = ticker.LogLocator(base=10)
    cmap = cm.gist_ncar
    cmap.set_bad('gray', 1.)
    plt.contourf(times, diameter, z, levels, locator=locator, cmap=cmap, extend="both")
    plt.colorbar(format='%.e', ticks=locator, label=r"$dN\/dlogD_{p} [cm^{-3}]$")
    plt.ylim((np.nanmin(diameter), np.nanmax(diameter)))
    plt.yscale('log')
    plt.ylabel("diameter [nm]")
    plt.xlabel("time [seconds]")
    plt.grid()
    # plt.show()
    plt.savefig(prefix + "_contour_log.png")
    plt.close()

    plt.figure(figsize=(9, 4.5), dpi=300)
    # levels = np.logspace(np.log10(np.nanmin(z)), np.log10(np.nanmax(z)), 1000)
    # locator = ticker.LogLocator(base=10)
    cmap = cm.gist_ncar
    plt.gca().set_facecolor("gray")
    plt.contourf(times, diameter, z, 100, cmap=cmap, extend="both")
    plt.colorbar(format='%.e', label=r"$dN\/dlogD_{p} [cm^{-3}]$")
    plt.ylim((np.nanmin(diameter), np.nanmax(diameter)))
    plt.yscale('log')
    plt.ylabel("diameter [nm]")
    plt.xlabel("time [seconds]")
    plt.grid()
    # plt.show()
    plt.savefig(prefix + "_contour.png")
    plt.close()


# for i in range(times.size):
#     plt.semilogx(diameter, concentrations[i, :])
#     plt.title('number size distribution')
#     plt.grid(True)
#     plt.savefig(str(i)+".png")
#     plt.close()
# contourplot Christian OPSS Size Format

elif fileType == "OPSS":
    diameter = table[0, 1:]
    #table = avg(table[1:, 0:], N=1)
    times = table[0:, 0]
    concentrations = table[0:, 1:]
    numberOfScans = concentrations.shape[0]

    concentrations[concentrations <= 0] = np.nan
    #concentrations[concentrations > 1e4] = np.nan
    z = np.ma.array(concentrations.transpose(), mask=np.isnan(concentrations.transpose()))
    #  print(z)

    plt.figure(figsize=(9, 4.5), dpi=300)
    levels = np.logspace(np.log10(np.nanmin(z)), np.log10(np.nanmax(z)), 1000)
    locator = ticker.LogLocator(base=10)
    cmap = cm.gist_rainbow
    plt.contourf(times, diameter, z, levels, locator=locator, cmap=cmap, extend="both")
    plt.gca().set_facecolor("gray")
    plt.colorbar(format='%.e', ticks=locator, label=r"$dN\/dlogD_{p} [cm^{-3}]$")
    plt.ylim((np.nanmin(diameter), np.nanmax(diameter)))
    plt.yscale('log')
    plt.ylabel("diameter [nm]")
    plt.xlabel("time [seconds]")
    plt.grid()
    # plt.show()
    plt.savefig(prefix + "_contour_log.png")
    plt.close()

    plt.figure(figsize=(9, 4.5), dpi=300)
    #levels = np.logspace(np.log10(np.nanmin(z)), np.log10(np.nanmax(z)), 1000)
    #locator = ticker.LogLocator(base=10)
    cmap = cm.gist_rainbow
    #plt.gca().set_facecolor("gray")
    plt.contourf(times, diameter, z, 1000,  cmap=cmap, extend="both")

    plt.colorbar(format='%.e', label=r"$dN\/dlogD_{p} [cm^{-3}]$")
    plt.ylim((np.nanmin(diameter), np.nanmax(diameter)))
    plt.yscale('log')
    plt.ylabel("diameter [nm]")
    plt.xlabel("time [seconds]")
    plt.grid()
    # plt.show()
    plt.savefig(prefix + "_contour.png")
    plt.close()




# diameter = table[0, 1:]
# table = avg(table[1:, 0:], N=10)
# times = table[0:, 0]
# concentrations = table[0:, 1:]
# concentrations[concentrations <= 0] = np.nan
#
# times, diameter = np.meshgrid(times, diameter)
#
# # Mask the bad data:
# z = np.ma.array(concentrations, mask=np.isnan(concentrations)).transpose()
#
# # Get the colormap and set the under and bad colors
# colMap = cm.rainbow
# colMap.set_over(color='white')
# colMap.set_under(color='black')
#
# # Create the contour plot
# plt.figure(figsize=(16, 4))
#
# plt.gca().set_facecolor("black")
# levels = np.logspace(np.log10(np.nanmin(z)), np.log10(np.nanmax(z)), 1000)
# locator = ticker.LogLocator(base=10)
# plt.contourf(times, diameter, z, levels, locator=locator, cmap=colMap, extend="both")
# plt.gca().set_facecolor("gray")
# plt.colorbar(format='%.e', ticks=locator, label="dN/dlogDp")

# plt.yscale('log')
# plt.ylabel("diameter [nm]")
# plt.xlabel("time [seconds]")
# plt.tight_layout()
# plt.show()
#
#
#
# colMap = cm.gist_ncar
# colMap.set_over(color='white')
# colMap.set_under(color='black')
#
# # Create the contour plot
# plt.figure(figsize=(16, 4))
#
# plt.gca().set_facecolor("black")
#
# # locator = ticker.LogLocator(base=10)
# plt.contourf(times, diameter, z, 1000, cmap=colMap, extend="both")
# plt.gca().set_facecolor("gray")
# plt.colorbar(format='%.e', label="dN/dlogDp")
#
# plt.yscale('log')
# plt.ylabel("diameter [nm]")
# plt.xlabel("time [seconds]")
# plt.tight_layout()
# plt.show()
