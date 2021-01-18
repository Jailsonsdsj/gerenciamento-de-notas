from time import sleep
from math import ceil
from random import choice, random,randint
from random import uniform


import data
import getpass

#Declaração de variáveis
cadastro=dict()
dados=list()



#chaves de dados:
'''
0 - nome
1 - mat
2 - faltas
3 - n1
4 - n2
5 - n3
6 - n4
7 - med
8 - sit
'''


def tela_login():

    print("="*57)
    print("                    SISTEMA DE NOTAS")
    print("="*57)
    print("Digite zero a qualquer momento para encerrar a aplicação")
    print("-"*57)


def menu():
    print("=" * 57)
    print("                    SISTEMA DE NOTAS")
    print("=" * 57)
    print(f'Usuário: {data.user}    |    Tipo de Perfil: {data.tipo}')
    print("-" * 57)
    print("")
    print("Escolha uma opção: \n"
          "1 - Cadastrar notas de aluno\n"
          "2 - Boletim de notas\n"
          "3 - Configurações do Sistema\n"
          "0 - Encerrar aplicação\n")


def cadastroNotas():
    stop_cadastro=1
    while stop_cadastro==1:
        print("=" * 57)
        print("                    CADASTRO DE NOTAS")
        print("=" * 57)

        cadastro['nome'] = str(input("Nome completo: "))
        #Validação dos 8 dígidos da matrícula
        while True:
            x = 0
            y = 1
            cadastro['mat'] = str(input("Matrícula: "))
            if len(cadastro['mat']) != 8:
                print("Erro: A matrícula deve conter 8 dígitos. Tente novamente.\n")
                x=1

            elif y==1:
                for i in range(len(dados)):
                    if dados[i]['mat'] == cadastro['mat']:
                        print("A matrícula já está em uso. \n")
                        x = 1
            if x==0:
                break


        #preenchimento das notas
        while True:
            cadastro['n1'] = float(input("Nota da 1ª Avaliação: "))
            if cadastro['n1'] > 10 or cadastro['n1'] <0:
                print("Nota inválida. Insira um valor entre 0 e 10.\n")
            else:
                break
        while True:
            cadastro['n2'] = float(input("Nota da 2ª Avaliação: "))
            if cadastro['n2'] > 10 or cadastro['n2'] <0:
                print("Nota inválida. Insira um valor entre 0 e 10.\n")
            else:
                break
        while True:
            cadastro['n3'] = float(input("Nota da 3ª Avaliação: "))
            if cadastro['n3'] > 10 or cadastro['n3'] <0:
                print("Nota inválida. Insira um valor entre 0 e 10.\n")
            else:
                break
        while True:
            cadastro['n4'] = float(input("Nota da 4ª Avaliação: "))
            if cadastro['n4'] > 10 or cadastro['n4'] <0:
                print("Nota inválida. Insira um valor entre 0 e 10.\n")
            else:
                break



        #cálculo da média e situação
        cadastro['med'],cadastro['sit'] = novaMedia(cadastro['n1'],cadastro['n2'],cadastro['n3'],cadastro['n4'])

        #a situação REPROVADO F deve ser insarida após o calculo das notas, para que seja sobreescrita
        cadastro['faltas'] = int(input("Quantidade da Faltas: "))
        if cadastro['faltas'] > data.min_faltas:
            cadastro['sit'] = "REPROVADO F"

        print("")
        print("Dados cadastrados com sucesso!")
        print("-" * 30)
        print(f"Nome: {cadastro['nome']}")
        print(f"Matrícula: {cadastro['mat']}")
        print(f"Notas: {cadastro['n1']} | {cadastro['n2']} | {cadastro['n3']} | {cadastro['n4']}")


        dados.append(cadastro.copy())
        cadastro.clear()
        stop_cadastro = int(input("\n1 - Cadastrar outro aluno\n"
                                    "2 - Voltar ao menu principal\n"))
        if stop_cadastro =="2":
            break
        limpatela()


