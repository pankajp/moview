""" Molecule definition. """

class Mol(object):
    """ Represents a molecule with atoms and coordinates.
    
    Attributes:
     - name: str: name of the molecule
     - atoms: list(str): list of symbols of Atoms contained in the molecule
     - coords: list([x,y,z]): list of x,y,z coordinate tuples for each
        atom in the order listed in `atoms` attribute
    """
    def __init__(self, atoms, coords, name=''):
        self.atoms = atoms
        self.coords = coords
        self.name = name
