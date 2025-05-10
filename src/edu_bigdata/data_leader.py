import pandas as pd
import logging
from src.database import obtener_conexion, DB_PATH  

def cargar_datos_desde_csv(csv_file):
    try:
        conn = obtener_conexion()  
        df = pd.read_csv(csv_file, encoding='utf-8')
        df.to_sql('HabitanteDeCalle', conn, if_exists='replace', index=False)
        conn.close()
        logging.info(f"Datos cargados desde {csv_file}")
    except FileNotFoundError:
        logging.error(f"Archivo no encontrado: {csv_file}")
    except Exception as e:
        logging.error(f"Error al cargar datos: {e}")