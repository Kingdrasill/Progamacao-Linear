# -*- coding: utf-8 -*-
import entrada
import solucoes

print('Digite o nome do arquivo de entrada: ', end='')
nome = input()
print()
(status, msg, n, m, c, A, b) = entrada.lerEntrada(nome)

if status:
    resposta = solucoes.calcularSolucoes(n,m, c, A, b)
    
    viaveis = [i for i in range(len(resposta)) if resposta[i][2] == 'viável']
    inviaveis = [i for i in range(len(resposta)) if resposta[i][2] == 'inviável']

    otima = min([resposta[i][1] for i in range(len(resposta)) if i in viaveis])
    s = [resposta[i][1] for i in range(len(resposta))]
    indicies_otimos = solucoes.np.where(s == otima)[0]
    
    for i in range(len(resposta)):
        saida = 'Solução: x=('
        for j in range(n):
            if j == 0:
                saida += f'{resposta[i][0][j]}'
            else:
                saida += f', {resposta[i][0][j]}'
        saida += f'),\tz={resposta[i][1]},\t{resposta[i][2]}'
        if i in indicies_otimos and resposta[i][2]:
            saida += ' ==> ótima'
        print(saida)
    print()
    print(f'Soluções básicas viáveis:\t{len(viaveis)}')
    print(f'Soluções básicas inviáveis:\t{len(inviaveis)}')
                
else:
    print(msg)
