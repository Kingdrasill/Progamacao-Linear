def lerEntrada(nome):
    file = open(nome, 'r')

    try:
        string_values = file.readline().split(' ')
        (n, m) = tuple([int(i) for i in string_values])
    except:
        return (False, 'Houve um erro ao ler os valores de n e m', None, None, None, None, None)

    try:
        string_coeficientes = file.readline().split(' ')
        c = list([int(i) for i in string_coeficientes])
        if len(c) != n:
            return (False, 'O número de coeficientes é diferente do número de variáveis de decisão', None, None, None, None, None)
    except:
        return (False, 'Não foi encontrada a linha dos coeficientes', None, None, None, None, None)
        
    A = []
    try:
        for j in range(m):
            string_restricao = file.readline().split(' ')
            restricao = list([int(i) for i in string_restricao])
            if len(restricao) != n:
                return (False, 'O número de valores na restrição é diferente do número de variáveis de decisão', None, None, None, None, None)
            A.append(restricao)
    except:
        return (False, 'Não foi encontrada todas as linhas de restrições', None, None, None, None, None)

    try:
        string_termos = file.readline().split(' ')
        b = list([int(i) for i in string_termos])
        if len(b) != m:
            return (False, 'O número de termos independentes é diferente do número de restrições', None, None, None, None, None)
    except:
        return (False, 'Não foi encontrada a linha dos termos independentes das restrições', None, None, None, None, None)
    
    return (True, '', n, m, c, A, b)