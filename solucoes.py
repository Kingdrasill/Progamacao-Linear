import numpy as np
from itertools import combinations

def calcularSolucoes(n, m, c, A, b):
    solucoes = []

    # Converte as listas de coeficientes e termos independentes para arrays do NumPy
    c = np.array(c)
    A = np.matrix(A)
    b = np.array(b).reshape(-1, 1)  # Converte b para uma matriz coluna

    # Todas as combinações possíveis de variáveis com exatamente n - m variáveis fixadas
    var_comb = combinations(range(n), n - m)

    # Itera sobre todas as combinações de variáveis
    for fixed_vars in var_comb:
        solucao = []
        
        # Remove as variáveis fixadas da matriz A
        A_temp = np.delete(A, fixed_vars, axis=1)

        try:
            # Resolve o sistema linear com a nova matriz A_temp
            valores_x_temp = np.linalg.solve(A_temp, b)
            
            # Preenche os valores fixados como zero
            valores_x = np.zeros(n)
            indicies_nao_zero = [k for k in range(n) if k not in fixed_vars]
            valores_x[indicies_nao_zero] = valores_x_temp.flatten()
            
            # Calcula o valor de z
            z = np.dot(c, valores_x)

            # Adiciona os valores de x, z e a viabilidade da solução à lista de soluções
            solucao.append(valores_x)
            solucao.append(z)
            if min(valores_x) < 0:
                solucao.append('inviável')
            else:
                solucao.append('viável')
            
            solucoes.append(solucao)
        except np.linalg.LinAlgError:
            # Se ocorrer um erro devido à singularidade da matriz A_temp, continua para a próxima iteração
            continue
    
    return solucoes
