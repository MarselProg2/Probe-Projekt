from .BusinessObject import BusinessObject

class Studi(BusinessObject):

    def __init__(self):
        super().__init__()
        self._matrikelnummer = 0
        self._studiengang = ""
    
    def get_matrikelnummer(self):
        return self._matrikelnummer
    def set_matrikelnummer(self, matrikelnummer):
        self._matrikelnummer = matrikelnummer

marsel=Studi()
marsel.set_matrikelnummer(123456)

print(marsel.get_matrikelnummer())