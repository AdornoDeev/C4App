from backend.modular_functionsinlore import clean
import backend.mainpages.mainpage_sh.main_sh_featuresexe as shfeat
import backend.databases.sh_db.sh_db as sh_db
import backend.databases.products_db.products_db as productsdb
import sys,json

# Recebendo as informações do login.
if len(sys.argv) > 1:
    login_sh_json = sys.argv[1]
    login_sh_data = json.loads(login_sh_json)
else:
    print("Nada recebido")

# Escolha do usuário:
if len(productsdb.data_base_products[login_sh_data['cnpj']]) < 1:
    print('\033[31mNão existe nenhuma categoria no estoque, aguarde o propríetário adicionar alguma.\033[m')
else:
    while True:
        decision_sh_main = input(f"""
Página Principal: Olá {sh_db.data_base_sh[login_sh_data['cnpj']][login_sh_data['id']]['name_sh_db']}!
            
        Escolha uma das opções:

[Visualizar estoque]: 1
[Cadastrar produtos]: 2
[Sair]: 3
Digite aqui: """)
        if decision_sh_main == '1':
            clean()
            print('---------------------------------------------------')
            shfeat.visualize_products_db(cnpj = login_sh_data['cnpj'])
            print('---------------------------------------------------')
        elif decision_sh_main == '2':
            if len(list(productsdb.data_base_products[login_sh_data['cnpj']].values())[0]) < 1:
                print('\033[31mNão é possível realizar o cadastro de nenhum produto, pois não há tipos de produtos para cadastrar. Aguarde seu chefe!\033[m')
                break
            else:
                shfeat.execute_new_product_sh(login_sh_data['cnpj'])
            clean()
        elif decision_sh_main == '3':
            break
        else:
            print('\033[31mUmas das opções deve ser informada, tente novamente!\033[m')
            clean()
