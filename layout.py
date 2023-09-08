import PySimpleGUI as pygui
import database as dbtools

# Add some color for GUI
pygui.theme('DarkTeal9')

# Main Menu layout
main_menu = [
    [pygui.Text('Bitte wählen Sie einen Menüpunkt aus.', size = (40,2))],
    [pygui.Button('Mitarbeiter anlegen', key = 'anlegen')],
    [pygui.Button('Mitarbeiter anzeigen', key = 'anzeigen')],
    [pygui.Button('Daten exportieren', key = 'export')],
    [pygui.Exit()]
]

# Database Config layout
database_config = [
    [pygui.Text('Bitte geben Sie ihre Datenbank-Verbindung ein:', size = (50,2))],
    [pygui.Text('Host:', size = (30,1)), pygui.InputText(key = 'host')],
    [pygui.Text('DB-User:', size = (30,1)), pygui.InputText(key = 'user')],
    [pygui.Text('Passwort:', size = (30,1)), pygui.InputText(key = 'password', password_char='*')],
    [pygui.Text('Database:', size = (30,1)), pygui.InputText(key = 'database')],
    [pygui.Submit(), pygui.Exit()]
]

# Create employee
create_employee = [
    [pygui.Text('Nachname:', size = (30,1)), pygui.InputText(key = 'nachname')],
    [pygui.Text('Vorname:', size = (30,1)), pygui.InputText(key = 'vorname')],
    [pygui.Text('Position:', size = (30,1)), pygui.Combo(dbtools.get_db_info(dbtools.config_file, 'Bezeichnung', 'Position'), key = 'position')],
    [pygui.Text('Zeitmodell:', size = (30,1)), pygui.Combo(dbtools.get_db_info(dbtools.config_file, 'Modell', 'Zeitmodell'), key = 'position')],
    [pygui.Text('Gehalt:', size = (30,1)), pygui.InputText(key = 'gehalt')],
    [pygui.Button('Mitarbeiter anlegen', key = 'anlegen'), pygui.Exit()]
]
