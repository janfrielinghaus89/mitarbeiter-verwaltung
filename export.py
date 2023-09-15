# -*- coding: utf-8 -*-

import layout
import json_handler as jsh
import excel_handler as exh
import PySimpleGUI as pygui
import database as dbtools

window = pygui.Window('Mitarbeiter-Verwaltungstool MiVerT v0.1 - Mitarbeiter anlegen', layout.data_export)

while True:
    event, values = window.read()
    if event == pygui.WIN_CLOSED or event == 'Exit':
        break
    if event == 'json':
        if jsh.export_table_as_json(dbtools.table_mitarbeiter):
            pygui.popup('Die Datei wurde im Ordner "output" abgelegt.')
            break
        else:
            pygui.popup('Ein Fehler ist beim Exportieren aufgetreten.')
            break
    if event == 'excel':
        print('Excel')
        if exh.export_table_as_excel(dbtools.table_mitarbeiter):
            pygui.popup('Die Datei wurde im Ordner "output" abgelegt.')
            break
        else:
            pygui.popup('Ein Fehler ist beim Exportieren aufgetreten.')
            break

window.close()