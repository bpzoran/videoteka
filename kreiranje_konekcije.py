import configparser

import mysql.connector
from mysql.connector import errorcode


def procitaj_konfiguraciju(filename='config.ini', section='database'):
    parser = configparser.ConfigParser()
    parser.read(filename)

    db_params = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db_params[item[0]] = item[1]
    else:
        raise Exception(f'{section} not found in {filename}')
    return db_params


def get_connection():
    try:
        db_config = procitaj_konfiguraciju()
        return mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        raise
