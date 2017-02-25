""" Main module to start the application. """

def main():
    from qtpy.QtWidgets import QApplication
    qapp = QApplication([])
    from moview.mainwindow import MainWindow
    w = MainWindow()
    qapp.exec_()


if __name__ == '__main__':
    main()
