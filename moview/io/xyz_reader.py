""" An XYZ coordinate file reader. """

class XYZReader(object):
    """ XYZ Coordinate file reader. """

    def read(self, file):
        """ Read the given file object into a new `Mol` instance. """
        num_atoms = int(file.readline())
        title = file.readline().strip()
        atoms = []
        coords = []
        for line in file:
            atoms, x, y, z = line.split()
            atoms.append(atom)
            coords.append((float(i) for i in (x, y, z)))
        return Mol(atoms, coords, title)

    def write(self, mol, file):
        """ Write the given `Mol` instance to the file object. """
        atoms = mol.atoms
        coords = mol.coords
        file.write('%s\n%s\n' % (len(atoms), mol.name))
        for i in xrange(atoms):
            file.write('%{0} %{1[0]} %{1[1]} %{1[2]}\n'.format(
                atoms[i], coords[i]))
