import itertools


def wordlists():
    # Aqui eu declaro uma lista de palavras-chave
    palavras_chave = ['nomecavalo', 'nomegato', 'nomecachorro', 'nome', 'sobrenome', 'nomemae', 'nomepai', 'nomefilho', 'nomefilha',
                      'nomeavo','2301', '1987', 'usuario', 'computador',
                      'admin', 'root', 'data', 'aniversario', 'bandafavorita']

    # Aqui eu faço combinações e permutações de palavras-chave
    combinacoes = itertools.combinations(palavras_chave, 2)
    permutacoes = itertools.permutations(palavras_chave, 2)

    # Aqui eu declaro caracteres especiais para inserir em algumas combinações
    caracteres_especiais = ['@', '#', '$', '!', '*', '?']

    # Aqui eu crio uma lista que será a lista de saída e adiciono a ela as combinações e permutações feitas
    wordlist = []
    for c in combinacoes:
        wordlist.append(''.join(c))

    for p in permutacoes:
        wordlist.append(''.join(p))

    # Aqui eu adicionando os caracteres_especiais
    for palavra in palavras_chave:
        for m in caracteres_especiais:
            wordlist.append(palavra + m)
        for i in caracteres_especiais:
            wordlist.append(i + palavra)

    # Aqui eu removo duplicatas e depois salvo a wordlist num txt de mesmo nome
    wordlist = list(set(wordlist))

    with open('wordlist.txt', 'w') as arquivo:
        arquivo.write('\n'.join(wordlist))