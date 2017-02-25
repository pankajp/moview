from setuptools import find_packages, setup

from moview import __version__

with open('requirements.txt') as req_file:
    install_requires = req_file.read().splitlines()

setup(
    name="MoView",
    version=__version__,

    packages=find_packages(),
    package_data={
        # Include example xyz files
        '': ['*.xyz'],
    },
    entry_points="""
        [gui_scripts]
        moview = moview.main:main
        """,

    author="Pankaj Pandey",
    author_email="pankaj86@gmail.com",
    description="Simple molecule viewer using matplotlib",
    license="MIT",
    keywords="matplotlib plot molecule chemistry",
    install_requires=install_requires,
    url="http://github.com/pankajp/moview/",
)
