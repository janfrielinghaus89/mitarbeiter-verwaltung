import json
import PySimpleGUI as pygui
import layout
import database as dbtools
import os
import decimal
from datetime import datetime

# config.json anlegen / laden
def create_config(i_host, i_user, i_password, i_database):
    config = {}
    config["host"] = i_host
    config["user"] = i_user
    config["password"] = i_password
    config["database"] = i_database

    with open('config.json', 'w') as config_file:
        json.dump(config, config_file, indent=4)

# Schreibtest
def write_data_to_file(filename, data):
    try:
        with open(filename, "w") as file:
            bytes_written = file.write(data)
            if bytes_written > 0:
                return True  # Erfolgreich geschrieben
            else:
                return False  # Nicht erfolgreich geschrieben
    except Exception as e:
        print(f"Fehler beim Schreiben der Datei: {str(e)}")
        return False  # Fehler beim Schreiben

# Export als JSON
def export_table_as_json(table_name, table_column = None, compare = None):
    # Connection to Database
    conn = dbtools.connect_to_db(dbtools.config_file)
    cursor = dbtools.create_cursor(conn)

    if table_column is None and compare is None:
        # SQL-Abfrage, um die gesamte Tabelle abzurufen
        query = f"SELECT * FROM {table_name}"
    elif table_column is not None and compare is not None:
        # SQL-Abfrage, um den gesuchten Mitarbeiter zu finden
        query = f"SELECT * FROM {table_name} WHERE {table_column} = '{compare}'"

    # Query ausführen
    cursor.execute(query)
    
    # Daten abrufen
    data = []
    
    for row in cursor:
        # Konvertiere Decimal-Werte in float
        converted_row = [float(value) if isinstance(value, decimal.Decimal) else value for value in row]
        data.append(converted_row)
    
    # Daten als JSON exportieren
    json_data = json.dumps(data, indent=4)
    
    # Ordner für den Export erstellen (mit aktuellem Datum und Uhrzeit)
    export_folder = datetime.now().strftime("%Y_%m_%d-%H_%M")
    os.makedirs(f"output/{export_folder}", exist_ok=True)
    
    # JSON-Datei im exportierten Ordner speichern
    #with open(f"output/{export_folder}/{table_name}.json", "w") as json_file:
    #    json_file.write(json_data)
    json_filename = f"output/{export_folder}/{table_name}.json"
    if write_data_to_file(json_filename, json_data):
        print(f"{table_name} wurde als JSON exportiert in {export_folder}.")
        return True
    else:
        print(f"Fehler beim Exportieren von {table_name} als JSON.")
        return False

def change_config():
    window = pygui.Window('Mitarbeiter-Verwaltungstool MiVerT v0.1 - Database konfigurieren', layout.database_config)

    while True:
        event, values = window.read()
        if event == pygui.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Submit':
            # Call json_handler and create config.json
            create_config(values['host'], values['user'], values['password'], values['database'])
    window.close()