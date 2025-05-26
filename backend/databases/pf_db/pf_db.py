import json
import os


base_dir_pf_db = os.path.dirname(os.path.abspath(__file__))
data_base_pf_path = os.path.join(base_dir_pf_db, 'pf_database.json')

data_base_pf = {}

# Carregar o banco de dados:
if os.path.exists(data_base_pf_path):
    with open(data_base_pf_path, 'r') as f:
        data_base_pf = json.load(f)

# Salvar usuário no banco de dados:
def save_db_pf():
    with open(data_base_pf_path, 'w') as f:
        json.dump(data_base_pf, f, indent=4)