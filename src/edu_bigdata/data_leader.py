import pandas as pd
import logging
import sqlite3

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def cargar_datos_desde_csv(csv_file):
    try:
        conn = sqlite3.connect('src/edu_bigdata/static/db/habitantes_de_calle.db')  # Ruta a la base de datos
        df = pd.read_csv(csv_file, encoding='utf-8')
        df.to_sql('HabitanteDeCalle', conn, if_exists='replace', index=False)
        conn.close()
        logging.info(f"Datos cargados desde {csv_file}")
    except FileNotFoundError:
        logging.error(f"Archivo no encontrado: {csv_file}")
    except Exception as e:
        logging.error(f"Error al cargar datos: {e}")