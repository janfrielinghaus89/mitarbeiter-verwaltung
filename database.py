import json
import mysql.connector

##########
# Config #
##########

config_file = 'config.json'

# Funktion um die Config aus json-File zu erhalten
def get_config(filename):
    with open(filename, 'r') as config_file:
        config = json.load(config_file)
    return config

###########
# Connect #
###########

def connect_to_db(filename):
    # Verbindung mit MySQL DB aufbauen
    config = get_config(filename)
    conn = mysql.connector.connect(**config)
    return conn

def create_cursor(conn):
    cursor = conn.cursor()
    return cursor

##############
# Disconnect #
##############

def close_connection(cursor, conn):
    cursor.close()
    conn.close()

##########
# Querys #
##########

# SQL-Abfrage, um Positionsnamen abzurufen
def get_position_names(config_file):
    conn = connect_to_db(config_file)
    cursor = create_cursor(conn)
    
    query = "SELECT Bezeichnung FROM Position"
    cursor.execute(query)

    # Positionsnamen aus dem Ergebnis abrufen
    position_names = [row[0] for row in cursor.fetchall()]

    # Verbindung schließen
    close_connection(cursor, conn)
    
    return position_names

# SQL-Abfrage, um MA Listen zu füllen
def get_db_info(config_file, column_name, table_name):
    conn = connect_to_db(config_file)
    cursor = create_cursor(conn)
    
    query = f"SELECT {column_name} FROM {table_name}"
    cursor.execute(query)

    # Positionsnamen aus dem Ergebnis abrufen
    results = [row[0] for row in cursor.fetchall()]

    # Verbindung schließen
    close_connection(cursor, conn)
    
    return results

# SQL-Abfrage, um Foreign Key abzurufen
def get_db_info2(config_file, column_name, table_name, where_column, where_value):
    conn = connect_to_db(config_file)
    cursor = create_cursor(conn)

    query = f"SELECT {column_name} FROM {table_name} WHERE {where_column} = '{where_value}'"
    cursor.execute(query)

    results = cursor.fetchone()

    return results

    # Verbindung schließen
    close_connection(cursor, conn)