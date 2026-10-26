from pathlib import Path
import json
def read_json_config(file_name,):
    current_folder = Path(__file__).resolve()
    current_folder = current_folder.parents[3]
    config_folder = current_folder / f'config/{file_name}'
    json_data = json.loads(config_folder.read_text(encoding='utf-8'))

    return json_data
