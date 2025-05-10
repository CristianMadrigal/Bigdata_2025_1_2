import argparse
import logging
from src.database import crear_tabla_habitante, obtener_conexion  
from src.data_loader import cargar_datos_desde_csv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description="Carga datos de habitantes de calle a SQLite.")
    parser.add_argument("csv_file", help="Ruta al archivo CSV.")
    args = parser.parse_args()

    crear_tabla_habitante()  
    cargar_datos_desde_csv(args.csv_file)  

    
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM HabitanteDeCalle")
    cantidad = cursor.fetchone()[0]
    logging.info(f"Total de habitantes de calle: {cantidad}")
    conn.close()

if __name__ == "__main__":
    main()