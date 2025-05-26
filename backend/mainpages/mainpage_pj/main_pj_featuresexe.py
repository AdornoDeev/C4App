import backend.databases.products_db.products_db as pj_productsdb
from  backend.modular_functionsinlore import clean
import regex


# Função de visualização dos produtos:
def visualize_products_db(cnpj):
    try:
        acess_my_products_db = pj_productsdb.data_base_products[cnpj]
        for category in acess_my_products_db:
            print(f"[{category}]: ")
            for type_products in acess_my_products_db[category]:
                print(f"{type_products}")
                for products in acess_my_products_db[category][type_products]:
                    print(f"  {products} ",end='R$ ')
                    values = acess_my_products_db[category][type_products][products]
                    print(values)
    except KeyError as k:
        print('\033[31mO estoque de dados não está completo e não pode ser acessado.')

    
# Função para criação de categorias:
def create_category(category_name,cnpj):
    try:
        acess_my_type_products_db = pj_productsdb.data_base_products[cnpj]
        pattern = regex.compile('[a-z]+')
        result = regex.search(pattern, category_name)
        if not result:
            return None
        else:
            if category_name in acess_my_type_products_db:
                print('\033[31mA categoria informada ja existe, se não a deseja mais você pode deletar.\033[m')
                return None
            else:
                pj_productsdb.data_base_products[cnpj].update({category_name:{}})
                pj_productsdb.save_db_products()
                return True
    except KeyError as k:
        return None
# Função de registro de typo de produto:
def register_type_product(cnpj,category,product_type):
    try:    
        acess_my_products_db = pj_productsdb.data_base_products[cnpj]
        pattern = regex.compile('[a-z]+')
        result = regex.search(pattern,category)
        result2 = regex.search(pattern,product_type)
        if not result or not result2:
            return None
        else:
            if product_type in acess_my_products_db[category]:
                print('\033[31mA tipo de produto informado já existe, se não o deseja mais você pode deletar.\033[m')
                return None
            else:
                pj_productsdb.data_base_products[cnpj][category].update({product_type:{}})
                pj_productsdb.save_db_products()
                return True
    except KeyError as k:
        return None

# Função de registro de typo de produto:
def register_new_product(cnpj,category,product_type,new_product,value):
    try:
        acess_my_products_db = pj_productsdb.data_base_products[cnpj][category][product_type]
        pattern = regex.compile('[a-z]+')
        pattern2 = regex.compile('[0-9]+')
        result = regex.search(pattern,category)
        result2 = regex.search(pattern,product_type)
        result3 = regex.search(pattern,new_product)
        result4 = regex.search(pattern2,value)
        if not result or not result2 or not result3 or not result4:
            return None
        else:
            if new_product in acess_my_products_db:
                print('\033[31mO produto informado já existe, se não o deseja mais você pode deletar.\033[m')
                return None
            else:
                pj_productsdb.data_base_products[cnpj][category][product_type].update({new_product:value})
                pj_productsdb.save_db_products()
                return True
    except KeyError as k:
        return None


# Execuções:
# Criando categoria para o banco de produtos.
def execute_create_category(login_pj_data_cnpj):
    while True:
        print('---------------------------------------------')
        visualize_products_db(login_pj_data_cnpj)
        print('---------------------------------------------')
        result = create_category(category_name=input('Digite o nome da nova categoria a ser cadastrada: ').strip().lower(),cnpj= login_pj_data_cnpj)
        if not result:
            print('''\033[31mDeve ser informado uma cetegoria e um produto ao mínimo.
    A categoria não pode conter números ou caracteres especiais.
    Tente novamente!\033[m''')
        else:
            print('\033[36mCategoria cadastrada com sucesso!\033[m')
            clean()
            break

# Criando novo tipo de produto:
def execute_create_register_type_product(login_pj_data_cnpj):    
    while True:
        print('---------------------------------------------')
        visualize_products_db(login_pj_data_cnpj)
        print('---------------------------------------------')
        result = register_type_product(cnpj=login_pj_data_cnpj,
                                            category=input('Digite em qual categoria o produto será cadastrado: ').strip().lower(),
                                            product_type=input('Digite o nome do novo tipo de produto: ').strip().lower())
        if not result:
            print('''\033[31mDeve ser informado uma cetegoria, um tipo de, o novo produto e seu repectivo valor.
    A categoria não pode conter números ou caracteres especiais e deve existir.
    O tipo de produto não pode conter números ou caracteres especiais.      
    Tente novamente!\033[m''')
        else:
            print('\033[36mNovo tipo de produto cadastrado com sucesso!\033[m')
            clean()
            break

# Adicionando novo produto.
def execute_register_new_product(login_pj_data_cnpj):
    while True:
        print('---------------------------------------------')
        visualize_products_db(login_pj_data_cnpj)
        print('---------------------------------------------')
        result = register_new_product(cnpj=login_pj_data_cnpj,
                                            category=input('Digite em qual categoria o produto será cadastrado: ').strip().lower(),
                                            product_type=input('Digite nome do tipo de produto em que o produto será cadastrado: ').strip().lower(),
                                            new_product=input('Digite o nome do novo produto a ser cadastrado: ').strip().lower(),
                                            value=input('Digite o valor do novo produto: R$  '))
        if not result:
            print('''\033[31mDeve ser informado uma cetegoria, um tipo de, o novo produto e seu repectivo valor.
    A categoria não pode conter números ou caracteres especiais e deve existir.
    O tipo de produto não pode conter números ou caracteres especiais e deve existir.
    O novo produto não pode conter números ou caracteres especiais.
    seu repectivo valor deve ser um número.      
    Tente novamente!\033[m''')
        else:
            print('\033[36mNovo produto cadastrado com sucesso!\033[m')
            clean()
            break