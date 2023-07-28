import os
import json
import csv


# Função que verifica se uma pessoa está autorizada a entrar no evento de confraternização
def validar_participante(dicionario: dict, id: str, nome: str, idade: int) -> bool:
    if id in dicionario:
        return dicionario[id].get('Nome') == nome and dicionario[id].get('Idade') == idade
    return False

# Função que armazena informações sobre penetras em um arquivo JSON
def registrar_penetra(penetras: list, id: str, nome: str, idade: int):
    penetrante = {'ID': id, 'Nome': nome, 'Idade': idade}
    penetras.append(penetrate)

# Função principal que gerencia a festa de confraternização
def gerenciar_festa(ano:int, dicionario:dict):
    # Carregar informações dos penetras (se o arquivo existir)
    nome_do_arquivo_penetras = f'penetras{ano}.json'
    if os.path.exists(nome_do_arquivo_penetras):
        with open(nome_do_arquivo_penetras, 'r') as f:
            penetras = json.load(f)
    else:
        penetras = []

    dicionario_de_festa = dicionario_de_arquivo(ano, 'festa.csv')

    if dicionario_de_festa == {}:
        return dicionario, penetras

    for id, participante in dicionario_de_festa.items():
        nome = participante.get('Nome')
        idade = int(participante.get('Idade'))

        if validar_participante(dicionario, id, nome, idade):
            dicionario[id].update({'Festa': 'Compareceu'})
        else:
            dicionario[id].update({'Festa': 'Não Compareceu'})
            registrar_penetra(penetras, id, nome, idade)

    # Salvar as informações dos penetras no arquivo JSON
    with open(nome_do_arquivo_penetras, 'w') as f:
        json.dump(penetras, f)

    return dicionario, penetras

# Restante do código...

# Menu principal para deixar a aplicação mais visual
def menu():
    '''
    Essa é a função principal do programa, ela exibe um menu de opções e permite que o usuário gerencie os dados.
    '''
    # Restante do código...

    opcao = input('Digite a opção escolhida (1, 2, 3 ou 4): ')
    while opcao != '4':
        if opcao == '1':
            # Restante do código...

        elif opcao == '2':
            # Restante do código...

        elif opcao == '3':
            ano = int(input('Digite o ano do evento de confraternização: '))
            if ano != 2020 and ano != 2021 and ano != 2022:
                print('Ano inválido. Digite um ano entre 2020 e 2022')
            else:
                dicionario_final, penetras = gerenciar_festa(ano, dicionario_final)
                gerar_arquivo_json(ano, dicionario_final)
                # Mostrar informações sobre penetras
                if penetras:
                    print('--- Penetras ---')
                    for penetra in penetras:
                        print(f"ID: {penetra['ID']}, Nome: {penetra['Nome']}, Idade: {penetra['Idade']}")
                    print('-----------------')

        # Restante do código...

        opcao = input('Para continuar digite uma das opções (1, 2, 3 ou 4) ou digite 4 para sair: ')

menu()