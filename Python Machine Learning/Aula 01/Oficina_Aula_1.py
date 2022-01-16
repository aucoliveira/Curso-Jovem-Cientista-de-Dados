"""
    Depois de aprender bastante sobre programação funcional nesta aula, chegou o momento de colocar seus conhecimentos em prática para resolver o 
    problema proposto nesta oficina. Para isso, imagine o seguinte caso:

    Você foi chamado para trabalhar como novo programador Python para o aplicativo Spotify, 
    analisando as avaliações de músicas pelos usuários. O seu chefe está muito entusiasmado com a sua chegada
    e já pensou em várias perguntas para você responder. Ele coletou diversas avaliações dos gêneros musicais Rock e Pop.

    Em cada avaliação o usuário pode dar uma nota em quantidade de estrelas para uma música, de 1 a 5. 
    Ele quer que você mapeie as avaliações numéricas em categorias: 
    entre 0 e 1 estrelas é uma música ruim, entre 2 e 3 é uma música mediana e entre 4 e 5 são para as músicas boas.
    O seu papel é dizer para o seu chefe quantas músicas ruins, medianas e boas existem para cada gênero: Rock e Pop.

    Além disso, ele quer saber se existe alguma música mediana de Rock e se todas as músicas de Pop são boas.
    Por fim, quer saber qual gênero musical teve uma maior quantidade de músicas boas. Abaixo seguem as notas de cada gênero.

    notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
    notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

    Pronto, com essas informações você pode começar a desenvolver um programa em Python capaz de responder as perguntas do seu chefe.

    Boa prática!
"""

notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

def categoria(notas):
    if notas <= 1:
        return 'ruim'
    elif notas >= 2 and notas <=3:
        return 'mediana'
    else:
        return 'boa'

classificacao_rock = list(map(categoria,notas_rock))
print('Rock: ',classificacao_rock)
print()
classificacao_pop = list(map(categoria, notas_pop))
print('Pop: ',classificacao_pop)

musica_rock_ruim = list(filter(lambda x: x == 'ruim',classificacao_rock))
musica_rock_mediana = list(filter(lambda x: x =='mediana', classificacao_rock))
musica_rock_boa = list(filter(lambda x: x =='boa', classificacao_rock))
print()
print('Rock: ',len(musica_rock_ruim), len(musica_rock_mediana), len(musica_rock_boa))
musica_pop_ruim = list(filter(lambda x: x =='ruim', classificacao_pop))
musica_pop_mediana = list(filter(lambda x: x =='mediana', classificacao_pop))
musica_pop_boa = list(filter(lambda x: x =='boa', classificacao_pop))
print()
print('Pop: ',len(musica_pop_ruim), len(musica_pop_mediana), len(musica_pop_boa))

musica_rock_booleana = list(map(lambda x: x =='mediana', classificacao_rock))
print()
print('Rock: ',musica_rock_booleana)

musica_pop_boleanda = list(map(lambda x: x =='boa', classificacao_pop))
print()
print('Pop:',musica_pop_boleanda)

print()
print('Existe alguma música mediada de rock? ', any(musica_rock_booleana))
print('Todas as músicas pops são boas? ', all(musica_pop_boleanda))
print()
print('Rock músicas boas:',classificacao_rock.count('boa'))
print('Pop músicas boas:', classificacao_pop.count('boa'))

