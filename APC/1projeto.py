from copy import deepcopy # usado para copiar um dicionario sem fazer referencia a ele; linha70
from operator import itemgetter # usado para organizar o dicionario em ordem crescente de cadeiras

def comando1(estado_restaurante, texto, num_comandos_feitos, total_visitantes):
    '''
    Colocar um grupo de pessoas em uma mesa de forma otimizada.
    '''

    grupo = int(texto[4]) # separo as palavras e pego o tamanho do grupo
    lugar = texto[8] # pego as ultimas que sei que se referem ao alugar que desejam comer
    total_visitantes += grupo
    tempo_comer = (2*grupo) + 2 + num_comandos_feitos 
    otimizacao_mesas = ''
    procura_otimizacao_mesas = 0
    for acomodacoes in estado_restaurante[lugar]: #leio a lista por todos os parzinhos [mesas,cadeiras]
        if acomodacoes[0] > 0: #garanto que existe uma mesa sobrando para o grupo para cada parzinho
            if grupo <= acomodacoes[1]: #verifico a mesa com o menor numero de cadeiras e salvo sua posicao na lista
                otimizacao_mesas = procura_otimizacao_mesas 
                break # como as cadeiras estao em ordem crescente, a primeira vez que o numero de cadeiras satisfazer o grupo sera a melhor opcao
        procura_otimizacao_mesas += 1
    if otimizacao_mesas == '':
        total_visitantes -= grupo
        return estado_restaurante, -1, 'nao tem', -1, -1, total_visitantes
    else:
        estado_restaurante[lugar][otimizacao_mesas][0] -= 1 
        return estado_restaurante, tempo_comer, lugar, otimizacao_mesas, grupo, total_visitantes


def comando2(restaurante):
    '''
    Consultar o numero de mesas ocupadas em relacao ao numero total.
    '''

    for key in restaurante.keys():
        total_mesas_area = 0
        mesas_ocupadas = 0
        for item in atividade_restaurante:
            if key == item[1]:
                mesas_ocupadas += 1
        for index in range(len(restaurante[key])):
            total_mesas_area += restaurante[key][index][0]
        print(f'{key}: ({mesas_ocupadas} de {total_mesas_area} mesas)')


def comando3(restaurante):  
    '''
    Consultar a lotacao atual do restaurante eem relacao a capacidade total.
    '''

    for key in restaurante.keys():
        lotacao_total = 0
        cadeiras_ocupadas = 0
        for item in atividade_restaurante:
            if key == item[1]:
                cadeiras_ocupadas += item[3]
        for index in range(len(restaurante[key])):
            lotacao_total += (restaurante[key][index][1]) * (restaurante[key][index][0])
        print(f'{key}: ({cadeiras_ocupadas} de {lotacao_total} pessoas)')


def comando4(restaurante, estado_restaurante, alteracao):
    '''
    Adicionar ou remover mesas em alguma area especifica no restaurante.
    '''

    change_mesas = int(alteracao[3])
    change_cadeiras = int(alteracao[6])
    tipo_mudanca = str(alteracao[1])
    area_mudada = alteracao[11]
    operacao = 'adicionadas ou removidas'
    for count in range(len(restaurante[area_mudada])):
        if  restaurante[area_mudada][count][1] == change_cadeiras:
            if tipo_mudanca == 'adicionar':
                operacao = 'adicionadas'
                estado_restaurante[area_mudada][count][0] += change_mesas
                restaurante[area_mudada][count][0] += change_mesas
            elif tipo_mudanca == 'remover':
                operacao = 'removidas'
                estado_restaurante[area_mudada][count][0] -= change_mesas
                restaurante[area_mudada][count][0] -= change_mesas
    if operacao == 'adicionadas ou removidas': # como a variavel nao mudou dentro do 'for', nao havia mesas desse tamanho
        operacao = 'adicionadas' #nunca serao removidas mesas inexistentes
        restaurante[area_mudada].append([change_mesas,change_cadeiras])
        restaurante[area_mudada] = sorted(restaurante[area_mudada], key = itemgetter(1,0))
        estado_restaurante[area_mudada].append([change_mesas,change_cadeiras])
        estado_restaurante[area_mudada] = sorted(estado_restaurante[area_mudada], key=itemgetter(1,0))
    print(f'{change_mesas} mesas de {change_cadeiras} cadeiras {operacao} com sucesso na area {area_mudada}.')
    return estado_restaurante, restaurante
    

