import mysql.connector
import json
import os
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog

# Verbindungsdaten
conn_config = {
    "host": "server10.febas.net",
    "user": "janfrielinghaus",
    "password": "faw123bank!",
    "database": "fawbank"
}

# Verbindung zur Datenbank herstellen
conn = mysql.connector.connect(**conn_config)
cursor = conn.cursor()

def export_table_as_json(table_name):
    # SQL-Abfrage, um die gesamte Tabelle abzurufen
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    
    # Daten abrufen
    data = []
    for row in cursor:
        data.append(row)
    
    # Daten als JSON exportieren
    json_data = json.dumps(data, indent=4)
    
    # Ordner für den Export erstellen (mit aktuellem Datum und Uhrzeit)
    export_folder = datetime.now().strftime("%Y_%m_%d-%H_%M")
    os.makedirs(f"output/{export_folder}", exist_ok=True)
    
    # JSON-Datei im exportierten Ordner speichern
    with open(f"output/{export_folder}/{table_name}.json", "w") as json_file:
        json_file.write(json_data)
    
    print(f"{table_name} wurde als JSON exportiert in {export_folder}.")

def import_json_to_table(table_name):
    # JSON-Datei lesen
    with open(f"input/{table_name}.json", "r") as json_file:
        data = json.load(json_file)

    # Spaltennamen abrufen
    cursor.execute(f"DESCRIBE {table_name}")
    columns = [row[0] for row in cursor.fetchall()]

    # Daten in die Tabelle importieren
    for row in data:
        # Daten in den richtigen Reihenfolge einfügen
        placeholders = ",".join(["%s" for _ in columns])
        insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
        cursor.execute(insert_query, tuple(row))
        conn.commit()

    print(f"Daten aus {table_name}.json wurden in die Tabelle importiert.")

def export_action():
    table_name = simpledialog.askstring("Tabelle exportieren", "Bitte geben Sie den Tabellennamen ein:")
    export_table_as_json(table_name)

def import_action():
    table_name = simpledialog.askstring("Tabelle importieren", "Bitte geben Sie den Tabellennamen ein:")
    import_json_to_table(table_name)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Datenbank-Tool")

    export_button = tk.Button(root, text="Export von MySQL", command=export_action)
    export_button.pack()

    import_button = tk.Button(root, text="Import zu MySQL", command=import_action)
    import_button.pack()

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack()

    root.mainloop()

# Verbindung schließen
conn.close()
