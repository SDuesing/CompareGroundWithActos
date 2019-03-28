import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, ticker, colors
from matplotlib.colors import LogNorm

f = "20150628_ground_aps+smps_merged.dat"

table = np.genfromtxt(f, delimiter="\t")

table = table[:, 0:76]
times = table[1::2, 0]
diameter = table[0, 4:]
print(diameter)
concentrations = table[1::2, 4:]
numberOfScans = concentrations.shape[0]

# for i in range(times.size):
#     plt.semilogx(diameter, concentrations[i, :])
#     plt.title('number size distribution')
#     plt.grid(True)
#     plt.savefig(str(i)+".png")
#     plt.close()



# contourplot
concentrations[concentrations <= 0] = np.nan
z = concentrations.transpose()
print(z)

plt.figure(figsize=(4.5, 9), dpi=300)
levels = np.logspace(np.log10(np.nanmin(z)), np.log10(np.nanmax(z)), 1000)
locator = ticker.LogLocator(base=10)

plt.contourf(times, diameter, z, levels, locator=locator, cmap = cm.jet)
plt.colorbar(plot, format='%.e', ticks=locator)
plt.ylim((10, 1e4))
plt.yscale('log')
plt.ylabel("diameter [nm]")
plt.xlabel("time [seconds")
plt.savefig("20150628_ground_contour.png")
