
Erstellen Sie eine kleine Webanwendung zur Verwaltung von Personen. Die Architektur soll sich am Beispielprojekt orientieren und folgende Anforderungen erfüllen:

**Aufgabenstellung:**


Es soll eine abstrakte Basisklasse `BusinessObject` geben, von der alle fachlich relevanten Klassen erben. Jedes BusinessObject besitzt eine eindeutige ID (wie ein Primärschlüssel in der Datenbank).

Von `BusinessObject` erbt die Klasse `Person`. Von `Person` wiederum erben die Klassen `Dozent` und `Studi` (Student). Die Anwendung soll die Verwaltung beider Personentypen ermöglichen.

Die Anforderungen im Detail:


1. Backend (z.B. Python mit Flask/Django):


- Implementieren Sie eine REST-API.
- Speichern Sie die Daten in einer relationalen Datenbank (z.B. SQLite, MySQL oder PostgreSQL).
- Verwenden Sie das Konzept der Business Objects (BOs) und Mapper:
  - Erstellen Sie eine abstrakte Basisklasse `BusinessObject` mit Attribut: ID (und passenden Getter/Setter-Methoden).
  - Erstellen Sie eine Klasse `PersonBO`, die von `BusinessObject` erbt und das Attribut Name besitzt.
  - Erstellen Sie die abgeleiteten Klassen `DozentBO` (mit Zusatzattribut: Fachgebiet) und `StudiBO` (mit Zusatzattributen: Matrikelnummer, Studiengang), die beide von `PersonBO` erben.
  - Erstellen Sie entsprechende Mapper-Klassen (`PersonMapper`, `DozentMapper`, `StudiMapper`), die für das Speichern, Laden, Aktualisieren und Löschen der jeweiligen Objekte in der Datenbank zuständig sind.
- Die API soll folgende Funktionen bieten (CRUD):
  - Person/Dozent/Studi anlegen (Create)
  - Alle Personen/Dozenten/Studis anzeigen (Read)
  - Eine Person/Dozent/Studi bearbeiten (Update)
  - Eine Person/Dozent/Studi löschen (Delete)


2. Frontend (z.B. React, Angular oder Vue):


- Zeigen Sie eine Liste aller Personen, Dozenten und Studierenden an.
- Ermöglichen Sie das Anlegen, Bearbeiten und Löschen von Personen, Dozenten und Studierenden über die Oberfläche.


3. Zusatz:


- Dokumentieren Sie die API (z.B. mit Swagger/OpenAPI oder einer eigenen Markdown-Datei).
- Geben Sie eine kurze Anleitung, wie das Projekt gestartet wird.

**Hinweise:**

- Die Anwendung muss nicht schön gestaltet sein, Funktionalität steht im Vordergrund.
- Die Datenbank kann lokal laufen (z.B. SQLite für einfache Einrichtung).
- Die Projektstruktur soll klar zwischen Backend und Frontend trennen (zwei Ordner).
- Die Backend-Logik soll sauber zwischen Business Objects, Mappern und API trennen.
