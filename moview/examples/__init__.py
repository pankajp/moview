import glob
from os.path import abspath, dirname, join

example_dir = dirname(abspath(__file__))
example_files = glob.glob(join(example_dir, '*.xyz'))
