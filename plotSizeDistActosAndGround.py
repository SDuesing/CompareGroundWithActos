import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, ticker
from NRowAverage import avg
import sys

f = sys.argv[1]
#print(f)
fileType = sys.argv[2]

table = np.genfromtxt(f, delimiter="\t", skip_header=False)
prefix = f.split(".")[0]
#print(table)
if fileType == "SMPS":
    diameter = table[0, 4:]
    times = table[1::2, 0]
    concentrations = table[1::2, 4:]
    numberOfScans = concentrations.shape[0]

    concentrations[concentrations <= 0] = np.nan
    z = concentrations.transpose()
    print(z)

    plt.figure(figsize=(9, 4.5), dpi=300)
    levels = np.logspace(np.log10(np.nanmin(z)), np.log10(np.nanmax(z)), 1000)
    locator = ticker.LogLocator(base=10)
    plt.contourf(times, diameter, z, levels, locator=locator, cmap=cm.jet)
    plt.colorbar(format='%.e', ticks=locator, label="dN/dlogDp")
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
    plt.contourf(times, diameter, z, 100, cmap=cm.jet)
    plt.colorbar(format='%.e', label="dN/dlogDp")
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
    table = avg(table[1:, 0:], N=20)
    times = table[0:, 0]
    concentrations = table[0:, 1:]
    numberOfScans = concentrations.shape[0]

    concentrations[concentrations <= 0] = np.nan
    z = concentrations.transpose()
    print(z)

    plt.figure(figsize=(9, 4.5), dpi=300)
    levels = np.logspace(np.log10(np.nanmin(z)), np.log10(np.nanmax(z)), 1000)
    locator = ticker.LogLocator(base=10)
    plt.contourf(times, diameter, z, levels, locator=locator, cmap=cm.jet)
    plt.colorbar(format='%.e', ticks=locator, label="dN/dlogDp")
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
    plt.contourf(times, diameter, z, 100,  cmap=cm.jet)
    plt.colorbar(format='%.e', label="dN/dlogDp")
    plt.ylim((np.nanmin(diameter), np.nanmax(diameter)))
    plt.yscale('log')
    plt.ylabel("diameter [nm]")
    plt.xlabel("time [seconds]")
    plt.grid()
    # plt.show()
    plt.savefig(prefix + "_contour.png")
    plt.close()



