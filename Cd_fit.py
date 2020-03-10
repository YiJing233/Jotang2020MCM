import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x = [1.0, 2.0, 4.0, 8.0]
laminar = [1.2, 0.60, 0.35, 0.25]
turbulent = [0.3, 0.2, 0.15, 0.1]
x_new = np.linspace(1, 8, 1000)
Interpolations = ['linear', 'zero', 'cubic', 'quadratic', 'slinear']
# laminar as the y_data
plt.xlabel(u'Long axis / short axis')
plt.ylabel(u'Cd in laminar')
tck = interpolate.splrep(x, laminar)
plt.plot(x, laminar, "o",  label=u"origin data")
for mode in Interpolations:
    plt.plot(x_new, interpolate.interp1d(x, laminar, kind=mode)(x_new), label="{} interpolation".format(mode))
plt.plot(x_new, interpolate.splev(x_new, tck), label=u"B-spline interpolation")
plt.legend()
plt.show()
# turbulent as the y_data
plt.xlabel(u'Long axis / short axis')
plt.ylabel(u'Cd in turbulent')
tck = interpolate.splrep(x, turbulent)
plt.plot(x, turbulent, "o",  label=u"origin data")
for mode in Interpolations:
    plt.plot(x_new, interpolate.interp1d(x, turbulent, kind=mode)(x_new), label="{} interpolation".format(mode))
plt.plot(x_new, interpolate.splev(x_new, tck), label=u"B-spline interpolation")
plt.legend()
plt.show()
