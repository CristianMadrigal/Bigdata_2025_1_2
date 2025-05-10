import argparse
import logging
from .data_leader import cargar_datos_desde_csv  # Importa la función

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description="Carga datos de habitantes de calle a SQLite.")
    parser.add_argument("csv_file", help="Ruta al archivo CSV.")
    args = parser.parse_args()

    cargar_datos_desde_csv(args.csv_file)  # Llama a la función

if __name__ == "__main__":
    main()