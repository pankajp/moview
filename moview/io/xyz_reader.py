""" An XYZ coordinate file reader. """

from moview.molecule import Mol


class XYZReader(object):
    """ XYZ Coordinate file reader. """

    ext = '.xyz'

    def read(self, file):
        """ Read the given file object into a new `Mol` instance. """
        num_atoms = int(file.readline())
        title = file.readline().strip()
        atoms = []
        coords = []
        for i in range(num_atoms):
            line = file.readline()
            atom, x, y, z = line.strip().split()
            atoms.append(atom)
            coords.append([float(i) for i in (x, y, z)])
        return Mol(atoms, coords, title)

    def write(self, mol, file):
        """ Write the given `Mol` instance to the file object. """
        atoms = mol.atoms
        coords = mol.coords
        file.write('%d\n%s\n' % (len(atoms), mol.name))
        for i, atom in enumerate(atoms):
            file.write('{0:5s} {1[0]:10.5f} {1[1]:10.5f} {1[2]:10.5f}\n'.format(
                atom, coords[i]))
