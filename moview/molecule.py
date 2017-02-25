""" Molecule definition. """

class Mol(object):
    """ Represents a molecule with atoms and coordinates. """
    def __init__(self, atoms, coords, name=''):
        self.atoms = atoms
        self.coords = coords
        self.name = name
