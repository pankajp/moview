""" A Plot view for the molecule. """

from qtpy import PYQT5
from qtpy.QtWidgets import QWidget, QVBoxLayout

from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
if PYQT5:
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
else:
    from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg, NavigationToolbar2QT


class MoViewCanvas(FigureCanvasQTAgg):
    """ Matplotlib Canvas to plot the Mol. """
    def __init__(self, parent=None):
        fig = Figure()
        super(MoViewCanvas, self).__init__(fig)
        self.axes = fig.add_subplot(111, projection='3d')
        self.setParent(parent)

    def plot_mol(self, mol):
        """ Plot the given Mol into the canvas. """
        axes = self.axes
        axes.clear()
        if mol is None:
            return
        axes.set_title(mol.name)
        axes.grid(False)
        atoms = mol.atoms
        atom_idx = {}
        coords = mol.coords
        xs = []
        ys = []
        zs = []
        s = []
        c = []
        for i, atom in enumerate(atoms):
            x, y, z = mol.coords[i]
            xs.append(x)
            ys.append(y)
            zs.append(z)
            s.append(500)
            c.append(atom_idx.setdefault(atom, len(atom_idx)))
            axes.text(x, y, z, atom)
        axes.scatter(xs, ys, zs, s=s, c=c)
        self.draw_idle()


class PlotView(QWidget):
    """ A QWidget to contain the mpl plot and toolbar. """
    def __init__(self, parent, show_toolbar=False):
        super(PlotView, self).__init__(parent)
        self.canvas = MoViewCanvas(self)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        if not show_toolbar:
            self.toolbar.hide()
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self, mol):
        self.canvas.plot_mol(mol)


if __name__ == '__main__':
    from moview.utils import get_qapp
    qapp = get_qapp()
    pv = PlotView(None)
    pv.show()
    qapp.exec_()