def boletimCompleto():
    tot_aprovados = 0
    tot_reprovados = 0
    tot_aprovadosf = 0
    tot_recuperacao = 0
    limpatela()
    print("=" * 145)
    print(" "*68,"BOLETIM COMPLETO")
    print("=" * 145)

    if len(dados) == 0:
        print("Boletim Vazio")
        stop()
        limpatela()
    else:
        # ajustando a largura da coluna nome
        txt = "a"
        for i in range(0, len(dados)):
            if len(dados[i]['nome']) > len(txt):
                txt = dados[i]['nome']
        txt = len(txt)
        txt2 = ceil(txt / 2) - 4

        '''
        Antes de tudo, eu calculei a coluna que mais pode variar de tamanho: o nome. 
        O esse cálculo será utilizado para ajustar a largura da coluna  NOME de acordo com o maior nome cadastrado.

        Após armazenar a quantidade de letras da maior String de 'nome' no laço for, é feia a divisão desse número pela
        metade e jogado o valor na variável txt2, para que 50% da quantidade de caracteres seja preenchida por espaços 
        em branco ao lado esquerdo e a outra metade ao lado direito da palavra NOME. Lembrando que a quantidade de caractere 
        do título da coluna também conta, e deve ser dividido pela metade e somado aos 50% que foram distribuídos para cada lado.

        A função ceil arredonda o número float para o seu sucessor inteiro, já que não é possível
        multiplicar strings por números reais.

        Representação na matemática:
        (qnt de caracteres em branco + (qnt de caracteres da coluna / 2)) + (qnt de caracteres em branco + (qnt de caracteres da coluna / 2))

        Representação na programação:
        txt2 = ceil(txt / 2) - 4
        - txt2 recebe o sucessor mais próximo da quantidade de caractere divida por dois, menos a quantidade de caractere da palavra NOME (4) 

        '''
        # fim do ajuste
        print("ID    |"," "*txt2," NOME "," "*txt2,"|  MATRÍCULA | QNT. DE FALTAS | NOTA 1 | NOTA 2 | NOTA 3 | NOTA 4 | MÉDIA | SITUAÇÃO")
        print("-" * 145)
        for i in range(0, len(dados)):
            if i <10:
                print(i,"   ", end="")
            elif i>=10 and i<100:
                print(i,"  ", end="")
            elif i>=100:
                print(i,end="  ")
            print(
                  " |",dados[i]['nome']," "*ceil(txt-len(dados[i]['nome'])),
                  "|",dados[i]['mat']," "*ceil(9-len(str(dados[i]['mat']))),
                  "|",dados[i]['faltas']," "*ceil(13-len(str(dados[i]['faltas']))),
                  "|",dados[i]['n1']," "*ceil(5-len(str(dados[i]['n1']))),
                  "|",dados[i]['n2']," "*ceil(5-len(str(dados[i]['n2']))),
                  "|",dados[i]['n3']," "*ceil(5-len(str(dados[i]['n3']))),
                  "|",dados[i]['n4']," "*ceil(5-len(str(dados[i]['n4']))),
                  "|",dados[i]['med']," "*ceil(4-len(str(dados[i]['med']))),
                  "|",dados[i]['sit']," "*ceil(8-len(str(dados[i]['sit']))))
            #aproveitando o laço for para gerar o analytcs
            if dados[i]['sit']=="APROVADO":
                tot_aprovados+=1
            elif dados[i]['sit']=="REPROVADO":
                tot_reprovados += 1
            elif dados[i]['sit']=="REPROVADO F":
                tot_aprovadosf += 1
            elif dados[i]['sit']=="RECUPERAÇÃO":
                tot_recuperacao += 1

        #calculando a média global

        print("-" * 145)
        print("Dica: amplie a largura da tela para visualizar melhor a tabela\n\n")

        print(f'ANALYTICS: \n'
              f'{tot_aprovados} aprovado(s) | {tot_recuperacao} em recuperação | '
              f'{tot_aprovadosf} reprovado(s) por falta | {tot_reprovados} reprovado(s) por média')

        tot_med = 0
        for i in range(0, len(dados)):
            tot_med += dados[i]['med']
        med_global = tot_med / (len(dados))
        print("Média Global: {:.2f}\n".format(med_global))
        stop()
        limpatela()


