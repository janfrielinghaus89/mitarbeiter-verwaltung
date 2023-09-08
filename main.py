# Hauptmenü

# TODO: 
# 1. Hauptmenü Buttons: MA anlegen, MA anzeigen, Settings, Exit
# 2a. JSON Handler schreiben
# 2b. Excel Handler schreiben
# 3. Menü für das Anlegen von Mitarbeitern + Import von JSON und Excel Daten in die Datenbank
# 4. Menü für das Anzeigen von Mitarbeitern + Export von JSON und Excel Daten aus der Datenbank
# TODO Ende

# Import libraries
import PySimpleGUI as pygui
import os
# Import local files
import layout
import json_handler

# Check if config.json already exists
if os.path.isfile('config.json'):
    # Config already exists
    # Start Main Menu
    window = pygui.Window('Mitarbeiter-Verwaltungstool MiVerT v0.1 - Hauptmenü', layout.main_menu)

    while True:
        event, values = window.read()
        if event == pygui.WIN_CLOSED or event == 'Exit':
            break
        if event == 'anlegen':
            with open("ma_anlegen.py") as f:
                exec(f.read())
            break
    window.close()

else:
    # Config doesnt exist
    # Start Database config
    window = pygui.Window('Mitarbeiter-Verwaltungstool MiVerT v0.1 - Database konfigurieren', layout.database_config)

    while True:
        event, values = window.read()
        if event == pygui.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Submit':
            # Call json_handler and create config.json
            json_handler.create_config(values['host'], values['user'], values['password'], values['database'])
    window.close()