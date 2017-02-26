""" Utility functions """

from os.path import dirname, join
import sys

from moview import __version__


def get_qapp():
    """ Return a QApplication instance, creating one if needed. """
    from qtpy.QtWidgets import QApplication
    qapp = QApplication.instance()
    if qapp:
        return qapp
    qapp = QApplication(sys.argv)
    qapp.setApplicationName('MoView')
    qapp.setApplicationDisplayName('MoView')
    qapp.setApplicationVersion(__version__)
    return qapp