def comando_fechar(restaurante, total_visitantes):
    '''
    Fecha o restaurante e mostra a configuracao final dele por cada area e o total de visitantes do dia, alem de uma mensagem motivacional
    '''

    print('Restaurante fechado.')
    print('Balanco final de mesas:')
    for area in restaurante.keys():
        print(f'{area}:')
        for index in range(len(restaurante[area])):
            print(f' {restaurante[area][index][0]} mesas de {restaurante[area][index][1]} cadeiras.')
    print(f'Um total de {total_visitantes} pessoas visitaram o restaurante hoje.')
    print('Bom descanso!')

    
caracteristicas_restaurante = input()
while caracteristicas_restaurante != '--CONFIGURACAO':
    caracteristicas_restaurante = input()
'''
recebimento das configuracoes do restaurante
'''
restaurante = {} # planilha com tudo que o restaurante possui
estado_restaurante = {} # planilha de das relacoes de mesas ainda livres em cada area
while True:
    configuracao = input()
    if configuracao == '--ATENDIMENTO':
        break
    area, mesas, cadeiras = configuracao.split()
    mesas = int(mesas)
    cadeiras = int(cadeiras)
    if area in restaurante:
        restaurante[area].append([mesas,cadeiras])
    else:
        restaurante[area] = [[mesas,cadeiras]]
restaurante = dict(sorted(restaurante.items()))
for keys in restaurante: # coloco as cadeiras, segundo termo das listas internas dos valores, em ordem crescente
    restaurante[keys] = sorted(restaurante[keys], key=itemgetter(1,0))
estado_restaurante = deepcopy(restaurante)

'''
recebimento do atendimento do restaurante
'''
atividade_restaurante = [] # planilha das mesas ocupadas[tempo que eles vao comer, o lugar do restaurente que estao, mesa deles, quantas pessoas sao]
num_comandos_feitos = 0
total_visitantes = 0
while True:
    for pedidos in atividade_restaurante:     
        if num_comandos_feitos == pedidos[0]:  #checo na planilha se esta na hora de liberar a mesa
            lugar = pedidos[1]
            otimizacao_mesas = pedidos[2]
            estado_restaurante[lugar][otimizacao_mesas][0] += 1
            atividade_restaurante.remove(pedidos)
        elif num_comandos_feitos < pedidos[0]: # como esta em ordem crescente, se o 'horario' de saida de algum termo nao chegou,
            break                              # tambem nao tera chegado para todos os seus posteriores 
    comando = int(input())
    if comando == -1:
        comando_fechar(restaurante, total_visitantes)
        break
    elif comando == 1:
        texto = input().split()
        estado_restaurante, tempo_comer, lugar, otimizacao_mesas, grupo, total_visitantes = comando1(estado_restaurante, texto, num_comandos_feitos,total_visitantes)
        if lugar == 'nao tem':
            print('Nao foi possivel levar o grupo de clientes para uma mesa.')
        else:
            num_cadeiras = estado_restaurante[lugar][otimizacao_mesas][1]
            print(f'Um grupo de {grupo} pessoas ocupou uma mesa de {num_cadeiras} lugares na area {lugar}.')
            atividade_restaurante.append([tempo_comer, lugar, otimizacao_mesas, grupo])
            atividade_restaurante.sort() # deixo as pessoas na ordem de quem vai embora primeiro
    elif comando == 2:
        comando2(restaurante)
    elif comando == 3:
        comando3(restaurante)
    elif comando == 4:
        alteracao = input().split()
        estado_restaurante, restaurante = comando4(restaurante, estado_restaurante, alteracao)
        print(estado_restaurante)
    else:
        comando = int(input())
    num_comandos_feitos += 1






























