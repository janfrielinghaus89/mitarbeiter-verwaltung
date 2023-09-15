# -*- coding: utf-8 -*-
# Hauptmenü

# TODO: 
# 1. Hauptmenü Buttons: MA anlegen, MA anzeigen, Settings, Exit
# 2a. JSON Handler schreiben
# 2b. Excel Handler schreiben
# 3. Menü für das Anlegen von Mitarbeitern
# 4. Menü für das Anzeigen von Mitarbeitern + Export von JSON und Excel Daten aus der Datenbank
# TODO Ende

# Import libraries
import PySimpleGUI as pygui
import os
# Import lokale Dateien
import json_handler
import layout

# Überprüfe, ob config.json bereits existiert
if os.path.isfile('config.json'):
    # Config ist bereits vorhanden
    # Starte Hauptmenü
    window = pygui.Window('Mitarbeiter-Verwaltungstool MiVerT v0.1 - Hauptmenü', layout.main_menu)

    while True:
        event, values = window.read()
        if event == pygui.WIN_CLOSED or event == 'Exit':
            break
        # Event Mitarbeiter anlegen
        if event == 'anlegen':
            with open("ma_anlegen.py") as f:
                exec(f.read())
            break
        # Event Mitarbeiter anzeigen
        if event == 'anzeigen':
            with open("ma_anzeigen.py") as f:
                exec(f.read())
            break
        # Event Exportieren
        if event == 'export':
            with open("export.py") as f:
                exec(f.read())
            break
        # Datenbankeinstellung verändern
        if event == 'einstellungen':
            json_handler.change_config()
            break
    window.close()

else:
    # Config existiert nicht
    # Starte Abruf der Database Config
    json_handler.change_config()