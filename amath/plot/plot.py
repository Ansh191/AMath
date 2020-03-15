import matplotlib.pyplot as plt
import numpy as np


def plot(f, xmin, xmax, *, plot_points=100, xlim=None, ylim=None, legend=False, size=6):
    x = np.linspace(xmin, xmax, plot_points)

    _plot(f, x, legend, '-', size=size)

    if ylim is not None:
        plt.ylim(ylim)
    if xlim is not None:
        plt.xlim(xlim)
    if legend:
        plt.legend(loc="upper left")
    plt.show()


def discrete_plot(f, xmin, xmax, step=1, *, xlim=None, ylim=None, legend=False, size=6):
    x = np.arange(xmin, xmax, step)

    _plot(f, x, legend, 'o', size=size)

    if ylim is not None:
        plt.ylim(ylim)
    if xlim is not None:
        plt.xlim(xlim)
    if legend:
        plt.legend(loc="upper left")
    plt.show()


def _plot(f, x, legend, style, size):
    if type(f) not in [list, tuple, set]:
        label = legend if legend else f.__name__
        y = np.array(list(map(f, x)))
        plt.plot(x, y, style, markersize=size, label=label)
    else:
        labels = _get_labels(f, legend)
        for i in range(len(f)):
            y = np.array(list(map(f[i], x)))
            plt.plot(x, y, style, markersize=size, label=labels[i])


def _get_labels(f, legend):
    labels = [func.__name__ for func in f]
    if type(legend) == [list, tuple, set]:
        for i in range(len(legend)):
            labels[i] = legend[i]
    return labels
