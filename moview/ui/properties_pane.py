""" List some properties of Mol. """

from collections import OrderedDict, Counter

from periodictable import formula
from qtpy.QtWidgets import QDockWidget, QTextBrowser


class PropertiesPane(QDockWidget):
    """ Simple text widget to display molecule properties. """

    def __init__(self, parent):
        super(PropertiesPane, self).__init__(parent)
        self.setWindowTitle('Properties')
        self._text_widget = QTextBrowser(self)
        self.setWidget(self._text_widget)

    def set_mol(self, mol):
        """ Set the Mol to display properties for. """
        properties = self._get_properties(mol)
        prop_rows = ['<tr><td>{}: </td><td>{}</td></tr>'.format(*p)
                     for p in properties.items()]
        html = '<table>' + '\n'.join(prop_rows) + '</table>'
        self._text_widget.setHtml(html)

    def _get_properties(self, mol):
        properties = OrderedDict()
        properties['Name'] = mol.name
        properties['Number of atoms'] = len(mol.atoms)

        atom_counts = Counter(mol.atoms)
        chem_formula = ''
        for atom, count in sorted(atom_counts.items()):
            chem_formula += atom
            if count > 1:
                chem_formula += str(count)
        properties['Chemical Formula'] = chem_formula

        mol_formula = formula(chem_formula)
        properties['Molecular Mass'] = mol_formula.mass
        mass_composition = {str(a):mass
                            for a, mass in mol_formula.mass_fraction.items()}
        properties['Mass Composition'] = '<br>'.join([
            '{0}: {1:.2f}%'.format(p[0], p[1]*100)
            for p in sorted(mass_composition.items())])
        return properties
