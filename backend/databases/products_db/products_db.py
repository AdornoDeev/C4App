import json
import os

base_dir_products_db = os.path.dirname(os.path.abspath(__file__))
data_base_products_path = os.path.join(base_dir_products_db, "products_database.json")

data_base_products = {}

# Carregar o banco de dados:
if os.path.exists(data_base_products_path):
    with open(data_base_products_path, "r") as f:
        data_base_products = json.load(f)


# Salvar no banco de dados:
def save_db_products():
    with open(data_base_products_path, "w") as f:
        json.dump(data_base_products, f, indent=4)
