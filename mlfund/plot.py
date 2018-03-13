import warnings
import matplotlib.pyplot as plt
import numpy
import re

import sklearn.svm

from mpl_toolkits.mplot3d import axes3d, Axes3D

class ColorHelper(object):

    regex_hex_color = re.compile("#[0-9a-fA-F]{6}")

    @staticmethod
    def mix_alpha(rgb, alpha):
        if ColorHelper.regex_hex_color.match(rgb) is None:
            raise TypeError("Argument 'rgb' is not a hex color code. Expected format: #rrggbb")
        if alpha < 0:
            alpha = 0
        elif alpha > 1:
            alpha = 1
        i_r = int(round(int(rgb[1:3], 16) * (1 - alpha) + 255 * alpha))
        i_g = int(round(int(rgb[3:5], 16) * (1 - alpha) + 255 * alpha))
        i_b = int(round(int(rgb[5:7], 16) * (1 - alpha) + 255 * alpha))

        return '#' + format((i_r << 16) + (i_g << 8) + i_b, 'x')

class PlotBase(object):
    def __init__(self):
        self.palette = ['#0000FF', '#FF0000', '#00FF00', '#FFFF00', '#FF00FF', '#00FFFF', '#000000']
        for i in range(0, len(self.palette)):
            self.palette[i] = ColorHelper.mix_alpha(self.palette[i], 0.4)
            
    def legend(self):
        self.ax.legend()

    def grid(self):
        self.ax.grid(True)

    def show(self):
        plt.show()

    def save2Png(self, filename):
        plt.savefig(filename, format='png', dpi=144)

    def save2Eps(self, filename):
        plt.savefig(filename, format='eps', dpi=300)
        
    
class Plot3D(PlotBase):
    def __init__(self):
        PlotBase.__init__(self)
        self.fig = plt.figure()
        self.ax = Axes3D(self.fig)
        
    def scatter(self, X, y):
        c_idx = 0

        if not isinstance(X, numpy.ndarray):
            raise TypeError("Argument 'X' is not an instance of 'numpy.ndarray'")

        if X.shape[1] > 3:
            warnings.warn("Dimension of samples exceeds 3, only plot the first-3 dimension")
            
        for yk in set(y):
            if c_idx >= len(self.palette):
                warnings.warn("Categories number exceeds %d, only plot data of the first-%d classes" % (c_idx, len(self.palette)))
                return

            Xk = X[y == yk, :]
            self.ax.scatter(Xk[:, 0], Xk[:, 1],Xk[:,2], c=self.palette[c_idx], s=20, label=('Class %d' % (c_idx+1)), edgecolors='none')

            c_idx = c_idx + 1

class Plot2D(PlotBase):
    def __init__(self):
        PlotBase.__init__(self)
        self.fig, self.ax = plt.subplots(figsize=(10,8))

    def scatter(self, X, y):
        c_idx = 0

        if not isinstance(X, numpy.ndarray):
            raise TypeError("Argument 'X' is not an instance of 'numpy.ndarray'")

        if X.shape[1] > 2:
            warnings.warn("Dimension of samples exceeds 2, only plot the first-2 dimension")

        for yk in set(y):
            if c_idx >= len(self.palette):
                warnings.warn("Categories number exceeds %d, only plot data of the first-%d classes" % (c_idx, len(self.palette)))
                return

            Xk = X[y == yk, :]
            self.ax.scatter(Xk[:, 0], Xk[:, 1], c=self.palette[c_idx], s=20, label=('Class %d' % (c_idx+1)), edgecolors='none')

            c_idx = c_idx + 1

    def scatterCSVC(self, clf):
        if isinstance(clf, sklearn.svm.SVC):
            indices_relaxed = (clf.C - numpy.abs(clf.dual_coef_) < 1e-6).ravel()
            indices_sv = numpy.invert(indices_relaxed).ravel()

            self.ax.scatter(clf.support_vectors_[indices_relaxed,0], clf.support_vectors_[indices_relaxed,1], s=75, marker='*', facecolors='none', edgecolors='r')
            self.ax.scatter(clf.support_vectors_[indices_sv,0], clf.support_vectors_[indices_sv,1], s=100, facecolors='none', edgecolors='k')

    def classifierContour(self, X, y, clf):
        if clf is None or ( clf is not None and type(clf.predict) is 'function'):
            raise TypeError("Argument 'clf' is not a valid classifier")

        axis0_grid, axis1_grid = self.__computeAxisGridRange(X, y)
        
        Z = clf.predict(numpy.c_[axis0_grid.ravel(), axis1_grid.ravel()])
        Z = Z.reshape(axis0_grid.shape)

        plt.contour(axis0_grid, axis1_grid, Z, cmap=plt.cm.Set1, vmin=-1, vmax=0, linewidths=1)

    def classifierContourF(self, X, y, clf):
        if clf is None or ( clf is not None and type(clf.decision_function) is 'function'):
            raise TypeError("Argument 'clf' is not a valid classifier")

        axis0_grid, axis1_grid = self.__computeAxisGridRange(X, y)
        
        Z = clf.decision_function(numpy.c_[axis0_grid.ravel(), axis1_grid.ravel()])
        Z = Z.reshape(axis0_grid.shape)

        plt.contourf(axis0_grid, axis1_grid, Z, cmap=plt.cm.PuBu_r, linewidths=1)
    
    def line(self, x, y):
        
        min_x, max_x = min(x), max(x)
        min_y, max_y = min(y), max(y)
        
        line = plt.Line2D(x, y)
        self.ax.add_line(line)
        self.ax.set_xlim(min_x, max_x)
        self.ax.set_ylim(min_y, max_y)
        
    def __computeAxisGridRange(self, X, y):
        axis0_min, axis0_max = min(X[:, 0]), max(X[:, 0])
        axis1_min, axis1_max = min(X[:, 1]), max(X[:, 1])
        
        axis0_min = axis0_min - 1
        axis1_min = axis1_min - 1
        axis0_max = axis0_max + 1
        axis1_max = axis1_max + 1

        axis0_grid, axis1_grid = numpy.meshgrid(numpy.arange(axis0_min, axis0_max, 0.01), numpy.arange(axis1_min, axis1_max, 0.01))
        
        return axis0_grid, axis1_grid