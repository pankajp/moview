""" The main window of the application, MoViewWindow. """

from os.path import dirname, join

from qtpy import QtWidgets, QtGui

from .plot_view import PlotView


class MoViewWindow(QtWidgets.QMainWindow):
    """ The main window of the application. """

    def __init__(self):
        super(MoViewWindow, self).__init__(
            windowTitle='MoView',
        )
        self._create_menus()
        self._create_central_widget()
        self._default_dir = join(dirname(__file__), 'examples')

    def _create_menus(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        open_action = file_menu.addAction('&Open...', self.open, shortcut=QtGui.QKeySequence.Open)
        file_menu.addAction('&Save As...', self.save_as, shortcut=QtGui.QKeySequence.Save)
        exit_action = file_menu.addAction('E&xit', self.close, shortcut=QtGui.QKeySequence.Quit)

    def _create_central_widget(self):
        self.plot_view = PlotView(self)
        self.setCentralWidget(self.plot_view)

    def _create_dock_panes(self):
        pass

    def open(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open XYZ Coordinate file',
            directory=self._default_dir,
            filter='XYZ coordinate files (*.xyz)')[0]

        print(filename)

    def save_as(self):
        pass


if __name__ == '__main__':
    qapp = QtWidgets.QApplication([])
    mw = MoViewWindow()
    mw.show()
    qapp.exec_()
