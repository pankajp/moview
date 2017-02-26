""" The main window of the application, MoViewWindow. """

from os.path import dirname, join, splitext

from qtpy import QtWidgets, QtGui, QtCore

from ..version import __version__
from ..molecule import Mol
from .plot_view import PlotView


class MoViewWindow(QtWidgets.QMainWindow):
    """ The main window of the application. """

    # Signal emitted when a new Molecule is loaded.
    mol_loaded = QtCore.Signal(Mol)

    def __init__(self):
        super(MoViewWindow, self).__init__()
        self._create_menus()
        self._create_central_widget()
        self._init_readers()
        self._default_dir = join(dirname(dirname(__file__)), 'examples')
        self._default_filename = join(self._default_dir, 'BaHfO3.xyz')
        self._mol = None
        self._open_default_file()

    @property
    def mol(self):
        return self._mol

    def _create_menus(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        open_action = file_menu.addAction(
            '&Open...', self.open, shortcut=QtGui.QKeySequence.Open)
        file_menu.addAction(
            '&Save As...', self.save_as, shortcut=QtGui.QKeySequence.Save)
        exit_action = file_menu.addAction(
            'E&xit', self.close, shortcut=QtGui.QKeySequence.Quit)
        help_menu = menubar.addMenu('&Help')
        about_menu = help_menu.addAction(
            '&About', self._about_dialog)
        # about_qt_menu = help_menu.addAction(
        #     'About &Qt', self._about_qt)

    def _create_central_widget(self):
        self.plot_view = PlotView(self)
        self.setCentralWidget(self.plot_view)
        self.mol_loaded.connect(self.plot_view.plot)

    def _create_dock_panes(self):
        pass

    def _init_readers(self):
        from ..io.xyz_reader import XYZReader
        self._readers = {
            XYZReader.ext: XYZReader
        }

    def _about_dialog(self):
        QtWidgets.QMessageBox.about(
            self, 'About MoView',
            """<p><emph>MoView ({})</emph> is a simple viewer for molecules
            using Matplotlib. It can load molecules from .xyz files.</p>

            <p>Copyright (C) 2017 Authors</p>

            <p>Licensed under MIT license
            <a href="https://opensource.org/licenses/MIT">
            https://opensource.org/licenses/MIT</a></p>
            """.format(__version__)
        )

    def _about_qt(self):
        QtWidgets.QApplication.instance().aboutQt()

    def _open_default_file(self):
        self.open_file(self._default_filename)

    def open(self):
        """ Show an open file dialog and open selected file. """
        filename = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open XYZ Coordinate file',
            directory=self._default_dir,
            filter='XYZ coordinate files (*.xyz)')[0]
        if filename:
            self.open_file(filename)

    def open_file(self, filename):
        """ Open the specified file. """
        reader = self._readers[splitext(filename)[-1]]()
        with open(filename) as f:
            mol = reader.read(f)
        self._mol = mol
        self.mol_loaded.emit(mol)
        self.setWindowFilePath(filename)

    def save_as(self):
        """ Save the currently loaded molecule prompting to select a file. """
        filename = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Save XYZ Coordinate file',
            directory=self._default_dir,
            filter='XYZ coordinate files (*.xyz)')[0]
        if filename:
            self.save_as_file(filename)

    def save_as_file(self, filename):
        """ Save the loaded molecule into specified filename. """
        reader = self._readers[splitext(filename)[-1]]()
        with open(filename, 'w') as f:
            reader.write(self.mol, f)


if __name__ == '__main__':
    qapp = QtWidgets.QApplication([])
    mw = MoViewWindow()
    mw.show()
    qapp.exec_()
