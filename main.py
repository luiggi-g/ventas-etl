from pathlib import Path
import pandas as pd
from src.ventas_etl.config.get_roots import get_config_roots
from src.ventas_etl.extract.extract_csv import read_csv
from src.ventas_etl.transform.validate_schema import validate_schemas
from src.ventas_etl.transform.validate_data import validate_data
from src.ventas_etl.transform.clean_data import clean_data
from src.ventas_etl.transform.transform_data import transform_data
from src.ventas_etl.load.load_data import load_data


def main():

    #obtener ruta de de raw
    row_path=get_config_roots()
    for file_path, df_actual in read_csv(row_path):
        print(f'procesando: --{file_path}--')

        schema_is_valid,df_actual,different_elements = validate_schemas(df_actual)
        if schema_is_valid:
            #print temporal para ver ocmo funciona el programa
            print("✓ Esquema validado correctamente. Continuando con la validación de datos.")
        else:
            print(f"error al inspeccionar el schema del archivo{file_path}")
            print(different_elements)
            continue

        data_is_valid, invalid_null_columns, invalid_dtypes, invalid_values = validate_data(df_actual)

        if data_is_valid:
            #print temporal para ver ocmo funciona el programa
            print("✓ data validada correctamente.")
        else:
            if invalid_null_columns:
                print(f"Columnas con nulos no permitidos: {invalid_null_columns}")

            if invalid_dtypes:
                print(f"Columnas con tipos inválidos: {invalid_dtypes}")

            if invalid_values:
                print(f"  → Valores no permitidos: {invalid_values}")

            continue

        df_actual = clean_data(df_actual)
        df_actual = transform_data(df_actual)
        load_data(df_actual)


if __name__ == "__main__":
    main()
