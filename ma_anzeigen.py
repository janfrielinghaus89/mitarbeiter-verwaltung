# Mitarbeiter suchen und anzeigen
# Import auf MySQL Datenbank

# -*- coding: utf-8 -*-

import layout
import database as dbtools
import PySimpleGUI as pygui

window = pygui.Window('Mitarbeiter-Verwaltungstool MiVerT v0.1 - Mitarbeiter suchen', layout.show_employee)

while True:
    event, values = window.read()
    if event == pygui.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'suchen':
        # Initialisiere die Suchkriterien
        search_criteria = None

        # Bestimme die Suchkriterien basierend auf den ausgefüllten Feldern
        if values['ma_id']:
            search_criteria = ('Mitarbeiter_ID', values['ma_id'])
        elif values['nachname']:
            search_criteria = ('Nachname', values['nachname'])
        elif values['position']:
            search_criteria = ('Position_ID', values['position'])
        elif values['zeitmodell']:
            search_criteria = ('Zeitmodell_ID', values['zeitmodell'])

        if search_criteria:
            results = dbtools.get_ma_info(dbtools.config_file, dbtools.table_mitarbeiter, *search_criteria)
            if results:
                # Initialisiere die Zeichenkette für die Popup-Nachricht
                popup_message = ""
                # Formatieren der Ergebnisse
                record_lines = []
                for record in results:
                    popup_message += "----------Beginn der Mitarbeiter-Daten----------\n"
                    popup_message += f"Mitarbeiter ID: {record[0]}\n"
                    popup_message += f"Nachname: {record[1]}\n"
                    popup_message += f"Vorname: {record[2]}\n"
                    popup_message += f"Position ID: {record[3]}\n"
                    popup_message += f"Zeitmodell ID: {record[4]}\n"
                    popup_message += f"Gehalt: {record[5]} Euro\n"
                    popup_message += "----------Ende der Mitarbeiter-Daten----------\n"
                    popup_message += "\n"

                # Überschrift für das Popup-Fenster
                popup_title = "Mitarbeiterdaten"

                # Erstelle das Popup-Fenster
                pygui.popup(popup_message, title = popup_title, font=("Arial", 12))
            else:
                pygui.popup('Keine Mitarbeiter gefunden.')
        
        print(event, values)
        
window.close()