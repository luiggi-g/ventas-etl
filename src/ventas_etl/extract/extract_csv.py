from pathlib import Path
import pandas as pd

def read_csv(folder_path: Path) -> iterator[tuple[Path, pd.DataFrame]]:
    """
    en esta funcion validaremos si el archivo existe desde la ruta que esta
    alojada en path como un string y si su extesnsion es csv
    """
    folder = Path(folder_path)

    if folder.is_dir():

        archivos_encontrados = 0
        for file in folder.glob("*.csv"):
            archivos_encontrados += 1
            df = pd.read_csv(file)
            print(list(df.columns))
            yield file, df


        if archivos_encontrados == 0:
            raise FileNotFoundError(f"No se detectaron archivos .csv en {folder}")
    else :
        raise FileNotFoundError ("la carpeta en la que deberia estar el archivo no existe")
