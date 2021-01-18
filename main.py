from time import sleep
import utility
import data
import sys
import getpass

login="1"
senha="1"
r=1
resp=99

#Tela de login

while True:
    utility.limpatela()
    utility.tela_login()
    login=input("Login: ")
    if login=="0":
        print("...Aplicação encerrada")
        sys.exit()  # encerra a aplicação

    #comente as linhas de senha para ativar ou desativar o getpass

    senha=input("Senha: ")
    #senha=getpass.getpass("Senha: ")
    val_login=data.login(login,senha)
    if val_login==1:
        break


while resp!=0:
    utility.menu()
    resp = int(input())

    if resp==1:
        utility.limpatela()
        utility.cadastroNotas()
        #criar uma função que retorne um valor para a variável res
        #essa validação precisa ficar dentro da função, bjs
        utility.limpatela()

    elif resp==2:
        utility.limpatela()

        print("=" * 57)
        print(" "*20,"BOLETIM DE NOTAS")
        print("=" * 57)
        v_boletim=int(input("1 - Boletim Completo\n2 - Pesquisar boletim\n0 - Voltar ao menu\n"))
        if v_boletim==1:
            utility.boletimCompleto()
        elif v_boletim==2:
            utility.pesquisarBoletim()
        elif v_boletim==0:
            utility.limpatela()
        else:
            print("Opção Inválida")

    elif resp==3:
        utility.limpatela()
        data.senha()
        utility.limpatela()
        utility.systemconfig()


    elif resp==0:
        print("Aplicação Encerrada")
        break

    else:
        print("Opção inválida, digite um número de acordo com o menu")
        sleep(2)