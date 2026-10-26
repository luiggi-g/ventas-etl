from pathlib import Path
import sys
import json

def get_config_roots():

    ruta_padre_proyecto = Path(sys.prefix).parent
    row_path = Path(ruta_padre_proyecto)/'data'/'raw'

    return row_path
