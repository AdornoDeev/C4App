from backend.modular_functionsinlore import clean
import backend.databases.pj_db.pj_db as pj_db
import backend.databases.pf_db.pf_db as pf_db
import backend.databases.products_db.products_db as products_db
import backend.modular_functionsinlore as mo
import sys,json

# Recebendo as informações do login.
if len(sys.argv) > 1:
    login_pf_json = sys.argv[1]
    login_pf_data = json.loads(login_pf_json)
else:
    print("Nada recebido")

# Recebendo a distâncias e nomes dos restaurantes:
while True:
    pf_main_decision = input(f"""
Página principal: {pf_db.data_base_pf[login_pf_data['cpf']]['name_pf_db']}.
    Escolha uma das opções abaixo:

[Verificar promos próximas]: 1 
[sair]: 2
Digite aqui: """)
    clean()
    
    if pf_main_decision == '1':
        result = list()
        for pos,cnpj in enumerate(list(pj_db.data_base_pj.keys())):
            result.append(mo.calculate_distance_from_dicts(dict2=pf_db.data_base_pf[login_pf_data['cpf']],dict1=pj_db.data_base_pj[cnpj]))
            result[pos].append(cnpj)
        
        # Retornando os CNPJS mais próximos os restaurantes com  no máximo 32km:
        result = mo.filtrar_cnpjs_por_distancia(result)
        
        print('------------------------------------------------------------------------------')
        # Print do estabelecimento com seus produtos promocionais:
        
        for cnpj_valido in result:
            nome_est = pj_db.data_base_pj[cnpj_valido]
            print(f"O estabelecimento {nome_est['name_pj_db']} está com as promoções em: ")
            acess_my_products_db = products_db.data_base_products[cnpj_valido]
            for category in acess_my_products_db:
                print(f"\n[{category}]")
                for type_products in acess_my_products_db[category]:
                    print(f" {type_products}")
                    value = products_db.data_base_products[cnpj_valido][category][type_products]
                    print(f" {value}")
            print('------------------------------------------------------------------------------')
    elif pf_main_decision == '2':
        break
    else:
        print('\033[31mUma das opções devem ser digitadas, tente novamente!\033[m')