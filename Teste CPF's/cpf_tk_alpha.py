import json

import tkinter as tk


def main():
    arquive = open("/home/ryan/projetinhos/Teste CPF's/cpf_list.json", 'r+')
    
    cpf_list = json.load(arquive)
    
    
    while True:
        menu()
        question = int(input('Escolha uma opção: '))
        
        if question == 1:
            nome = str(input('Digite seu nome: '))
            cpf = str(input('Digite seu cpf: '))
            if not verificar_cpf(cpf): # Fail Fast
                print('Valores inválidos!')
                continue
            if cpf.strip() == '' or nome.strip() == '':
                break
            seu_cpf = formatar_cpf(cpf)
            add_cpf(cpf_list, nome, cpf)
            print(f'O cpf informado é o {seu_cpf}')
            print('Valor adicionado!')
            
   
        elif question == 2:
            cpf_pesquisa = str(input('Informe o cpf: '))
            try:
                nome_pesquisa = cpf_list[cpf_pesquisa]
                print(f'O ser que você está procurando se chama {nome_pesquisa}')
            except KeyError:
                print('Nome inválido!')
            armazenar(arquive, cpf_list)
            
            
        elif question == 3:
            print('Limpando base de dados!')
            apagar(arquive)
        
        
        elif question == 4:
            print('=Base de dados=')
            for c in cpf_list:
                print('=' * 10)
                print('Nome:', cpf_list[c], f'\nCPF: {formatar_cpf(c)}')
                print('='*10)
                
    print('Programa encerrado!')

def formatar_cpf(cpf):
    p1 = cpf[:3]
    p2 = cpf[3:6]
    p3 = cpf[6:9]
    p4 = cpf[9:]
    return f'{p1}.{p2}.{p3}-{p4}'
    
    
def verificar_cpf(cpf):
    if len(cpf) == 11:
        try:
            int(cpf)
            return True
        except ValueError:
            return False
    else:
        return False
    
def menu():
    print('=' * 30)
    print('1 - Adcionar CPF\n2 - Pesquisar pessoa pelo CPF\n3- Limpar Banco de Dados\n4 - Listar Valores')
    print('=' * 30)

def armazenar(arquive, content):
    arquive.seek(0)
    json.dump(content, arquive)

def apagar(arquive):
    arquive.truncate(0)
    
def add_cpf(lista, nome, cpf):
     lista[cpf] = nome
    
    
    
main()