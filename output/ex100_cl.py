import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/aizhan.akh/Documents/Projects/class_public/output/ex100_cl.dat', '/Users/aizhan.akh/Documents/Projects/class_public/output/ex100_cl_lensed.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['ex100_cl', 'ex100_cl_lensed']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = ['TT', 'EE', 'TE', 'BB', 'phiphi', 'TPhi', 'Ephi']
tex_names = ['TT', 'EE', 'TE', 'BB', 'phiphi', 'TPhi', 'Ephi']
x_axis = 'l'
ylim = []
xlim = []
ax.plot(curve[:, 0], curve[:, 1])
ax.plot(curve[:, 0], curve[:, 2])
ax.plot(curve[:, 0], curve[:, 3])
ax.plot(curve[:, 0], curve[:, 4])
ax.plot(curve[:, 0], curve[:, 5])
ax.plot(curve[:, 0], curve[:, 6])
ax.plot(curve[:, 0], curve[:, 7])

index, curve = 1, data[1]
y_axis = ['TT', 'EE', 'TE', 'BB', 'phiphi', 'TPhi', 'Ephi']
tex_names = ['TT', 'EE', 'TE', 'BB', 'phiphi', 'TPhi', 'Ephi']
x_axis = 'l'
ylim = []
xlim = []
ax.plot(curve[:, 0], curve[:, 1])
ax.plot(curve[:, 0], curve[:, 2])
ax.plot(curve[:, 0], curve[:, 3])
ax.plot(curve[:, 0], curve[:, 4])
ax.plot(curve[:, 0], curve[:, 5])
ax.plot(curve[:, 0], curve[:, 6])
ax.plot(curve[:, 0], curve[:, 7])

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
plt.show()