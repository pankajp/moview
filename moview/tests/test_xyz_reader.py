import unittest

import os
from os.path import join
import tempfile

from moview.utils import get_example_dir
from moview.io.xyz_reader import XYZReader
from moview.molecule import Mol


class TestXYZReader(unittest.TestCase):
    def setUp(self):
        self.example_file = join(get_example_dir(), 'benzene.xyz')
        self.reader = XYZReader()

    def get_water_mol(self):
        atoms = ['O', 'H', 'H']
        coords = [[0, 0, 0],
                  [0.757, 0.586, 0],
                  [-0.757, 0.586, 0]]
        return Mol(atoms, coords, 'Water')

    def assert_mol_equal(self, mol1, mol2, check_name=True):
        if check_name:
            self.assertEqual(mol1.name, mol2.name)
        self.assertListEqual(mol1.atoms, mol2.atoms)
        for i in xrange(len(mol1.coords)):
            coords1 = mol1.coords[i]
            coords2 = mol2.coords[i]
            for axis in xrange(3):
                self.assertAlmostEqual(coords1[axis], coords2[axis])

    def test_read(self):
        with open(self.example_file) as f:
            mol = self.reader.read(f)
        self.assertEqual(mol.name, 'Benzene')
        self.assertEqual(len(mol.atoms), 12)
        self.assertListEqual(mol.atoms, ['C', 'H'] * 6)

    def test_write(self):
        # Given
        mol = self.get_water_mol()
        atoms = mol.atoms
        coords = mol.coords

        # When
        with tempfile.NamedTemporaryFile(prefix='moview_reader-',
                                         delete=False) as f:
            self.addCleanup(os.remove, f.name)
            self.reader.write(mol, f)

        # Then
        with open(f.name) as f:
            self.assertEqual(f.readline().strip(), '3')
            self.assertEqual(f.readline().strip(), 'Water')
            for i in range(3):
                line = f.readline().strip()
                atom, x, y, z = line.strip().split()
                self.assertEqual(atom, atoms[i])
                self.assertAlmostEqual(float(x), coords[i][0])
                self.assertAlmostEqual(float(y), coords[i][1])
                self.assertAlmostEqual(float(z), coords[i][2])

        with open(f.name) as f:
            mol2 = self.reader.read(f)
        self.assert_mol_equal(mol, mol2)


if __name__ == '__main__':
    unittest.main()
