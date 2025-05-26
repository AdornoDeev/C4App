import json
import os
data_base_pj = {}

base_dir_pj_db = os.path.dirname(os.path.abspath(__file__))
data_base_pj_path = os.path.join(base_dir_pj_db, 'pj_database.json')

# Carregar o banco de dados:
if os.path.exists(data_base_pj_path):
    with open(data_base_pj_path, 'r') as f:
        data_base_pj = json.load(f)

# Salvar usuário no banco de dados:
def save_db_pj():
    with open(data_base_pj_path, 'w') as f:
        json.dump(data_base_pj, f, indent=4)