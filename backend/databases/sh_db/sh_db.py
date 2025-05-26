import json
import os

data_base_sh = {'44.455.566/6000-24':{'897':{'name_sh_db':'Rufus','password_sh_db':'Ru1234567@'}}}

base_dir_sh_db = os.path.dirname(os.path.abspath(__file__))
data_base_sh_path = os.path.join(base_dir_sh_db, 'sh_database.json')

# Carregar o banco de dados:
if os.path.exists(data_base_sh_path):
        with open(data_base_sh_path, 'r') as f:
            data_base_sh = json.load(f)

# Salvar usuário no banco de dados:
def save_db_sh():
    with open(data_base_sh_path, 'w') as f:
        json.dump(data_base_sh, f, indent=4)