def pesquisarBoletim():
    limpatela()
    print("=" * 130)
    print(" " * 57, "PESQUISAR POR BOLETIM")
    print("=" * 130)
    src=str(input("Informe o nome completo ou matrícula: "))
    found="a"
    # ajustando a largura da coluna nome
    txt = "a"
    for i in range(0, len(dados)):
        if len(dados[i]['nome']) > len(txt):
            txt = dados[i]['nome']
    txt = len(txt)
    txt2 = ceil(txt / 2) - 4
    '''
    Antes de tudo, eu calculei a coluna que mais pode variar de tamanho, o nome. 
    O esse cálculo será utilizado para ajustar a largura da coluna  NOME de acordo com o maior nome cadastrado.

    Após armazenar a quantidade de letras da maior String de 'nome', no laço for, é feia a divisão desse número pela
    metade e jogado o valor na variável txt2, para que 50% da quantidade de caracteres seja preenchida por espaços 
    em branco ao lado esquerdo e a outra metade ao lado direito da palavra NOME. Lembrando que a quantidade de caractere 
    do título da coluna também conta, e deve ser dividido pela metade e somado aos 50% que foram distribuídos para cada lado.

    A função ceil arredonda o número float para o seu sucessor inteiro, já que não é possível
    multiplicar strings por números reais.

    Representação na matemática:
    (qnt de caracteres em branco + (qnt de caracteres da coluna / 2)) + (qnt de caracteres em branco + (qnt de caracteres da coluna / 2))

    Representação na programação:
    txt2 = ceil(txt / 2) - 4
    - txt2 recebe o sucessor mais próximo da quantidade de caractere divida por dois, menos a quantidade de caractere da palavra NOME (4) 

    '''
    # fim do ajuste


    for j in range(len(dados)):

        for i in range(len(dados)):
            if found == "ok":
                break
            elif dados[i]['mat'] == src or dados[i]['nome'] == src:
                found="ok"

                #A PARTIR DAQUI NÃO HÁ NECESSIDADE DE ALTERAÇÃO NO CÓDIGO
                print("-" * 130)
                print("ID |", " " * txt2, " NOME  ", " " * txt2,
                      "|  MATRÍCULA | QNT. DE FALTAS | NOTA 1 | NOTA 2 | NOTA 3 | NOTA 4 | MÉDIA | SITUAÇÃO")
                print("-" * 130)
                print(i,
                      " | ", dados[i]['nome'], " " * ceil(txt - len(dados[i]['nome'])),
                      "|", dados[i]['mat'], " " * ceil(9 - len(str(dados[i]['mat']))),
                      "|", dados[i]['faltas'], " " * ceil(13 - len(str(dados[i]['faltas']))),
                      "|", dados[i]['n1'], " " * ceil(5 - len(str(dados[i]['n1']))),
                      "|", dados[i]['n2'], " " * ceil(5 - len(str(dados[i]['n2']))),
                      "|", dados[i]['n3'], " " * ceil(5 - len(str(dados[i]['n3']))),
                      "|", dados[i]['n4'], " " * ceil(5 - len(str(dados[i]['n4']))),
                      "|", dados[i]['med'], " " * ceil(4 - len(str(dados[i]['med']))),
                      "|", dados[i]['sit'], " " * ceil(8 - len(str(dados[i]['sit']))))
                print("-" * 130)

                option = int(input("\n1 - Alterar dados\n"
                                     "2 - Remover dados\n"
                                     "3 - Voltar ao Menu\n"))

                if option == 1:
                    #Inserir validação de senha
                    print("")
                    data.senha()
                    option2=int(input("Escolha o registro que deseja ALTERAR\n"
                                      "1 - Nome\n"
                                      "2 - Faltas\n"
                                      "3 - Nota 1\n"
                                      "4 - Nota 2\n"
                                      "5 - Nota 3\n"
                                      "6 - Nota 4\n"
                                      "0 - Voltar ao Menu\n"))
                    if option2 == 1:
                        dados[i]['nome']=str(input("Informe o novo nome: "))
                        print("Nome alterado com sucesso!")
                        stop()
                        limpatela()

                    elif option2 == 2:
                        dados[i]['faltas'] = int(input("Informe a quantidade de faltas: "))
                        if dados[i]['faltas'] > data.min_faltas:
                            dados[i]['sit'] = "REPROVADO F"
                        print("Registro alterado com sucesso!")
                        stop()
                        limpatela()

                    elif option2 == 3:
                        print("\033[1;33mATENÇÃO: A alteração de qualquer nota altera diretamente a média e o resultado final!\033[0;0m")
                        dados[i]['n1'] = float(input("Informe um novo valor para NOTA 1: "))
                        #a alteração é feita através de uma função que retorna, respectivamente, a nova média e a situação
                        dados[i]['med'],dados[i]['sit'] = novaMedia(dados[i]['n1'],dados[i]['n2'],dados[i]['n3'],dados[i]['n4'])

                        print("Nota alterada com sucesso!")
                        stop()
                        limpatela()

                    elif option2 == 4:
                        print("ATENÇÃO: A alteração de qualquer nota altera diretamente a média e o resultado final!")
                        dados[i]['n2'] = float(input("Informe um novo valor para NOTA 2: "))
                        #a alteração é feita através de uma função que retorna, respectivamente, a nova média e a situação
                        dados[i]['med'],dados[i]['sit'] = novaMedia(dados[i]['n1'],dados[i]['n2'],dados[i]['n3'],dados[i]['n4'])

                        print("Nota alterada com sucesso!")
                        stop()
                        limpatela()

                    elif option2 == 5:
                        print("ATENÇÃO: A alteração de qualquer nota altera diretamente a média e o resultado final!")
                        dados[i]['n3'] = float(input("Informe um novo valor para NOTA 3: "))
                        #a alteração é feita através de uma função que retorna, respectivamente, a nova média e a situação
                        dados[i]['med'],dados[i]['sit'] = novaMedia(dados[i]['n1'],dados[i]['n2'],dados[i]['n3'],dados[i]['n4'])

                        print("Nota alterada com sucesso!")
                        stop()
                        limpatela()

                    elif option2 == 6:
                        print("ATENÇÃO: A alteração de qualquer nota altera diretamente a média e o resultado final!")
                        dados[i]['n4'] = float(input("Informe um novo valor para NOTA 4: "))
                        #a alteração é feita através de uma função que retorna, respectivamente, a nova média e a situação
                        dados[i]['med'],dados[i]['sit'] = novaMedia(dados[i]['n1'],dados[i]['n2'],dados[i]['n3'],dados[i]['n4'])

                        print("Nota alterada com sucesso!")
                        stop()
                        limpatela()

                elif option == 2:
                    data.senha()
                    option3 = int(input("Escolha o registro que deseja REMOVER\n"
                                        "1 - Nota 1\n"
                                        "2 - Nota 2\n"
                                        "3 - Nota 3\n"
                                        "4 - Nota 4\n"
                                        "5 - Registro completo\n"
                                        "\033[1;31mATENÇÃO: A Remoção de qualquer nota afeta diretamente a média e, consequentemente, o resultado final.\n"
                                        "Digite 0 para cancelar\033[0;0m\n"))

                    if option3==1:
                        dados[i]['n1']=0
                        # a alteração é feita através de uma função que retorna, respectivamente, a nova média e a situação
                        dados[i]['med'], dados[i]['sit'] = novaMedia(dados[i]['n1'], dados[i]['n2'], dados[i]['n3'], dados[i]['n4'])
                        print("NOTA 1 removida com sucesso!")
                        stop()


                    elif option3==2:
                        dados[i]['n2']=0
                        # a alteração é feita através de uma função que retorna, respectivamente, a nova média e a situação
                        dados[i]['med'], dados[i]['sit'] = novaMedia(dados[i]['n1'], dados[i]['n2'], dados[i]['n3'], dados[i]['n4'])
                        print("NOTA 2 removida com sucesso!")
                        stop()
                    elif option3==3:
                        dados[i]['n3'] = 0
                        # a alteração é feita através de uma função que retorna, respectivamente, a nova média e a situação
                        dados[i]['med'], dados[i]['sit'] = novaMedia(dados[i]['n1'], dados[i]['n2'], dados[i]['n3'], dados[i]['n4'])
                        print("NOTA 3 removida com sucesso!")
                        stop()
                    elif option3==4:
                        dados[i]['n4'] = 0
                        # a alteração é feita através de uma função que retorna, respectivamente, a nova média e a situação
                        dados[i]['med'], dados[i]['sit'] = novaMedia(dados[i]['n1'], dados[i]['n2'], dados[i]['n3'], dados[i]['n4'])
                        print("NOTA 4 removida com sucesso!")
                        stop()

                    elif option3 == 5:
                        dados.pop(i)
                        print("Registro Removido")
                        stop()
                    else:
                        print("Operação cancelada!")
                        stop()

                elif option == 3:
                    found = "ok"
                    break
                    limpatela()
                else:
                    print("Opção Inválida")

        if found == "ok":
            break
        if found != "ok":
            print("Registro não encontrado")
            stop()
            break


    limpatela()


