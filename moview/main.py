""" Main module to start the application. """

from os.path import dirname, join

from moview import __version__
from moview.ui.app import get_qapp


def main():
    qapp = get_qapp()
    from moview.ui.mainwindow import MoViewWindow
    w = MoViewWindow()
    w.show()
    qapp.exec_()


if __name__ == '__main__':
    main()
