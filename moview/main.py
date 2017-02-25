""" Main module to start the application. """

from moview import __version__

def get_qapp():
    from qtpy.QtWidgets import QApplication
    qapp = QApplication([])
    qapp.setApplicationName('MoView')
    qapp.setApplicationVersion(__version__)
    return qapp

def main():
    qapp = get_qapp()
    from moview.ui.mainwindow import MoViewWindow
    w = MoViewWindow()
    w.show()
    qapp.exec_()


if __name__ == '__main__':
    main()
