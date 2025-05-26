from backend.modular_functionsinlore import clean
import backend.mainpages.mainpage_pj.main_pj_featuresexe as pjfeat
import backend.databases.pj_db.pj_db as pj_db
import backend.databases.products_db.products_db as productsdb
import sys,json

# Recebendo informações da página de login.
if len(sys.argv) > 1:
    login_pj_json = sys.argv[1]
    login_pj_data = json.loads(login_pj_json)
else:
        print("Nada recebido")

# Escolhas do usuário, o que ele deseja realizar:
while True:
    if len(productsdb.data_base_products[login_pj_data["cnpj"]]) < 1:
        print('Como é sua primeira vez acessando o sistema, seu estoque está vazio. Siga os processo para começar!')
        pjfeat.execute_create_category(login_pj_data["cnpj"])
        pjfeat.execute_create_register_type_product(login_pj_data["cnpj"])
    else:
        main_pj_choice = input(f"""
Página Principal: Olá {pj_db.data_base_pj[login_pj_data["cnpj"]]['name_pj_db']}
    
    Escolha uma das opções: 
                               
[Visualizar estoque]: 1
[Criar categorias para o estoque]: 2
[Criar novos tipos de produtos]: 3
[Criar novos produtos]: 4
[Cadastrar funcionário]: 5 (Não Funcional).
[Sair]: 6
Digite aqui: """)
        if main_pj_choice == '1':
            clean()
            print('----------------------------------------------')
            pjfeat.visualize_products_db(login_pj_data["cnpj"])
            print('----------------------------------------------')
        elif main_pj_choice == '2':
            clean()
            pjfeat.execute_create_category(login_pj_data["cnpj"])
        elif main_pj_choice == '3':
            clean()
            pjfeat.execute_create_register_type_product(login_pj_data["cnpj"])
        elif main_pj_choice == '4':
            clean()
            pjfeat.execute_register_new_product(login_pj_data["cnpj"])
        elif main_pj_choice == '5':
            print()
        elif main_pj_choice == '6':
            break
        else:
            print('\033[31mUmas das opções deve ser informada, tente novamente!\033[m')
            clean()