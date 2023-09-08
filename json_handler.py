import json

# config.json anlegen / laden
def create_config(i_host, i_user, i_password, i_database):
    config = {}
    config["host"] = i_host
    config["user"] = i_user
    config["password"] = i_password
    config["database"] = i_database

    with open('config.json', 'w') as config_file:
        json.dump(config, config_file, indent=4)

# Export als JSON
# Import als JSON