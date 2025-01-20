import os
import json
from pathlib import Path
from ..consts import *

def load_data():
    app_dir = Path(__file__).parents[1]
    data_path = os.path.join(app_dir, RELATIVE_DATA_PATH)

    data = {}
    databases = ['Comercializacao.json','Exportacao.json','Importacao.json','Processamento.json','Producao.json']

    for item in databases:
        try:
            # Load arquivos JSON
            with open(os.path.join(data_path, item), 'r', encoding='utf-8') as fp:
                data[Path(item).stem.lower()] = json.load(fp)
        except Exception as e:
            #preenche com lista vazia caso não exista
            data[Path(item).stem.lower()] = []
    
    return data