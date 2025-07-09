from abc import ABC

class BusinessObject(ABC):
    """Gemeinsame Basisklasse aller 
    in diesem Projekt für die Umsetzung 
    des Fachkonzepts relevanten Klassen.

    Zentrales Merkmal ist, dass jedes 
    BusinessObject eine Nummer besitzt, 
    die man in
    einer relationalen Datenbank auch als
      Primärschlüssel bezeichnen würde.
    """
    def __init__(self):
        self._id=0
        self._name=""
    
    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

# Die Datei BusinessObject.py definiert eine abstrakte Basisklasse für alle fachlich relevanten Objekte deines Projekts. Sie sorgt dafür, dass jedes BusinessObject eine eindeutige ID besitzt, die wie ein Primärschlüssel in der Datenbank funktioniert.

# Erklärung der wichtigsten Teile:

# from abc import ABC:
# Das Modul abc steht für "Abstract Base Classes" (abstrakte Basisklassen).
# ABC ist eine spezielle Basisklasse, die verwendet wird, um abstrakte Klassen in Python zu definieren.
# Eine abstrakte Klasse kann nicht direkt instanziiert werden, sondern dient als Vorlage für andere Klassen.

# class BusinessObject(ABC):
# BusinessObject ist eine abstrakte Basisklasse.
# Alle Klassen, die von BusinessObject erben, bekommen automatisch die ID-Funktionalität.

# __init__:
# Konstruktor, der das Attribut _id mit dem Wert 0 initialisiert.

# get_id und set_id:
# Methoden, um die ID auszulesen und zu setzen.

# Zusammengefasst:
# Mit dieser Datei stellst du sicher, dass alle Business-Objekte in deinem Projekt eine eindeutige ID haben und von einer gemeinsamen Basisklasse erben. Das erleichtert die Verwaltung und sorgt für einheitliche Schnittstellen.
# ABC sorgt dafür, dass BusinessObject als abstrakte Klasse behandelt wird und nicht direkt verwendet werden sollte, sondern nur als Basis für andere Klassen dient