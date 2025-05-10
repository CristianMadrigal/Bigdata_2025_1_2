import os
import datatime
import pandas as pd
import sqlite3

DB_PATH = 'src/static/db/habitantes_de_calle.db'  

def crear_tabla_habitante():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS HabitanteDeCalle (
        id_habitante INTEGER PRIMARY KEY AUTOINCREMENT,
        numero INTEGER UNIQUE NOT NULL,
        nombres_apellidos TEXT NOT NULL,
        sexo TEXT,
        spa_consume TEXT,
        ocupacion_oficio TEXT
    )
    ''')
    conn.commit()
    conn.close()

def obtener_conexion():
    """Obtiene una conexión a la base de datos."""
    return sqlite3.connect(DB_PATH)