def systemconfig():

    print("=" * 57)
    print("             CONFIGURAÇÕES DO SISTEMA")
    print("=" * 57)

    config1=int(input("1 - Alterar Login\n"
                      "2 - Alterar Senha\n"
                      "3 - Alterar quantidade máxima de faltas\n"
                      "4 - Alterar critérios de situação\n"
                      "5 - Inserir Cadastros em Lote\n"
                      "6 - Limpar boletim\n"
                      "0 - Voltar ao Menu\n"))
    limpatela()
    if config1==1:
        limpatela()
        print("-" * 57)
        print("            ALTERAÇÃO DO LOGIN")
        print("-" * 57)
        data.user=str(input("Digite o novo login: "))
        print("Login alterado com sucesso!")
        stop()

    elif config1==2:
        limpatela()
        while True:
            print("-" * 57)
            print("                 ALTERAÇÃO DA SENHA")
            print("-" * 57)
            senha_antiga=getpass.getpass("Digite a senha antiga: ")
            if senha_antiga==data.pas:
                while True:
                    senha_nova1=getpass.getpass("Informe a nova senha: ")
                    senha_nova2=getpass.getpass("Confirme a nova senha: ")
                    if senha_nova1==senha_nova2:
                        data.pas = senha_nova2

                        print("\nSenha alterada com sucesso!")
                        stop()
                        limpatela()
                        break

                    else:
                        print("\nAs senhas não conferem. Tente novamente")
                break
            else:
                print("Senha incorreta")
                limpatela()

    elif config1==3:
        limpatela()
        print("-" * 57)
        print("    ALTERAÇÃO DA QUANTIDADE MÁXIMA DE FALTAS")
        print("-" * 57)
        print("OBSERVAÇÃO: A nova taxa de reprovação por faltas só passará a valer a patir dos próximos cadastros.\n"
              "            As notas já cadastradas no sistema permacenem com a taxa mínima antiga. Ou seja, nenhuma nota atual\n"
              "            será afetada.\n")
        data.min_faltas=int(input("Informe a nova taxa mínima de faltas: "))
        print("\n Alteração realizada com sucesso!")
        stop()

    elif config1==4:
        limpatela()
        while True:
            print("-" * 59)
            print("      ALTERAÇÃO DA QUANTIDADE MÍNIMA DE APROVEITAMENTO")
            print("-" * 59)
            print("OBSERVAÇÃO: O novo critério de situação só passará a\n"
                  "            valer a patir dos próximos cadastros.\n"
                  "            As notas já cadastradas no sistema permanecem\n"
                  "            com a os critérios antigos. Ou seja, nenhuma\n"
                  "            nota atual será afetada.\n")

            data.aprovacao = float(input("Informe nota MÍNIMA de APROVEITAMENTO: "))
            data.recuperacao1 = float(input("Infomre nota MÁXIMA para RECUPERAÇÃO: "))
            if data.recuperacao1 >= data.aprovacao:
                print("\nOperação Inválida.\n"
                      "A nota MÍNIMA de recuperação deve ser inferior à nota de APROVEITAMENTO.\n")
                stop2()
            else:
                data.recuperacao2 = float(input("Informe a nota MÍNIMA para RECUPERAÇÃO: "))
                if data.recuperacao2 >= data.aprovacao or data.recuperacao2 >= data.recuperacao1:
                    print("\nOperação Inválida.\n"
                            "A nota MÍNIMA de recuperação deve ser inferior à nota de APROVEITAMENTO e inferior à nota MÁXIMA de RECUPERAÇÃO\n")
                    stop2()

                else:
                    data.reprovacao = float(input("Informe a MÁXIMA para REPROVAÇÃO: "))
                    if data.reprovacao>=data.aprovacao or data.reprovacao>=data.recuperacao2 or data.reprovacao>=data.recuperacao1:
                        print("\nOperação Inválida.\n"
                                "A nota MÁXIMA de REPROVAÇÃO deve ser inferior ou diferente das notas de APROVAÇÃO e RECUPERAÇÃO.\n")
                        stop2()
                    else:
                        print("\n Alteração realizada com sucesso!\n")
                        print(f"Nota mínima para aprovação: {data.aprovacao}\n"
                              f"Notas mínimas para recuperação: Entre {data.recuperacao1} e {data.recuperacao2}\n"
                              f"Nota máxima para reprovação: {data.reprovacao}\n")
                        stop()
                        limpatela()
                        break

    elif config1==5:

        print("-" * 70)
        print(" "*25,"INSERIR DADOS EM LOTE")
        print("-" * 70)
        qnt=int(input("Informe a quantidade de usuários para cadastrar automaticamente: "))
        while True:
            situacao_lote=int(input("Infome a situação dos dados cadastrados:\n"
                  "1 - Aprovados\n"
                  "2 - Recuperação\n"
                  "3 - Reprovados\n"
                  "4 - Reprovados por falta\n"
                  "5 - Aleatório\n"
                  "0 - Cancelar"))

            if situacao_lote==1:
                for i in range(1, qnt + 1):
                    cadastro['nome'] = choice(data.nomescompletos).capitalize()
                    #[ERRO] inserir um verificador de matrícula igual

                    cadastro['mat'] = str(randint(10000000,99999999))
                    cadastro['n1'] = randint(data.aprovacao, 10)
                    cadastro['n2'] = randint(data.aprovacao, 10)
                    cadastro['n3'] = randint(data.aprovacao, 10)
                    cadastro['n4'] = randint(data.aprovacao, 10)
                    cadastro['med'], cadastro['sit'] = novaMedia(cadastro['n1'], cadastro['n2'], cadastro['n3'],
                                                                 cadastro['n4'])
                    cadastro['faltas'] = randint(0, data.min_faltas)
                    if cadastro['faltas'] > data.min_faltas:
                        cadastro['sit'] = "REPROVADO F"
                    dados.append(cadastro.copy())
                    cadastro.clear()

                print(f"{qnt} Registros de situação APROVADO foram inseridos!")
                stop()
                limpatela()
                break


            elif situacao_lote == 2:

                for i in range(1, qnt + 1):
                    cadastro['nome'] = choice(data.nomescompletos).capitalize()
                    # [ERRO] inserir um verificador de matrícula igual
                    cadastro['mat'] = str(randint(10000000, 99999999))
                    cadastro['n1'] = round(uniform(data.recuperacao2,data.recuperacao1),1)
                    cadastro['n2'] = round(uniform(data.recuperacao2,data.recuperacao1),1)
                    cadastro['n3'] = round(uniform(data.recuperacao2,data.recuperacao1),1)
                    cadastro['n4'] = round(uniform(data.recuperacao2,data.recuperacao1),1)
                    cadastro['med'], cadastro['sit'] = novaMedia(cadastro['n1'], cadastro['n2'], cadastro['n3'],
                                                                 cadastro['n4'])
                    cadastro['faltas'] = randint(0, data.min_faltas)
                    if cadastro['faltas'] > data.min_faltas:
                        cadastro['sit'] = "REPROVADO F"

                    dados.append(cadastro.copy())
                    cadastro.clear()

                print(f"{qnt} Registros de situação RECUPERAÇÂO foram inseridos!")
                stop()
                limpatela()
                break


            elif situacao_lote == 3:
                for i in range(1, qnt + 1):
                    cadastro['nome'] = choice(data.nomescompletos).capitalize()
                    # [ERRO] inserir um verificador de matrícula igual
                    cadastro['mat'] = str(randint(10000000, 99999999))
                    cadastro['n1'] = round(uniform(0,data.reprovacao),1)
                    cadastro['n2'] = round(uniform(0,data.reprovacao),1)
                    cadastro['n3'] = round(uniform(0,data.reprovacao),1)
                    cadastro['n4'] = round(uniform(0,data.reprovacao),1)
                    cadastro['med'], cadastro['sit'] = novaMedia(cadastro['n1'], cadastro['n2'], cadastro['n3'],
                                                                 cadastro['n4'])
                    cadastro['faltas'] = randint(0, data.min_faltas)
                    if cadastro['faltas'] > data.min_faltas:
                        cadastro['sit'] = "REPROVADO F"

                    dados.append(cadastro.copy())
                    cadastro.clear()

                print(f"{qnt} Registros de situação REPROVADO foram inseridos!")
                stop()
                limpatela()
                break


            elif situacao_lote==4:
                for i in range(1,qnt+1):
                    cadastro['nome'] = choice(data.nomescompletos).capitalize()
                    # [ERRO] inserir um verificador de matrícula igual
                    cadastro['mat'] = str(randint(10000000,99999999))
                    cadastro['n1'] = round(uniform(0,10),1)
                    cadastro['n2'] = round(uniform(0,10),1)
                    cadastro['n3'] = round(uniform(0,10),1)
                    cadastro['n4'] = round(uniform(0,10),1)
                    cadastro['med'], cadastro['sit'] = novaMedia(cadastro['n1'], cadastro['n2'], cadastro['n3'], cadastro['n4'])
                    cadastro['faltas'] = randint(data.min_faltas+1, data.min_faltas+5)
                    if cadastro['faltas'] > data.min_faltas:
                        cadastro['sit'] = "REPROVADO F"

                    dados.append(cadastro.copy())
                    cadastro.clear()

                print(f"{qnt} Registros em situação REPROVADO F foram inseridos!")
                stop()
                limpatela()

                break


            elif situacao_lote==5:
                for i in range(1,qnt+1):
                    cadastro['nome'] = choice(data.nomescompletos).capitalize()
                    cadastro['mat'] = str(randint(10000000,99999999))
                    cadastro['n1'] = round(uniform(0,10),1)
                    cadastro['n2'] = round(uniform(0,10),1)
                    cadastro['n3'] = round(uniform(0,10),1)
                    cadastro['n4'] = round(uniform(0,10),1)
                    cadastro['med'], cadastro['sit'] = novaMedia(cadastro['n1'], cadastro['n2'], cadastro['n3'], cadastro['n4'])
                    cadastro['faltas'] = randint(0, 12)
                    if cadastro['faltas'] > data.min_faltas:
                        cadastro['sit'] = "REPROVADO F"

                    dados.append(cadastro.copy())
                    cadastro.clear()

                print(f"{qnt} Registros aleatórios foram inseridos!")
                stop()
                limpatela()

                break


            elif situacao_lote == 0:
                print("Ação cancelada.")
                stop()
                limpatela()
                break


            else:
                print("Opção inválida.\n")
                stop2()
                limpatela()


    elif config1==6:
        print("-" * 57)
        print("                     LIMPAR BOLETIM")
        print("-" * 57)
        limpardados=int(input("Tem certeza que deseja limpar TODAS as notas cadastradas\n"
                              "no sistema? A ação é irreversível.\n"
                              "1 - Sim\n"
                              "2 - Não\n"))
        if limpardados == 1:
            data.senha()
            dados.clear()
            print("\nTodos os registros foram excluídos.")
            stop()
            limpatela()

        elif limpardados == 2:
            print("\nOperação cancelada!")
            stop()
            limpatela()


#SUB FUNÇÕES
def novaMedia(n1=0,n2=0,n3=0,n4=0):
    media=(n1+n2+n3+n4)/4
    media= round(media,1) #arredondar o número quebrado para o próximo número inteiro
    if media >= data.aprovacao:
        return media,"APROVADO"

    elif media <= data.recuperacao1 and media >= data.recuperacao2:
        return media,"RECUPERAÇÃO"

    elif media <= data.reprovacao:
        return media,"REPROVADO"
    else:
        media = 0
        return media,"ERRO_035"
        #O erro 35 acontece quando a nota obtida não se encontra no critério de situação.


def limpatela():
    sleep(1)
    for i in range(0,50):
        print(".")


def stop():
    stop = input("--------------------------------------\n"
            "Digite 0 para voltar ao menu principal\n")


def stop2():
    stop2 = input("--------------------------------------\n"
                 "Digite 0 para continuar\n")





