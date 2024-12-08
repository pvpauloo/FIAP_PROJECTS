import pandas as pd
import re
import json
import os

# Carregar configurações do arquivo JSON
with open("config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)

baseURL = config["baseURL"]
path = config["path"]

def detect_delimiter(file_path):
    """Detecta o delimitador de um arquivo CSV."""
    delimiters = [';', '\t']
    for delimiter in delimiters:
        try:
            df = pd.read_csv(file_path, delimiter=delimiter, nrows=3)
            if df.shape[1] > 1:
                return delimiter
        except Exception:
            continue
    return None

def trata_tipo_csv(loader, rota):
    """Trata o CSV conforme o tipo e rota especificados."""
    tiposCsv = {
        "Producao": "Produto",
        "Processamento": "Cultivar",
        "Comercializacao": "Produto"
    }
    
    delimiter = detect_delimiter(loader)
    try:
        data = pd.read_csv(loader, delimiter=delimiter)
    except:
        print("Erro ao tendar baixar o arquivo: ",loader)
    if rota in tiposCsv.keys():
        data.columns = [col.title() for col in data.columns]
        data["Tipo"] = data[tiposCsv[rota]].apply(lambda x: x if x.isupper() else None)
        data["Tipo"] = data["Tipo"].ffill()
        data = data[data[tiposCsv[rota]].apply(lambda x: not x.isupper())]

        columns = list(data.columns)
        columns.remove("Tipo")
        columns.insert(3, "Tipo")
        data = data[columns].reset_index(drop=True)

    colunas = [x for x in data.columns if not (re.match(r"\d{4}\.1", x) or x.isdigit())]
    data = pd.melt(data, id_vars=colunas, var_name="Ano", value_name="Valor")
    return data

def processar_dados():
    """Processa os dados e salva em arquivos JSON."""
    for p in path:
        if isinstance(path[p], list):
            dfs = []
            for q in path[p]:
                csv_loader = f"{baseURL}{q}"
                data = trata_tipo_csv(csv_loader, p)
                data["Source"] = q
                dfs.append(data)
            data = pd.concat(dfs, ignore_index=True)
        else:
            csv_loader = f"{baseURL}{path[p]}"
            data = trata_tipo_csv(csv_loader, p)

        json_data = data.to_json(orient="records", force_ascii=False, indent=4)
        
        # Definir o diretório onde os arquivos serão salvos
        output_dir = "db_json"

        # Verificar se a pasta já existe; se não, criar
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Caminho do arquivo de saída dentro da pasta "db_json"
        output_path = os.path.join(output_dir, f"{p}.json")

        with open(output_path, "w", encoding="utf-8") as json_file:
            json_file.write(json_data)
        print(f"Arquivo JSON salvo em: {output_path}")
