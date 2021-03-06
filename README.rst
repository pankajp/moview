MoView
======

``Moview`` is a simple application to view XYZ coordinate files to show
the molecule as positions of the various atoms in it in a 3D plot view
using Matplotlib. It uses Qt as the windowing toolkit using either
PyQt5, PyQt4 or PySide as the Python bindings.

The setup script creates a gui entry point ``moview`` which starts the
application.


Requirements
------------

- Matplotlib
- qtpy (tested with PyQt5 backend)
- periodictable


Code Structure
--------------

The code of the application is structured as follows::

    moview
    ├── COPYING                     License
    ├── README.rst                  README
    ├── moview
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── examples                Example files
    │   │   ├── __init__.py
    │   │   ├── BaHfO3.xyz
    │   │   └── benzene.xyz
    │   ├── io                      File I/O code
    │   │   ├── __init__.py
    │   │   └── xyz_reader.py       XYZ format reader/writer
    │   ├── main.py                 Main application code
    │   ├── molecule.py             Simple Molecule model
    │   ├── tests                   Tests
    │   │   ├── __init__.py
    │   │   └── test_xyz_reader.py
    │   ├── ui                      GUI code
    │   │   ├── __init__.py
    │   │   ├── app.py              Create/get QApplication
    │   │   ├── mainwindow.py       Main window of the application
    │   │   ├── plot_view.py        Matplotlib molecule plot widget
    │   │   └── properties_pane.py  Properties dockpane
    │   └── version.py              Version info of `MoView`
    ├── requirements.txt            Pip requirements
    └── setup.py                    Setup script


Usage
-----

Start the application with the following command::

    moview

or to run it from the source directory without installing::

    python -m moview
