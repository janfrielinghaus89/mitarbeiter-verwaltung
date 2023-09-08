# Mitarbeiter anlegen
# Mitarbeiter in MySQL exportieren

import layout
import database as dbtools
import PySimpleGUI as pygui

window = pygui.Window('Mitarbeiter-Verwaltungstool MiVerT v0.1 - Mitarbeiter anlegen', layout.create_employee)

while True:
    event, values = window.read()
    if event == pygui.WIN_CLOSED or event == 'Exit':
        break
    if event == 'anlegen':
        print(event, values)
window.close()