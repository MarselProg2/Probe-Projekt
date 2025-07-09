1. Datenbank (db)
Verzeichnis:

mysql/
Wichtige Dateien:

MySQL-Dump.sql und MySQL-Dump-v8.sql:
Diese Dateien enthalten das SQL-Schema und Beispieldaten für die MySQL-Datenbank. Sie definieren Tabellen wie Kunden, Konten, Transaktionen usw., die für die Bankanwendung benötigt werden.
2. Backend
Verzeichnis:

src/
main.py: Startpunkt des Backends, enthält die Server-Initialisierung und Routing.
requirements.txt: Listet die Python-Abhängigkeiten (z.B. Flask, SQLAlchemy).
server/bo/: Enthält die Business Objects (BOs) – Python-Klassen, die die Geschäftslogik und Datenstruktur für Entitäten wie Account, Customer, Transaction, User abbilden.
Account.py, Customer.py, Transaction.py, User.py, BusinessObject.py
server/db/: Enthält die Mapper-Klassen, die für die Kommunikation zwischen den BOs und der Datenbank zuständig sind.
AccountMapper.py, CustomerMapper.py, TransactionMapper.py, UserMapper.py, Mapper.py
server/BankAdministration.py: Zentrale Logik für Bankoperationen, verwendet die BOs und Mapper, um Geschäftsprozesse zu steuern.
SecurityDecorator.py: Vermutlich für Authentifizierung/Autorisierung zuständig.
Ablauf:

Das Backend stellt eine REST-API bereit.
Die Business Objects (BOs) repräsentieren die Daten und Logik der Bank-Entitäten.
Die Mapper-Klassen übernehmen das Laden, Speichern, Aktualisieren und Löschen der Daten in der Datenbank.
Die zentrale Steuerung erfolgt über die BankAdministration, die die BOs und Mapper orchestriert.
3. Frontend
Verzeichnis:

frontend/
Wichtige Dateien und Ordner:

src/
App.js, index.js: Einstiegspunkte der React-Anwendung.
api/: Schnittstelle zum Backend, enthält Klassen wie BankAPI.js, AccountBO.js, CustomerBO.js, TransactionBO.js, BusinessObject.js.
components/: Wiederverwendbare UI-Komponenten, z.B. Listen, Detailansichten, Dialoge.
pages/: Seiten wie About.js, SignIn.js.
firebase/: Für Authentifizierung (z.B. Google Login).
public/: Statische Dateien wie index.html, Icons, Manifest.
http-fake-backend/: Konfigurationsdateien und Beispieldaten für lokale Tests ohne echtes Backend.
package.json: Listet die JavaScript-Abhängigkeiten und Build-Skripte.
Ablauf:

Das Frontend ist eine React-App, die mit der REST-API des Backends kommuniziert.
Die API-Klassen im Frontend kapseln die HTTP-Requests an das Backend.
Die Komponenten und Seiten stellen die Benutzeroberfläche dar, z.B. für das Anzeigen und Bearbeiten von Kunden, Konten und Transaktionen.
Dialog-Komponenten ermöglichen Interaktionen wie das Anlegen oder Löschen von Einträgen.
Zusammenfassung des Zusammenspiels
Die Datenbank speichert alle relevanten Daten (Kunden, Konten, Transaktionen).
Das Backend stellt die Geschäftslogik und die REST-API bereit, verwaltet die Daten über BOs und Mapper.
Das Frontend bietet eine moderne Benutzeroberfläche, kommuniziert über die API mit dem Backend und stellt die Daten dar bzw. ermöglicht deren Bearbeitung.