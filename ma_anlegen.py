# Mitarbeiter anlegen
# Mitarbeiter in MySQL exportieren

import layout
import database as dbtools
import PySimpleGUI as pygui
import mysql.connector

# SQL-Query, um MA anzulegen
def create_employee(config_file, nachname, vorname, posID, zeitID, gehalt):
    conn = dbtools.connect_to_db(config_file)
    cursor = dbtools.create_cursor(conn)

    query = f"INSERT INTO Mitarbeiter (Nachname, Vorname, Position_ID, Zeitmodell_ID, Gehalt) VALUES('{nachname}', '{vorname}', '{posID}', '{zeitID}', '{gehalt}')"
    #cursor.execute(query)

    try:
        # SQL-Abfrage ausführen
        cursor.execute(query)
    
        # Transaktion bestätigen
        conn.commit()
    except Exception as e:
        # Bei einem Fehler die Transaktion rückgängig machen und Fehler protokollieren
        conn.rollback()
        print(f"Fehler beim Hinzufügen des Mitarbeiters: {str(e)}")
    finally:
        # Überprüfen, ob der INSERT erfolgreich war
        if cursor.rowcount > 0:
            dbtools.close_connection(cursor, conn)
            return True
        else:
            dbtools.close_connection(cursor, conn)
            return False

    

window = pygui.Window('Mitarbeiter-Verwaltungstool MiVerT v0.1 - Mitarbeiter anlegen', layout.create_employee)

while True:
    event, values = window.read()
    if event == pygui.WIN_CLOSED or event == 'Exit':
        break
    if event == 'anlegen':
        print(event, values)
        try:
            position_ID = dbtools.get_db_info2(dbtools.config_file, 'Position_ID', 'Position', 'Bezeichnung', values['position'])
            zeitmodell_ID = dbtools.get_db_info2(dbtools.config_file, 'Zeitmodell_ID', 'Zeitmodell', 'Modell', values['zeitmodell'])

            # Zu speichernden Wert aus dem Tupel extrahieren
            if position_ID is not None:
                position_ID = position_ID[0]

            if zeitmodell_ID is not None:
                zeitmodell_ID = zeitmodell_ID[0]

            gehalt_rounded = round(float(values['gehalt']), 2)
    
            if position_ID is not None and zeitmodell_ID is not None:
                if create_employee(dbtools.config_file, values['nachname'], values['vorname'], position_ID, zeitmodell_ID, gehalt_rounded):
                    pygui.popup('Mitarbeiter wurde erfolgreich hinzugefügt.')
                else:
                    pygui.popup('Fehler beim Hinzufügen des Mitarbeiters.')
            else:
                pygui.popup('Position oder Zeitmodell nicht gefunden.')
        except Exception as e:
            pygui.popup(f'Ein Fehler ist aufgetreten: {str(e)}')

window.close()